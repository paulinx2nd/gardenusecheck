# Source Provenance

## Collection behavior

No external data collection occurs. Plot context, policy, plan, challenge, and outcome are public caller-attested snapshots.

The contract performs no live web request, does not scrape a page, and does not silently claim that a label or URL authenticates its publisher. This avoids validator drift from changing pages. If an application needs live retrieval, that retrieval belongs in a separately reviewed mechanism whose validators independently fetch and normalize the same source.

## Integrity bindings

- Contract source SHA-256: `049e0e0492e8a3b58655ee5d3ccfa716052741915f3e193a8534c8e5f42c7163`
- ABI SHA-256: `cd1717c029bc72c4aa97fbe72cfb8edfd0731a7976228e6dc380795157713893`
- Frozen text and canonical JSON records are hashed inside the contract where the workflow needs a content binding.
- Human-readable source references, when present, are expressly marked unverified.

## Fixture policy

Tests use synthetic public fixtures written for this repository. They are not copied production records and do not represent real people.
