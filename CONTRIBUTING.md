# Contributing

Keep contributions narrowly scoped and evidence-based. Examples must be fictional and must not contain resumes, personal contact details, credentials, application screenshots, or local home paths.

Before opening a pull request, run:

```bash
python3 -m unittest discover -v
python3 scripts/validate.py
python3 scripts/check_private_data.py .
python3 "6周冲刺八股和力扣/scripts/validate_vault.py"
bash tests/install-smoke.sh
```

New Skills need a `SKILL.md` with `name` and `description` frontmatter plus `agents/openai.yaml`. Relative Markdown references must resolve.

When adapting substantial material from another project, record its source and license in `THIRD_PARTY_NOTICES.md` and retain any required copyright notice.
