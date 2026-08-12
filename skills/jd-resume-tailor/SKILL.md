---
name: jd-resume-tailor
description: Use when a user wants to tailor an existing resume to a specific job description, improve ATS keyword coverage, select the strongest evidence, or rewrite bullets without fabricating experience, metrics, employment, or skills.
---

# JD Resume Tailor

Produce a role-specific resume while preserving factual integrity and the user's requested format or page limit.

## Inputs

Require the target JD and current resume/profile. Read the shared [candidate contract](../../shared/references/candidate-profile-schema.md), [scoring contract](../../shared/references/fit-scoring.md), and [output contract](../../shared/references/output-contracts.md).

## Workflow

1. Extract hard requirements, core duties, preferred skills, domain signals, and repeated keywords from the JD.
2. Build a claim ledger mapping each candidate claim to its source. Mark ambiguous claims for confirmation.
3. Choose evidence by relevance and strength. Keep internship, employment, project, research, and campus experience in their original categories.
4. Rewrite bullets with action, architecture or method, scale, result, and business context where evidence exists.
5. Add missing JD terminology only when it accurately names demonstrated work. Never create experience to satisfy a keyword.
6. Respect the page limit by removing low-relevance detail before shrinking readability.
7. Return the tailored copy, coverage assessment, omitted material, and verification questions.

## Writing Rules

- Prefer specific systems and measured results over self-evaluation.
- Use the JD's language naturally; avoid keyword stuffing.
- Distinguish implemented results from targets, plans, and prototypes.
- Preserve dates, employers, degrees, award levels, and metric denominators exactly.
- Use [tailoring-output.md](references/tailoring-output.md) for the handoff.
