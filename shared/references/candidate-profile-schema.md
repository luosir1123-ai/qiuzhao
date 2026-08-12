# Candidate Profile Contract

Use this normalized profile across all Skills. Unknown values remain `unknown`; never invent them.

| Field | Type | Notes |
|---|---|---|
| target_roles | list | Preferred role families and keywords |
| education | list | School, degree, major, dates |
| experiences | list | Organization, title, dates, verified bullets |
| projects | list | Name, stack, evidence, verified metrics |
| skills | list | Tools and proficiency evidence |
| awards | list | Name, level, date |
| constraints | object | Location, graduation cohort, availability |
| source_map | object | Claim to resume section or user statement |

Sensitive contact data is optional and must stay local. Do not include it in generated examples or repository files.
