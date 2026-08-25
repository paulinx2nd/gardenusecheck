"""Five-validator GLSim flow for a history-bound planting decision."""

import json
from pathlib import Path

from gltest import get_contract_factory, get_validator_factory
from gltest.accounts import create_accounts
from gltest.assertions import tx_execution_succeeded
from gltest.types import TransactionStatus
from gltest.utils import extract_contract_address


def _ok(receipt):
    assert tx_execution_succeeded(receipt), json.dumps(receipt, default=str)


def _context():
    validators = get_validator_factory().batch_create_mock_validators(
        5,
        mock_llm_response={"nondet_exec_prompt": {"Evaluate a proposed planting": json.dumps({"verdict": "SUITABLE", "conditions": []})}},
    )
    return {"validators": [validator.to_dict() for validator in validators]}


def test_five_validator_rotation_commit_and_close():
    owner_account = create_accounts(1)[0]
    factory = get_contract_factory(
        contract_file_path=Path(__file__).resolve().parents[2] / "contracts" / "garden_use_check.py"
    )
    deployed = factory.deploy_contract_tx(args=[], account=owner_account, wait_transaction_status=TransactionStatus.FINALIZED)
    _ok(deployed)
    address = extract_contract_address(deployed)
    owner = factory.build_contract(address, account=owner_account)
    plot_id = f"{str(owner_account.address).lower()}:PLOT-A"
    proposal_id = f"{plot_id}:SPRING"
    _ok(owner.create_plot(args=["PLOT-A", "Raised community plot with full sun, clay-loam soil, drip irrigation, and a documented tomato disease concern.", "Avoid repeating the same crop family within two seasons and reject plans that ignore documented disease pressure.", 2]).transact(wait_transaction_status=TransactionStatus.FINALIZED))
    _ok(owner.evaluate_planting(args=[plot_id, "SPRING", 1, "LEGUME", "Plant beans in the northern bed with compost amendment, drip irrigation, and weekly disease inspection."]).transact(transaction_context=_context(), wait_transaction_status=TransactionStatus.FINALIZED))
    _ok(owner.commit_planting(args=[proposal_id]).transact(wait_transaction_status=TransactionStatus.FINALIZED))
    _ok(owner.close_season(args=[proposal_id, "Beans established successfully and the plot remained free of observed disease."]).transact(wait_transaction_status=TransactionStatus.FINALIZED))
    assert owner.get_history_count(args=[plot_id]).call() == 1
    assert owner.get_proposal(args=[proposal_id]).call()["state"] == "CLOSED"
