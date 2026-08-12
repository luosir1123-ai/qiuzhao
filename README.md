# qiuzhao-skills

Open-source Skills for Chinese campus recruiting: discover official openings, rank job fit using resume evidence, tailor a resume, assist with application forms, and prepare for interviews.

[中文文档](README.zh-CN.md)

## Included Skills

| Skill | Purpose |
|---|---|
| `job-fit-ranker` | Extract and rank roles with hard eligibility gates and evidence |
| `jd-resume-tailor` | Tailor an existing resume without inventing claims |
| `application-form-helper` | Map resumes to Chinese ATS fields and stop before submission |
| `interview-prep` | Generate evidence-grounded interview drills and study priorities |

## Install

```bash
npx skills add luosir1123-ai/qiuzhao-skills -g
```

Install one Skill:

```bash
npx skills add luosir1123-ai/qiuzhao-skills --skill job-fit-ranker -g
```

## Principles

- Separate evidence, inference, gaps, and unknowns.
- Apply cohort, degree, major, language, and location hard gates before scoring.
- Preserve internship, employment, project, research, and campus categories.
- Keep candidate data local; this repository has no hosted backend.
- Never bypass CAPTCHA, identity checks, declarations, or final-submit confirmation.

See the [Chinese guide](README.zh-CN.md) for the workflow, prompts, limitations, and contribution instructions.

## License

[MIT](LICENSE)
