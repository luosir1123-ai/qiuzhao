# Application Record Contract

Use one record per company and requisition. Merge duplicate notifications into its event history.

| Field | Meaning |
|---|---|
| `application_id` | Stable local identifier |
| `job_id`, `company`, `title` | Link to the target job |
| `status` | `planned`, `submitted`, `screening`, `assessment`, `interview`, `offer`, `rejected`, `withdrawn`, or `unknown` |
| `events` | Timestamp, status, source, and note |
| `next_action`, `due_at` | Concrete follow-up and deadline |
| `artifact_paths` | Local resume or preparation files; never credentials |

Only evidence changes status. An automated receipt supports `submitted`, not `screening` or `interview`. Preserve status history instead of overwriting it.

