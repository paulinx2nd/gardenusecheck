# Originality

## Mechanism fingerprint

The decision is history-dependent and can be challenged by a different wallet before a seasonal event is committed.

Lifecycle: create plot -> evaluate proposal against history -> optional challenge -> owner commit -> close season into history.

Consensus boundary: Validators independently derive the proposal verdict and conditions; a separate consensus pass adjudicates challenge counter-evidence.

Settlement boundary: A non-blocked commit advances the plot season, while closure appends the crop family and observed outcome to the immutable history sequence.

## Review-cohort defense

Names, prompts, labels, and method names are not the basis of the distinction. The actor topology, stored state, allowed transitions, validator decision, and deterministic settlement described above are the reusable mechanism. A full-workspace structural scan is run before publication; its JSON report is retained outside the repository-wide source tree and summarized in `AUDIT.md` after the final pass.
