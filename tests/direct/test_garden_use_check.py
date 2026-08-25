"""Direct tests for rotation history, challenge, and seasonal closure."""

import json


CONTEXT = "Raised community plot with full sun, clay-loam soil, drip irrigation, and a documented tomato disease concern."
POLICY = "Avoid repeating the same crop family within two seasons and reject plans that ignore documented disease pressure."
PLAN = "Plant beans in the northern bed with compost amendment, drip irrigation, and weekly disease inspection."


def _plot(contract, direct_vm, owner):
    direct_vm.sender = owner
    return contract.create_plot("PLOT-A", CONTEXT, POLICY, 2)


def _proposal(contract, direct_vm, owner, plot_id, key="SPRING", season=1, family="LEGUME", verdict="SUITABLE"):
    direct_vm.sender = owner
    direct_vm.mock_llm(
        r".*Evaluate a proposed planting.*",
        json.dumps({"verdict": verdict, "conditions": [] if verdict != "CONDITIONAL" else ["Add drainage monitoring."]}),
    )
    return contract.evaluate_planting(plot_id, key, season, family, PLAN)


def test_plot_registration_records_rotation_gap(contract, direct_vm, direct_alice):
    plot_id = _plot(contract, direct_vm, direct_alice)
    assert contract.get_plot(plot_id)["same_family_gap"] == 2
    assert contract.get_history_count(plot_id) == 0


def test_only_plot_owner_can_propose(contract, direct_vm, direct_alice, direct_bob):
    plot_id = _plot(contract, direct_vm, direct_alice)
    direct_vm.sender = direct_bob
    with direct_vm.expect_revert("only_plot_owner"):
        contract.evaluate_planting(plot_id, "BAD", 1, "LEGUME", PLAN)


def test_suitable_proposal_commits_and_closes_into_history(contract, direct_vm, direct_alice):
    plot_id = _plot(contract, direct_vm, direct_alice)
    proposal_id = _proposal(contract, direct_vm, direct_alice, plot_id)
    contract.commit_planting(proposal_id)
    contract.close_season(proposal_id, "Beans established successfully and the plot remained free of observed disease.")
    assert contract.get_proposal(proposal_id)["state"] == "CLOSED"
    assert contract.get_history_count(plot_id) == 1
    assert contract.get_history(plot_id, 0)["crop_family"] == "LEGUME"


def test_same_family_gap_is_enforced_from_history(contract, direct_vm, direct_alice):
    plot_id = _plot(contract, direct_vm, direct_alice)
    first = _proposal(contract, direct_vm, direct_alice, plot_id)
    contract.commit_planting(first)
    contract.close_season(first, "The first legume crop completed with acceptable soil and disease observations.")
    with direct_vm.expect_revert("same_family_gap_not_met"):
        contract.evaluate_planting(plot_id, "TOO-SOON", 2, "LEGUME", PLAN)


def test_independent_challenge_can_block_commit(contract, direct_vm, direct_alice, direct_bob):
    plot_id = _plot(contract, direct_vm, direct_alice)
    proposal_id = _proposal(contract, direct_vm, direct_alice, plot_id)
    direct_vm.sender = direct_bob
    direct_vm.mock_llm(r".*Review a planting decision challenge.*", json.dumps({"result": "BLOCK"}))
    result = contract.challenge_proposal(
        proposal_id,
        "The supplied disease log documents the same crop-family pathogen in this bed during the prior season.",
    )
    assert result == "BLOCK"
    direct_vm.sender = direct_alice
    with direct_vm.expect_revert("proposal_blocked"):
        contract.commit_planting(proposal_id)


def test_plot_owner_cannot_self_challenge(contract, direct_vm, direct_alice):
    plot_id = _plot(contract, direct_vm, direct_alice)
    proposal_id = _proposal(contract, direct_vm, direct_alice, plot_id)
    with direct_vm.expect_revert("owner_cannot_challenge"):
        contract.challenge_proposal(proposal_id, "Owner-authored counter evidence is intentionally not an independent challenge.")


def test_invalid_model_verdict_leaves_no_proposal(contract, direct_vm, direct_alice):
    plot_id = _plot(contract, direct_vm, direct_alice)
    direct_vm.mock_llm(
        r".*Evaluate a proposed planting.*",
        json.dumps({"verdict": "PERFECT", "conditions": []}),
    )
    with direct_vm.expect_revert("invalid_verdict"):
        contract.evaluate_planting(plot_id, "BAD-AI", 1, "LEGUME", PLAN)
