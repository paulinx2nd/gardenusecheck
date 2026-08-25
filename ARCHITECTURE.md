# Architecture

## Boundary

- Frontend or backend: wallet UX, indexing, private drafts, non-authoritative previews, notifications, and optional off-chain source retrieval.
- GenLayer contract: Validators independently derive the proposal verdict and conditions; a separate consensus pass adjudicates challenge counter-evidence. A non-blocked commit advances the plot season, while closure appends the crop family and observed outcome to the immutable history sequence.
- External world: No external data collection occurs. Plot context, policy, plan, challenge, and outcome are public caller-attested snapshots.

## Event path

create plot -> evaluate proposal against history -> optional challenge -> owner commit -> close season into history

## Actors

- plot owner
- independent challenger
- GenLayer validators

## Consensus design

The leader produces a normalized bounded result. Each validator independently reruns the substantive task from the same frozen public inputs. Validators compare the decision fields that change state, not merely JSON shape. Invalid model output raises `[LLM_ERROR]` so a broken leader is not accepted.

## Deterministic layer

A non-blocked commit advances the plot season, while closure appends the crop family and observed outcome to the immutable history sequence. Identifiers, bounds, access checks, ordering, counters, masks, hashes, and terminal-state guards are computed deterministically.

## Persistence

State uses GenLayer storage types only. Public composite records are serialized as canonical JSON where appropriate. Source SHA-256 at evidence generation: `049e0e0492e8a3b58655ee5d3ccfa716052741915f3e193a8534c8e5f42c7163`.
