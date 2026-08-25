# Reviewer Guide

## Mechanism in one sentence

A reusable crop-rotation ledger that binds every new planting proposal to prior closed seasons, supports an independent challenge, and appends outcomes only after owner commitment.

## What consensus actually decides

Validators independently derive the proposal verdict and conditions; a separate consensus pass adjudicates challenge counter-evidence.

## What code settles afterward

A non-blocked commit advances the plot season, while closure appends the crop family and observed outcome to the immutable history sequence.

## Why this is distinct

The decision is history-dependent and can be challenged by a different wallet before a seasonal event is committed.

## Fast review path

1. Confirm the pinned dependency on the first source line.
2. Inspect the custom validator and verify it reruns the substantive task.
3. Trace role checks and terminal-state guards in each write method.
4. Run lint, strict type checking, seven direct tests, and the five-validator integration test.
5. Compare `abi.json` and the StudioNet manifest to the committed source hash.

## Known limitations

The contract does not inspect soil, plants, or disease records. It is an auditable coordination tool, not agronomic or safety advice.
