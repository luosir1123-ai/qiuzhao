# Candidate Profile Contract

Use this normalized profile across all Skills. Unknown values remain `unknown`; never invent them.

| Field | Type | Notes |
|---|---|---|
| target_roles | list | Preferred role families and keywords |
| education | list | School, degree, major, dates |
| experiences | list | Stable ID, organization, title, dates, verified bullets |
| projects | list | Stable ID, name, stack, evidence, verified metrics |
| skills | list | Tools and proficiency evidence |
| awards | list | Name, level, date |
| constraints | object | Location, graduation cohort, availability |
| source_map | object | Claim to resume section or user statement |

Every resume-ready statement should point to the shared [claim ledger](claim-ledger-schema.md). Keep a claim's ownership scope narrower than or equal to the evidence that supports it.

Sensitive contact data is optional and must stay local. Do not include it in generated examples or repository files.
