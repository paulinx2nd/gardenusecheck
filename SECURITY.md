# Security

## Threat model

- Prompt injection inside public descriptions or evidence.
- A leader returning a well-formed but substantively false decision.
- Unauthorized wallets attempting role transitions.
- Replay, duplicate identifiers, duplicate votes, or repeated terminal actions.
- Oversized or malformed JSON and text.

## Controls

- Public data is explicitly delimited and described as data, never instructions.
- Validators independently rerun the substantive task and compare normalized decision fields.
- Bounded enums, counts, text lengths, identifier characters, arrays, and integer ranges fail closed.
- Role and state checks precede mutation.
- Canonical JSON and SHA-256 bindings make frozen inputs and ordered records auditable.
- The runner and Python dependencies are pinned.

## Residual risk

The contract does not inspect soil, plants, or disease records. It is an auditable coordination tool, not agronomic or safety advice.

Report vulnerabilities privately through the GitHub security advisory interface. Do not publish secrets in an issue.
