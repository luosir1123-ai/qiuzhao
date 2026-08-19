<div align="center">
  <img src="assets/qiuzhao-banner.svg" alt="qiuzhao - An open-source toolkit for Chinese campus recruiting" width="100%">
</div>

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-2da44e.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-tested%20on%203.11-3776ab.svg)](https://www.python.org/)
[![Repository checks](https://github.com/luosir1123-ai/qiuzhao/actions/workflows/validate.yml/badge.svg)](https://github.com/luosir1123-ai/qiuzhao/actions/workflows/validate.yml)
[![Skills](https://img.shields.io/badge/Codex-Skills-8250df.svg)](skills/)
[![Obsidian](https://img.shields.io/badge/Obsidian-Ready-7c3aed.svg)](6周冲刺八股和力扣/)

**Evidence-first tools and a six-week learning system for Chinese campus recruiting.**

[中文完整指南](README.zh-CN.md)

</div>

---

## What is qiuzhao?

`qiuzhao` is an open-source system for Chinese graduate and internship applications. It connects role discovery, evidence-based fit ranking, resume tailoring and audit, application tracking, interview preparation, honest open-source contribution, and structured study.

The repository has two primary entrances:

| Entrance | Use it when | Main outputs |
|---|---|---|
| [Job-search Skills](skills/) | You have job descriptions, a resume, or an application form | Ranked roles, tailored resume content, field mappings, interview packs |
| [Six-week interview sprint](6周冲刺八股和力扣/) | You are already applying but need stronger coding and fundamentals | 42 daily plans, LeetCode reviews, CS fundamentals, Agent/RAG study, mock interviews |

> [!IMPORTANT]
> qiuzhao does not invent experience or guarantee an offer. Claims must remain grounded in verifiable evidence. Login, CAPTCHA, declarations, and final submission always require the user's confirmation.

## Included Skills

| Skill | Purpose | Key output |
|---|---|---|
| `job-fit-ranker` | Apply hard eligibility gates and rank roles against resume evidence | Eligibility, fit score, evidence, gaps, official links |
| `jd-resume-tailor` | Tailor an existing resume to one target role without fabricating claims | Rewrites, keyword coverage, fact-check list |
| `resume-auditor` | Audit ownership, metrics, timelines, attribution, and evidence | Claim ledger, risky wording, corrected copy |
| `application-form-helper` | Map ATS fields and preserve the application event history | Field plan, conflicts, status, next action |
| `interview-prep` | Build JD-specific technical and behavioral preparation | Project deep dives, answer outlines, follow-ups, gap-repair plan |
| `oss-contributor` | Prepare a compliant contribution and preserve its actual state | Validated diff, confirmation gates, contribution record |

## Six-week interview sprint

The [Six-week interview sprint](6周冲刺八股和力扣/) is a GitHub-readable Obsidian Vault for candidates targeting AI Agent and RAG application-development roles. It assumes six hours of study per day and advances six tracks in parallel:

- Python programming
- LeetCode and live coding
- operating systems, networking, and databases
- Agent/RAG concepts and experiments
- project communication and mock interviews
- applications and daily review

Start with the [Dashboard](6周冲刺八股和力扣/00-Dashboard/学习总览.md), [Day 01](6周冲刺八股和力扣/07-Daily/2026-08-14-Day01.md), or the [42-day task cards](6周冲刺八股和力扣/08-Weekly/每日任务卡.md).

## Install

Install every Skill:

```bash
npx skills add luosir1123-ai/qiuzhao -g
```

Install one Skill:

```bash
npx skills add luosir1123-ai/qiuzhao --skill job-fit-ranker -g
```

Install from a local clone:

```bash
git clone https://github.com/luosir1123-ai/qiuzhao.git
cd qiuzhao
npx skills add . -g
```

To use the learning system, open `6周冲刺八股和力扣/` as an Obsidian Vault. Community plugins are optional; the core content uses standard Markdown and relative links.

## Workflow

```text
Official roles / JDs
        ↓
Eligibility and evidence-based fit ranking
        ↓
Resume tailoring → application-field consistency
        ↓
Interview preparation → gap repair → review
        ↖ honest OSS evidence and application history
```

The workflow keeps four categories separate:

- **Evidence**: facts supported by the resume, project artifacts, experiments, or official job descriptions.
- **Inference**: conclusions derived from evidence and labeled as such.
- **Gaps**: requirements with weak or missing evidence.
- **Unknowns**: information that was unavailable or still needs user confirmation.

## Principles

- Apply cohort, degree, major, language, and location hard gates before scoring.
- Never turn internships, projects, research, or campus activities into a different experience category.
- This repository does not require committing or uploading a real resume and provides no hosted backend. Data handling still depends on the runtime and tools you choose.
- Never bypass CAPTCHA, identity checks, declarations, or final-submit confirmation.
- Treat coding submissions as evidence only after closed-book reproduction and explanation.

## Development

```bash
python3 -m unittest discover -v
python3 scripts/validate.py
python3 scripts/check_private_data.py .
python3 "6周冲刺八股和力扣/scripts/validate_vault.py"
```

Examples must use fictional identities and `example.com` addresses. See [AGENTS.md](AGENTS.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE). See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for upstream inspirations and license notices.
