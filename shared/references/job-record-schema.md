# Job Record Contract

Store one record per company and requisition.

| Field | Meaning |
|---|---|
| `job_id` | Stable local identifier |
| `company`, `title`, `location` | Official listing values |
| `source_url`, `checked_at` | Source and observation time |
| `hard_gates` | Requirement, candidate evidence, and pass/fail/unknown state |
| `fit_evidence`, `gaps`, `unknowns` | Evidence-based match explanation |
| `score`, `recommendation` | Ranking aid, never an admission probability |

If a role disappears or changes, preserve the earlier observation and add a new check timestamp.

