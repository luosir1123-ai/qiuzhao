# qiuzhao Repository Rebrand Design

## Goal

Rename the GitHub repository from `qiuzhao-skills` to `qiuzhao` and present it as a complete, evidence-first campus recruiting system rather than a loose collection of skills. Rename the Obsidian learning module from `qiuzhao/` to `6周冲刺八股和力扣/` so its purpose is immediately clear.

## Repository Identity

- GitHub repository: `luosir1123-ai/qiuzhao`
- Display name: `qiuzhao`
- Chinese description: `面向中文校招与实习的一站式开源求职系统，覆盖岗位匹配、简历定制、网申辅助、面试准备，以及六周 Python、力扣、计算机八股与 Agent/RAG 冲刺计划。`
- Default branch remains `main`; no feature branch is created.
- Existing repository history, issues, stars, releases, and settings are preserved through GitHub's repository rename operation.

## Repository Structure

```text
qiuzhao/
├── skills/                     # Installable job-search skills
├── shared/                     # Evidence and output contracts
├── templates/                  # Fictional candidate examples
├── 6周冲刺八股和力扣/          # Obsidian and GitHub learning vault
├── README.zh-CN.md             # Detailed primary guide
└── README.md                   # Concise English guide
```

The learning Vault remains isolated from installable Skills. Its internal Markdown links stay relative so the Chinese directory name does not break GitHub or Obsidian navigation.

## Chinese README

The Chinese README is the detailed primary introduction. It uses GitHub-supported Markdown and restrained inline HTML only where centering improves the first viewport.

### First viewport

1. Centered `qiuzhao` wordmark and a concise Chinese value proposition.
2. Shields.io badges for license, Python, Codex Skills, Obsidian compatibility, and repository checks. Badges must report real repository facts only.
3. Compact anchor navigation: quick start, capability map, six-week sprint, principles, contribution.
4. No fabricated adoption statistics, testimonials, interview pass rates, or company logos.

### Information sequence

1. **What qiuzhao is**: audience, problem, and evidence-first position.
2. **Job-search loop**: discover roles → assess fit → tailor resume → assist application → prepare and review interviews.
3. **Two primary entrances**:
   - installable Skills;
   - `6周冲刺八股和力扣` learning Vault.
4. **Skills table**: purpose, inputs, outputs, and safety boundary for all four skills.
5. **Six-week sprint**: daily six-hour allocation, weekly objectives, 42-day evidence outputs, and direct links to Dashboard, Day 01, task cards, and templates.
6. **Quick start**: installation commands using `luosir1123-ai/qiuzhao`, local clone instructions, and Obsidian opening instructions.
7. **Example workflow**: realistic sequence from official JD to interview review using fictional data only.
8. **Repository map**: explain directories without overwhelming the reader.
9. **Principles and limitations**: evidence, hard eligibility, privacy, human confirmation, website variability, and no hiring guarantee.
10. **Development and contribution**: exact validation commands and contribution rules.

## English README

The English README mirrors the repository identity, current install commands, two primary entrances, safety principles, and links to the detailed Chinese guide. It stays shorter than the Chinese README but must not retain any `qiuzhao-skills` URLs or commands.

## Learning Vault Rename

- Rename root directory `qiuzhao/` to `6周冲刺八股和力扣/` with `git mv` so Git records the change as a move.
- Change the Vault README display title from `qiuzhao` to `六周冲刺：八股与力扣`.
- Update the Vault design and implementation documents so they describe the new module name rather than the repository name.
- Preserve all 42 schedule days, templates, Obsidian settings, and validators.

## Link And Command Migration

Replace every repository reference:

- `luosir1123-ai/qiuzhao-skills` → `luosir1123-ai/qiuzhao`
- `github.com/luosir1123-ai/qiuzhao-skills` → `github.com/luosir1123-ai/qiuzhao`
- local clone directory `qiuzhao-skills` → `qiuzhao`

The migration applies to READMEs, setup instructions, specs, plans, tests, examples, and skill installation commands. Historical Git commit messages are not rewritten.

## Visual Rules

- Use a dark, solid-color first-viewport banner rendered with GitHub-compatible HTML; do not use gradients.
- Use a small number of functional badges and colored section accents.
- Use tables for exact mappings and weekly comparisons, not decorative card grids.
- Keep paragraphs short, headings descriptive, and navigation visible near the top.
- Ensure the README remains useful when images or external badge services are unavailable.
- Do not add generated logos, company marks, decorative blobs, or unverifiable social proof.

## GitHub Metadata

After content is pushed successfully:

1. Rename the repository through the GitHub API.
2. Set the detailed Chinese description defined above.
3. Preserve `main` as the default branch.
4. Add relevant topics: `campus-recruiting`, `job-search`, `resume`, `interview`, `leetcode`, `obsidian`, `codex-skills`, and `chinese`.
5. Update the local `origin` URL to `https://github.com/luosir1123-ai/qiuzhao.git`.

## Verification

Before pushing content:

- Run `python3 -m unittest discover -v`.
- Run `python3 scripts/validate.py`.
- Run `python3 scripts/check_private_data.py .`.
- Run the learning Vault validator from its renamed directory.
- Run `git diff --check`.
- Search tracked files for `qiuzhao-skills` and old `qiuzhao/` module references.
- Verify all Markdown links and install commands use the future repository name.

After the GitHub rename:

- Read the repository metadata back from GitHub.
- Confirm `main` and the pushed commit are unchanged.
- Confirm `6周冲刺八股和力扣/README.md` is present.
- Confirm old GitHub repository URLs redirect to the renamed repository.
