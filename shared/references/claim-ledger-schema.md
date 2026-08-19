# Claim Ledger Contract

Use a claim ledger whenever resume copy, interview answers, or contribution records need to remain traceable.

## Sources

Each source has a stable `S-###` ID, type, title, optional URL, and access note. Allowed types are `official`, `repository`, `user_document`, `user_statement`, and `public_page`.

## Claims

Each atomic claim has:

| Field | Meaning |
|---|---|
| `id` | Stable `C-###` identifier |
| `text` | One independently testable statement |
| `status` | `source_grounded`, `user_attested`, `inferred`, `planned`, or `unknown` |
| `source_ids` | Sources that support the status |
| `scope` | Candidate-owned subsystem or responsibility boundary |
| `metric` | Optional complete ratio group (`numerator`, `denominator`, `displayed_percent`) or change group (`baseline`, `result`, `change_percent`), plus unit and time window |

Do not combine role, ownership, outcome, and causality in one claim when they require different evidence. `user_attested` means the user states it; it does not mean independently verified. `source_grounded` requires at least one referenced source other than `user_statement`.

Validate JSON ledgers with:

```bash
python3 scripts/validate_claim_ledger.py /path/to/claim-ledger.json
```
