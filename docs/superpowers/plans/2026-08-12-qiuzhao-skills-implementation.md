# qiuzhao-skills Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish an installable, privacy-safe collection of four open-source Skills for evidence-based matching and preparation on Chinese campus recruitment websites.

**Architecture:** Four independent `skills/*/SKILL.md` workflows share candidate, scoring, ATS, safety, and output contracts from `shared/references`. Small Python validators enforce repository shape and prevent personal data from entering Git history; GitHub Actions runs them on every change.

**Tech Stack:** Markdown Skills, YAML agent metadata, Python 3 standard library, GitHub Actions, `npx skills` installer.

## Global Constraints

- Repository name is `qiuzhao-skills` and license is MIT.
- Never commit resumes, candidate profiles, application answers, screenshots, histories, credentials, or local absolute paths.
- Never bypass CAPTCHA, MFA, identity verification, application limits, legal declarations, or final-submit confirmation.
- Do not depend on a hosted backend, proprietary CLI, or employer credentials.
- Chinese documentation is primary; English documentation covers the same public interface.
- All examples use synthetic identities and public careers URLs.

---

### Task 1: Repository Contracts And Validation

**Files:**
- Create: `LICENSE`, `AGENTS.md`, `.gitignore`
- Create: `shared/references/{candidate-profile-schema,fit-scoring,role-families,chinese-ats-patterns,browser-safety,output-contracts}.md`
- Create: `shared/templates/{candidate-profile.example,preferences.example}.md`
- Create: `scripts/{validate,check-private-data}.py`
- Create: `tests/test_validation.py`
- Create: `.github/workflows/validate.yml`

**Interfaces:**
- Produces `python3 scripts/validate.py` and `python3 scripts/check-private-data.py` with exit code `0` on success.
- Produces the shared reference paths consumed verbatim by all four Skills.

- [ ] Write `tests/test_validation.py` with temporary valid/invalid Skill trees and synthetic private-data fixtures.
- [ ] Run `python3 -m unittest tests.test_validation -v`; verify missing frontmatter and synthetic secrets fail.
- [ ] Implement standard-library validators for YAML-like frontmatter, required agent metadata, broken relative references, placeholders, and private-data patterns.
- [ ] Write shared contracts exactly matching the approved design, including hard-gate states `eligible`, `ineligible`, and `needs-confirmation`.
- [ ] Add MIT license, repository rules, ignore patterns, examples, and CI commands.
- [ ] Run unit tests and both validators; commit `feat: add shared contracts and repository validation`.

### Task 2: job-fit-ranker

**Files:**
- Create: `skills/job-fit-ranker/SKILL.md`
- Create: `skills/job-fit-ranker/agents/openai.yaml`
- Create: `skills/job-fit-ranker/references/workflow-examples.md`
- Create: `tests/fixtures/job-fit/{candidate,beisen-jobs,moka-jobs,limited-portal}.md`

**Interfaces:**
- Consumes the six shared references.
- Produces Markdown and optional JSON reports conforming to `shared/references/output-contracts.md`.
- Supports `best-one` and `top-n` modes.

- [ ] Add synthetic fixtures covering a direct Agent match, misleading AI Infra title, hard-gate failure, and single-application portal.
- [ ] Write the Skill workflow: resume extraction, bounded listing extraction, complete-JD reading, hard gates, evidence scoring, ranking, and browser handoff.
- [ ] Encode keyword expansion for Agent/RAG, AI application, algorithms, Infra, backend, test development, and product roles.
- [ ] Add examples for Beisen, Moka, and employer-hosted portals without fixed selectors or private data.
- [ ] Generate `agents/openai.yaml`, run repository validation, and manually verify the scoring arithmetic on fixtures.
- [ ] Commit `feat: add evidence-based job fit ranker`.

### Task 3: jd-resume-tailor

**Files:**
- Create: `skills/jd-resume-tailor/SKILL.md`
- Create: `skills/jd-resume-tailor/agents/openai.yaml`
- Create: `skills/jd-resume-tailor/references/factual-integrity.md`

**Interfaces:**
- Consumes one complete JD, one resume, and optionally a `job-fit-ranker` report.
- Produces requirement/evidence matrix, keyword gaps, ordering changes, wording changes, and optional non-destructive draft.

- [ ] Define substantiated, adjacent, and unsupported keyword categories with concrete synthetic examples.
- [ ] Write the workflow that preserves dates, metrics, proficiency, and source resume while exposing interview-risk claims.
- [ ] Add output examples for an Agent role and an AI Infra mismatch.
- [ ] Generate agent metadata, validate all links and private-data checks.
- [ ] Commit `feat: add factual JD resume tailoring skill`.

### Task 4: application-form-helper

**Files:**
- Create: `skills/application-form-helper/SKILL.md`
- Create: `skills/application-form-helper/agents/openai.yaml`
- Create: `skills/application-form-helper/references/{field-matching,ats-interactions}.md`

**Interfaces:**
- Consumes current application page, candidate profile, and approved file paths.
- Produces a redacted field plan and fills only after consolidated approval; stops at review.

- [ ] Specify scan-first field discovery and `known`, `proposed`, `missing`, `sensitive` classifications.
- [ ] Add Chinese/English fuzzy field mappings for identity, education, experience, projects, awards, languages, and standard questions.
- [ ] Document Beisen, Moka, Feishu, Dayee, and unknown-ATS interaction patterns with semantic locator fallback.
- [ ] Encode required confirmations for personal-data transmission, uploads, declarations, and final submission.
- [ ] Generate agent metadata, run validation, and commit `feat: add safe application form helper`.

### Task 5: interview-prep

**Files:**
- Create: `skills/interview-prep/SKILL.md`
- Create: `skills/interview-prep/agents/openai.yaml`
- Create: `skills/interview-prep/references/question-framework.md`

**Interfaces:**
- Consumes JD, resume, and optional fit report.
- Produces technical questions, project drills, STAR outlines, prioritized study plan, interviewer questions, and claim checklist.

- [ ] Define question generation by role family and evidence strength.
- [ ] Require every STAR outline and project answer to cite a resume fact; unsupported claims become preparation gaps.
- [ ] Add realistic synthetic Agent/RAG and algorithm-research examples.
- [ ] Generate agent metadata, validate, and commit `feat: add evidence-grounded interview preparation`.

### Task 6: Public Documentation And Installation QA

**Files:**
- Create: `README.zh-CN.md`, `README.md`
- Modify: `.github/workflows/validate.yml`
- Create: `tests/install-smoke.sh`

**Interfaces:**
- Documents per-Skill and all-Skills installation via `npx skills add`.
- `tests/install-smoke.sh` installs from a local repository copy into a temporary directory and verifies all four discoveries.

- [ ] Write Chinese and English capability tables, quick starts, example prompts, privacy model, limitations, and contribution instructions.
- [ ] Add local installation smoke test with cleanup handled by a temporary directory trap.
- [ ] Run unit tests, validators, and install smoke test from a clean clone.
- [ ] Confirm `rg` finds no personal data, local paths, placeholders, or generated caches.
- [ ] Commit `docs: add bilingual usage and installation guide`.

### Task 7: GitHub Publication

**Files:**
- Modify only release metadata if validation finds an issue.

**Interfaces:**
- Produces public repository `https://github.com/luosir1123-ai/qiuzhao-skills` on branch `main`.

- [ ] Verify GitHub CLI authentication without printing tokens; otherwise use the signed-in GitHub UI.
- [ ] Create the public MIT repository and set the local `origin`.
- [ ] Show the exact repository creation/push action and obtain action-time confirmation because publication is an external side effect.
- [ ] Push `main`, inspect GitHub Actions, and fix only verified failures.
- [ ] Test `npx skills add luosir1123-ai/qiuzhao-skills --skill job-fit-ranker -g` in an isolated temporary configuration.
- [ ] Tag `v0.1.0` after all checks pass and report the public installation commands.

## Self-Review

- Every design section maps to a task: four Skills (Tasks 2-5), shared scoring/ATS/safety/output contracts (Task 1), bilingual docs and installability (Task 6), publication (Task 7).
- Function and command names are consistent across tasks.
- No unspecified runtime dependency or hosted service is introduced.
- Publication and final application submission remain explicit-confirmation actions.
