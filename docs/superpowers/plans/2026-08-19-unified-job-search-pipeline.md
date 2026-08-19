# Unified Job Search Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add evidence audit, application tracking, honest open-source contribution, and richer resume delivery to the existing qiuzhao workflow.

**Architecture:** Six independent skills exchange four shared Markdown contracts. Python standard-library validation enforces the claim ledger, while existing repository checks enforce packaging, links, and privacy.

**Tech Stack:** Markdown skill packages, YAML agent metadata, Python 3.11 standard library, unittest.

## Global Constraints

- Keep existing skill names compatible.
- Never invent or silently upgrade a claim's evidence status.
- Require explicit confirmation for final submissions and external repository writes.
- Keep examples fictional and use example.com addresses.
- Add no runtime dependency or hosted backend.

---

### Task 1: Shared evidence contracts and validator

**Files:**
- Create: `shared/references/claim-ledger-schema.md`
- Create: `shared/references/job-record-schema.md`
- Create: `shared/references/application-record-schema.md`
- Create: `scripts/validate_claim_ledger.py`
- Modify: `shared/references/candidate-profile-schema.md`
- Modify: `shared/references/output-contracts.md`
- Test: `tests/test_claim_ledger.py`

**Interfaces:**
- Consumes: JSON object containing `sources` and `claims`.
- Produces: `validate_claim_ledger(data: dict) -> list[str]`.

- [ ] Write tests for valid records, missing sources, invalid status, inconsistent ratios, and unsafe URLs.
- [ ] Run `python3 -m unittest tests.test_claim_ledger -v` and confirm missing-module failure.
- [ ] Implement the three contract documents and minimal standard-library validator.
- [ ] Re-run the focused test and confirm it passes.

### Task 2: Resume audit skill

**Files:**
- Create: `skills/resume-auditor/SKILL.md`
- Create: `skills/resume-auditor/agents/openai.yaml`
- Create: `skills/resume-auditor/references/audit-output.md`
- Modify: `skills/jd-resume-tailor/SKILL.md`

**Interfaces:**
- Consumes: candidate profile, claim ledger, resume, and optional public evidence.
- Produces: audit summary and updated claim ledger.

- [ ] Extend repository tests to require six expected skill packages.
- [ ] Run the focused validation test and confirm it fails while skills are absent.
- [ ] Add the audit skill and resume handoff instructions.
- [ ] Re-run the focused validation test and confirm it passes for this skill.

### Task 3: Application tracking and OSS contribution

**Files:**
- Create: `skills/oss-contributor/SKILL.md`
- Create: `skills/oss-contributor/agents/openai.yaml`
- Create: `skills/oss-contributor/references/contribution-record.md`
- Create: `templates/application-tracker.example.md`
- Modify: `skills/application-form-helper/SKILL.md`

**Interfaces:**
- Consumes: application events or a candidate-approved contribution target.
- Produces: application records or contribution evidence suitable for the claim ledger.

- [ ] Add expected-package and contract-link tests.
- [ ] Confirm the tests fail before adding the new files.
- [ ] Add state transitions, deduplication, confirmation boundaries, and contribution handoff.
- [ ] Re-run the tests.

### Task 4: Documentation, provenance, and release validation

**Files:**
- Create: `THIRD_PARTY_NOTICES.md`
- Modify: `README.zh-CN.md`
- Modify: `README.md`
- Modify: `CONTRIBUTING.md`

**Interfaces:**
- Consumes: completed six-skill structure.
- Produces: install, workflow, provenance, and contributor documentation.

- [ ] Update README assertions and install examples to list all six skills.
- [ ] Record both upstream MIT projects and adapted concepts.
- [ ] Run `python3 -m unittest discover -v`.
- [ ] Run `python3 scripts/validate.py`.
- [ ] Run `python3 scripts/check_private_data.py .`.
- [ ] Run `python3 "6周冲刺八股和力扣/scripts/validate_vault.py"`.

