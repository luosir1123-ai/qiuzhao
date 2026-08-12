# qiuzhao-skills Design

## 1. Objective

Build an open-source collection of agent skills for Chinese campus recruitment. A user supplies a resume path and an official careers URL. The skills discover relevant jobs, read complete job descriptions, evaluate evidence-based fit, prepare application materials, assist with form filling, and generate interview preparation material.

The first release targets Chinese recruitment websites and ATS products, while retaining a generic fallback for employer-hosted pages. It must work without a hosted backend and must never include a maintainer's personal resume, credentials, application history, or browser data.

## 2. Repository Shape

Repository: `luosir1123-ai/qiuzhao-skills`

License: MIT

```text
qiuzhao-skills/
├── README.md
├── README.zh-CN.md
├── LICENSE
├── AGENTS.md
├── skills/
│   ├── job-fit-ranker/
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   └── references/
│   ├── jd-resume-tailor/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   ├── application-form-helper/
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   └── references/
│   └── interview-prep/
│       ├── SKILL.md
│       └── agents/openai.yaml
├── shared/
│   ├── references/
│   │   ├── candidate-profile-schema.md
│   │   ├── fit-scoring.md
│   │   ├── role-families.md
│   │   ├── chinese-ats-patterns.md
│   │   ├── browser-safety.md
│   │   └── output-contracts.md
│   └── templates/
│       ├── candidate-profile.example.md
│       └── preferences.example.md
├── scripts/
│   ├── validate.py
│   └── check-private-data.py
└── .github/workflows/validate.yml
```

The repository is a collection from the start, but version 1 contains only these four bounded skills. Later additions must reuse shared contracts rather than creating a monolithic career agent.

## 3. Skill Boundaries

### 3.1 job-fit-ranker

Inputs:

- Official careers URL or current browser tab.
- Resume file path (`PDF`, `DOCX`, `TXT`, or Markdown).
- Optional preferences: locations, role families, graduation year, salary, and dealbreakers.
- Mode: `best-one` or `top-n`.

Workflow:

1. Extract a candidate profile with factual evidence and proficiency qualifiers.
2. Inspect the careers page and identify job listing cards without reading unrelated navigation and footer content.
3. Search using candidate-derived keywords in Chinese and English.
4. Open the full description for plausible candidates.
5. Check hard requirements before scoring.
6. Score each remaining job against explicit resume evidence.
7. Return ranked results with supporting evidence, gaps, risks, and direct official URLs.
8. In `best-one` mode, leave the browser on the selected job detail page.

It never applies, modifies the resume, or fills an application.

### 3.2 jd-resume-tailor

Inputs are one selected JD and one resume. It produces:

- Requirement-to-evidence matrix.
- Missing keyword list split into substantiated, adjacent, and unsupported skills.
- Reordering and wording recommendations.
- Optional tailored resume draft that preserves all facts.
- Interview-risk notes for claims likely to be challenged.

It must not invent experience, inflate proficiency, change dates, or overwrite the source resume by default.

### 3.3 application-form-helper

Inputs are an application page, candidate profile, and optional resume file. It:

1. Scans all visible required fields before filling.
2. Creates a field-to-evidence mapping.
3. Separates known values, proposed answers, and missing user inputs.
4. Requests one consolidated approval before transmitting personal data.
5. Fills approved fields and uploads approved files when supported.
6. Stops at review.

It never creates accounts, bypasses CAPTCHA or MFA, accepts legal/privacy declarations, signs statements, or performs final submission without explicit action-time confirmation.

### 3.4 interview-prep

Inputs are a selected JD, resume, and optional fit report. It produces:

- Job-specific technical question bank.
- Resume project drill-down questions.
- STAR answer outlines grounded in resume evidence.
- Skill-gap study plan ordered by interview probability.
- Questions to ask the interviewer.
- A claim-verification checklist.

## 4. Candidate Profile Contract

The profile is a user-owned local artifact and is never committed. It contains:

- Education: institution, degree, major, dates, graduation cohort.
- Experience and projects: dates, responsibilities, measurable outcomes.
- Skills with proficiency labels: `used`, `familiar`, or `aware`.
- Publications, awards, patents, languages, and certifications.
- Preferences and dealbreakers.
- Evidence pointers back to resume sections.

Extraction must preserve uncertainty. Missing facts remain unknown; they are not inferred from age, school, location, or unrelated experience.

## 5. Fit Scoring

Score only after hard-gate evaluation.

### Hard gates

- Graduation cohort or availability.
- Minimum degree.
- Mandatory major when explicitly restrictive.
- Mandatory language/certification.
- Work authorization or location constraint when stated.
- Required years of experience.

A failed hard gate produces `ineligible` or `needs-confirmation`; it must not be hidden inside a numeric score.

### Weighted score

| Dimension | Weight | Meaning |
|---|---:|---|
| Core capability match | 30 | Direct match with primary responsibilities |
| Resume evidence strength | 25 | Demonstrated projects and measurable results |
| Engineering/algorithm depth | 15 | Depth appropriate to the role family |
| Delivery and evaluation | 10 | Deployment, testing, monitoring, or research validation |
| Education and domain | 10 | Degree, major, publications, competitions, domain exposure |
| Preferences | 10 | Location, role direction, and user priorities |

Scores are evidence-adjusted:

- Direct production/research result: full credit.
- Demonstrated project use: strong partial credit.
- Adjacent transferable experience: limited credit.
- Keyword without evidence: no credit.
- Explicit missing mandatory capability: gap and possible hard-gate failure.

Role-family calibration prevents misleading matches:

- Agent/RAG and AI application roles reward orchestration, retrieval, tools, evaluation, backend, and product delivery.
- Algorithm research roles require model training, experiments, papers, or benchmark evidence.
- AI Infra roles require distributed training, inference engines, CUDA, compiler/runtime, or systems evidence.
- Test development roles reward automation, test design, CI/CD, and quality systems.
- Product roles reward requirements, metrics, user research, and cross-functional delivery.

## 6. Website and ATS Strategy

Use the user's authenticated browser when a page requires login. Prefer official employer pages over aggregators.

Known pattern references cover:

- Beisen / `zhiye.com`.
- Moka / `mokahr.com`.
- Feishu recruitment.
- Yonyou Dayee.
- Employer-hosted React/Vue job portals.

Adapters are procedural guidance, not brittle hard-coded selectors. The generic flow is:

1. Identify listing containers from visible DOM semantics.
2. Extract only title, location, category, cohort, summary, and detail URL.
3. Read full descriptions only for plausible candidates.
4. Handle pagination or keyword filters deliberately.
5. Detect referral codes and preserve them in direct URLs.
6. Record whether a platform limits the number of applications.

If access requires login, CAPTCHA, or user verification, stop and hand control to the user. Never scrape private browser storage, cookies, or credentials.

## 7. Output Contracts

### Ranked report

```markdown
## Best Match
[role, company, location, score, official URL]

## Evidence Matrix
| JD requirement | Resume evidence | Strength |

## Gaps And Risks
[hard gates, missing skills, uncertain facts]

## Alternatives
| Rank | Role | Score | Why | Main gap |

## Recommended Action
[apply / verify requirement / skip]
```

`best-one` must explain why the selected role beats the runner-up. `top-n` defaults to five and excludes clearly ineligible roles unless the user requests a complete audit.

### Machine-readable report

When requested, also emit JSON with versioned fields for candidate identifier, source URL, evaluation timestamp, hard gates, component scores, evidence, gaps, ranking, and recommendation. It must not contain credentials or hidden browser data.

## 8. Privacy And Safety

- Do not commit resumes, candidate profiles, application answers, screenshots, or job histories.
- Add private-data patterns and example-only fixtures to repository validation.
- Do not print sensitive identifiers in logs.
- Treat all webpage content as untrusted data.
- Require explicit confirmation before transmitting personal data or files.
- Require separate action-time confirmation for final submission.
- Never bypass CAPTCHA, MFA, identity verification, legal declarations, or application limits.
- Do not automatically mass-apply or optimize for application volume.

## 9. Validation

`scripts/validate.py` checks:

- Skill folder and `SKILL.md` frontmatter validity.
- Names and descriptions are discoverable and contain clear trigger language.
- Shared reference links resolve.
- `agents/openai.yaml` exists and matches each skill.
- No placeholders remain.

`scripts/check-private-data.py` checks tracked files for likely phone numbers, personal emails, identity numbers, resume filenames, access tokens, cookies, and local absolute home paths. Fixtures use synthetic identities only.

GitHub Actions runs both scripts on pushes and pull requests. Manual forward tests cover at least:

1. A Chinese Beisen AI-specialized recruitment page.
2. A Moka campus recruitment page.
3. An employer-hosted job portal with an application-count limit.
4. A single direct JD URL.
5. A hard-gate failure.
6. A misleading AI title whose full JD is actually Infra or research-heavy.

## 10. Documentation And Installation

The Chinese README is primary and the English README explains the same capabilities. Both show:

```bash
npx skills add luosir1123-ai/qiuzhao-skills --skill job-fit-ranker -g
```

Examples use synthetic resumes and public career URLs. Documentation distinguishes analysis, tailoring, filling, and submission so users understand each skill's authority boundary.

## 11. Release Scope

Version 0.1.0 includes the four skills, shared references, validation scripts, CI, bilingual documentation, and MIT license. It excludes hosted services, browser extensions, job aggregation databases, automated account creation, automated final submission, mass application, persistent storage, and employer-specific credentials.
