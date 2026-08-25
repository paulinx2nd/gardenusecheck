# GardenUseCheck

A reusable crop-rotation ledger that binds every new planting proposal to prior closed seasons, supports an independent challenge, and appends outcomes only after owner commitment.

## Why GenLayer

Validators independently derive the proposal verdict and conditions; a separate consensus pass adjudicates challenge counter-evidence. A non-blocked commit advances the plot season, while closure appends the crop family and observed outcome to the immutable history sequence.

## Roles

- plot owner
- independent challenger
- GenLayer validators

## Lifecycle

create plot -> evaluate proposal against history -> optional challenge -> owner commit -> close season into history

## Contract interface

- Constructor: none
- Write methods: challenge_proposal, close_season, commit_planting, create_plot, evaluate_planting
- View methods: can_repeat_family, get_history, get_history_count, get_plot, get_proposal
- Runner: `py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6`

## Public-data warning

All contract inputs, evidence, notes, addresses, model results, and state are public. Do not submit secrets, private documents, personal contact information, or confidential identifiers.

## Source model

No external data collection occurs. Plot context, policy, plan, challenge, and outcome are public caller-attested snapshots.

## Verification

```text
genvm-lint check contracts/garden_use_check.py
genvm-lint typecheck contracts/garden_use_check.py --strict
python -m pytest tests/direct -q
python tests/run_glsim.py --port 4000 --validators 5 --no-browser
python -m pytest tests/integration -q -s
```

The repository contains seven direct tests and one full five-validator GLSim flow. StudioNet evidence is recorded separately under `deployments/` after network execution.

## Limitations

The contract does not inspect soil, plants, or disease records. It is an auditable coordination tool, not agronomic or safety advice.

Licensed under MIT. See `LICENSE`.
