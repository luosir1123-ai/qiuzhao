# qiuzhao Repository Rebrand Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rename the repository to `qiuzhao`, publish a detailed and polished bilingual introduction, and rename the learning Vault to `6周冲刺八股和力扣` without breaking links, Skills, or history.

**Architecture:** Content changes are completed and verified under the current repository name first. The learning Vault is moved with Git, README files and repository references are updated as one documentation change, then the content commit is pushed before the GitHub repository metadata is renamed. GitHub metadata and local origin are verified only after the rename succeeds.

**Tech Stack:** Git, GitHub API/CLI, Markdown, GitHub-compatible HTML, Shields.io badges, Python repository validators

## Global Constraints

- Work directly on `main`; do not create a feature branch.
- Preserve repository history and all existing Skills.
- Rename `qiuzhao/` to `6周冲刺八股和力扣/`.
- Use only real repository facts in badges and copy.
- Never commit personal data, credentials, or local user paths.
- Keep examples fictional and use `example.com` addresses.
- Preserve manual confirmation before final applications or high-risk actions.

---

### Task 1: Rename the learning Vault

**Files:**
- Move: `qiuzhao/` → `6周冲刺八股和力扣/`
- Modify: `6周冲刺八股和力扣/README.md`
- Modify: `6周冲刺八股和力扣/docs/superpowers/specs/2026-08-14-qiuzhao-vault-design.md`
- Modify: `6周冲刺八股和力扣/docs/superpowers/plans/2026-08-14-qiuzhao-vault-implementation.md`

**Interfaces:**
- Consumes: the verified 42-day Obsidian Vault
- Produces: a clearly named learning module whose relative links remain valid

- [ ] Move the directory with `git mv qiuzhao '6周冲刺八股和力扣'`.
- [ ] Change the module display title to `六周冲刺：八股与力扣` and describe it as a module of the larger `qiuzhao` repository.
- [ ] Replace the old module name in its design and implementation documents.
- [ ] Run `python3 '6周冲刺八股和力扣/scripts/validate_vault.py'`; expect 50 Markdown files and 42 schedule days.

### Task 2: Rebuild bilingual repository introductions

**Files:**
- Modify: `README.zh-CN.md`
- Modify: `README.md`
- Modify: `.gitignore`

**Interfaces:**
- Consumes: four installable Skills and the renamed learning module
- Produces: a detailed Chinese landing page and concise English landing page using the new repository identity

- [ ] Add `.superpowers/` to `.gitignore` so visual brainstorming artifacts cannot be committed.
- [ ] Replace the Chinese README with the approved brand header, real badges, anchor navigation, job-search loop, two primary entrances, Skills details, six-week curriculum, quick start, example workflow, repository map, principles, limitations, and contribution commands.
- [ ] Replace the English README with the new identity, updated install commands, two primary entrances, principles, and Chinese guide link.
- [ ] Ensure every GitHub URL and installation command uses `luosir1123-ai/qiuzhao`.
- [ ] Ensure the learning module links use the URL-encoded-safe Markdown path `6周冲刺八股和力扣/`.

### Task 3: Verify and publish content

**Files:**
- Modify as needed: tracked documentation containing `qiuzhao-skills`

**Interfaces:**
- Consumes: renamed module and rebuilt READMEs
- Produces: a tested content commit on the current `main`

- [ ] Search tracked files for `qiuzhao-skills` and update current commands, URLs, specs, and examples; do not rewrite Git history.
- [ ] Run `python3 -m unittest discover -v`; expect 5 passing tests.
- [ ] Run `python3 scripts/validate.py`; expect no findings.
- [ ] Run `python3 scripts/check_private_data.py .`; expect no findings.
- [ ] Run `git diff --check`; expect no whitespace errors.
- [ ] Commit the verified content as `docs: rebrand repository as qiuzhao`.
- [ ] Push `main` to the current remote before renaming the GitHub repository.

### Task 4: Rename and verify GitHub repository

**Files:**
- Modify local Git config: `origin` URL only
- Modify GitHub repository metadata: name, description, topics

**Interfaces:**
- Consumes: pushed rebrand commit
- Produces: public repository `https://github.com/luosir1123-ai/qiuzhao`

- [ ] Read remote `main` and confirm it equals the local rebrand commit.
- [ ] Rename the GitHub repository from `qiuzhao-skills` to `qiuzhao` through the GitHub API.
- [ ] Set the approved Chinese repository description and eight topics.
- [ ] Change local origin to `https://github.com/luosir1123-ai/qiuzhao.git`.
- [ ] Read back repository metadata, `main`, README, and `6周冲刺八股和力扣/README.md` from GitHub.
- [ ] Confirm the old repository URL redirects to the renamed repository.
- [ ] Run `git status --short --branch`; expect local `main` synchronized with `origin/main` and no tracked changes.
