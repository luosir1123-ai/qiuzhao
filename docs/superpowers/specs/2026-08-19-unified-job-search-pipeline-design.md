# Unified Job Search Pipeline Design

## Goal

Evolve `qiuzhao` from four isolated job-search skills into one evidence-driven pipeline that covers role discovery, resume tailoring and audit, application tracking, interview preparation, and honest open-source contribution.

## Architecture

Keep the repository installable as a collection of independent skills. The skills exchange Markdown records defined in `shared/references` rather than depending on a server, database, or orchestrator. Existing skill names remain stable; `resume-auditor` and `oss-contributor` are added as new entry points.

```text
candidate profile
  -> job-fit-ranker
  -> jd-resume-tailor -> resume-auditor
  -> application-form-helper -> interview-prep
  -> oss-contributor -> claim ledger -> resume-auditor
```

## Shared Contracts

- Candidate profile: durable facts, constraints, and source map.
- Claim ledger: atomic resume claims with source, verification status, scope, and metrics.
- Job record: official source, hard gates, match evidence, gaps, and recommendation.
- Application record: company, role, state, evidence, next action, and timestamps.

Unknown values remain unknown. Inferences are labeled. User-attested claims are not presented as independently verified. Metrics retain their numerator, denominator, baseline, result, and time window where available.

## Skill Boundaries

- `job-fit-ranker`: extracts roles and ranks them after hard-gate checks.
- `jd-resume-tailor`: selects grounded evidence, rewrites copy, and optionally produces editable HTML/PDF artifacts.
- `resume-auditor`: checks internal consistency and the support for role, ownership, timeline, and metric claims.
- `application-form-helper`: maps fields and maintains application state without final submission.
- `interview-prep`: derives likely questions and gap-repair work from the JD and audited claims.
- `oss-contributor`: prepares one honest contribution at a time; all external writes require explicit confirmation.

## Compatibility And Migration

The current four skill names and prompts stay valid. The richer contracts are additive. Existing candidate profiles can be upgraded by adding stable IDs and verification metadata when evidence is available. No user data is committed to the repository.

## Third-Party Provenance

The design is informed by `Hisn00w/ASu-skills` and `Claycui828/ASu-resume-skills`, both under MIT. `THIRD_PARTY_NOTICES.md` records repository URLs, authorship, licenses, and the capabilities adapted. No third-party branding is used as the default product identity.

## Safety

- Do not invent employers, projects, titles, ownership, metrics, or merged contribution status.
- Do not collect unrelated personal information for resume audits.
- Do not bypass authentication, CAPTCHA, declarations, or final submission.
- Do not fork, push, comment, or open a pull request without action-specific confirmation.
- Keep examples fictional and use `example.com` addresses.

## Verification

Repository validation checks all six skill packages, local links, shared contract presence, and privacy rules. A standard-library validator checks claim IDs, evidence states, source references, metric arithmetic, and unsafe URLs. Unit tests cover valid and invalid records.

