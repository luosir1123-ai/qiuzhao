# GitHub Portfolio Refresh Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade the three remaining public repositories to the verified presentation standard of `qiuzhao` and rename `letouch-outreach-agent` to `waimao-outreach-agent` without changing application behavior.

**Architecture:** Treat each repository as an independent publication unit with its own domain-specific banner and documentation. Make repository-local changes, run that repository's checks, commit and push `main`, then update GitHub metadata; perform the outreach repository rename last so history and redirects are preserved.

**Tech Stack:** Git, GitHub CLI/API, Markdown, self-contained SVG, Python/pytest, Node.js/npm, existing repository validation tools.

## Global Constraints

- Work directly on each repository's `main` branch; do not create feature branches.
- Preserve implemented behavior, repository history, safety boundaries, and factual claims.
- Public product naming must not contain `letouch`; use `waimao` for the outreach product.
- Do not mechanically replace legal company names, historical facts, or third-party identifiers.
- Do not introduce screenshots, benchmarks, or capabilities that are not verified in the repository.
- Use relative GitHub links, fictional examples, and reserved domains such as `example.com`.
- Scan tracked text and SVG assets for local home paths, credentials, private contact details, and unintended internal endpoints.

---

### Task 1: Prepare Clean Local Checkouts

**Files:**
- Inspect: `local-translation-agent/**`
- Inspect: `letouch-outreach-agent/**`
- Inspect: `enterprise-nas-rag/**`

**Interfaces:**
- Consumes: GitHub repositories under `luosir1123-ai`.
- Produces: three clean local `main` checkouts with recorded baseline SHAs and verification commands.

- [ ] **Step 1: Clone or complete each checkout**

Run `git clone --depth 1 https://github.com/luosir1123-ai/<repo>.git <repo>` for missing repositories. If an interrupted checkout exists, remove only that incomplete checkout after confirming it has no worktree files, then clone again.

- [ ] **Step 2: Record repository state**

Run `git status --short --branch`, `git rev-parse HEAD`, `git remote -v`, and inspect `README*`, `AGENTS.md`, manifests, workflows, and recent commits in each repository.

- [ ] **Step 3: Discover exact checks and public naming**

Run `rg -n -i 'letouch|/Users/|README|pytest|ruff|mypy|npm (test|run)'` against tracked text while excluding build output. Record only commands supported by each manifest or repository guide.

- [ ] **Step 4: Run baseline checks**

Run the existing lightweight documentation and test commands available in each checkout. Record pre-existing failures and do not attribute them to documentation changes.

---

### Task 2: Refresh Local Translation Agent

**Files:**
- Modify: `local-translation-agent/README.md`
- Create: `local-translation-agent/README.zh-CN.md`
- Create: `local-translation-agent/assets/local-translation-agent-banner.svg`
- Modify only if present and necessary: `local-translation-agent/.github/workflows/*`

**Interfaces:**
- Consumes: supported formats, engines, cleanup behavior, auth modes, and commands verified from source and `pyproject.toml`.
- Produces: an accurate Chinese primary guide, English companion, and GitHub-renderable banner.

- [ ] **Step 1: Extract verified product facts**

Map each README claim to configuration, source, test, or existing documentation. Explicitly distinguish local Ollama processing from optional remote HTTP engines.

- [ ] **Step 2: Create the SVG banner**

Create a self-contained banner using document-page and translation-flow motifs, solid colors, accessible `<title>`/`<desc>`, no scripts, external resources, gradients, or embedded private data.

- [ ] **Step 3: Write the Chinese guide**

Cover positioning, supported formats, capability matrix, processing flow, deployment modes, quick start, configuration, quality checks, file lifecycle, privacy boundary, limitations, development checks, repository map, and license.

- [ ] **Step 4: Rewrite the English overview**

Use the same verified facts in a more concise English document. Link both languages at the top and use only valid relative links.

- [ ] **Step 5: Validate and commit**

Run `xmllint --noout assets/local-translation-agent-banner.svg`, Markdown-link checks available in the repository, `git diff --check`, privacy/name scans, and the repository's relevant pytest command. Commit as `docs: refresh project presentation` and push `main`.

---

### Task 3: Rebrand Waimao Outreach Agent

**Files:**
- Modify: `letouch-outreach-agent/README.md`
- Create: `letouch-outreach-agent/README.zh-CN.md`
- Create: `letouch-outreach-agent/assets/waimao-outreach-agent-banner.svg`
- Modify: product-facing tracked files returned by `git grep -n -i 'letouch'`
- Modify only when repository URLs are embedded: package metadata, Compose labels, docs, workflows, and examples.

**Interfaces:**
- Consumes: implemented account research, product recommendation, market comparison, presentation, approval, export, authentication, and retention behavior.
- Produces: `Waimao Outreach Agent` public identity with unchanged APIs and safety behavior.

- [ ] **Step 1: Classify every old-name occurrence**

For every tracked `letouch` occurrence, label it product branding, repository URL/path, historical/legal fact, third-party identifier, or fixture data. Replace only product branding and repository references.

- [ ] **Step 2: Add a naming regression check**

Extend the smallest existing validation test or script so public README titles, badges, install commands, and repository URLs cannot regress to `letouch-outreach-agent`. Verify the check fails before replacements and passes afterward.

- [ ] **Step 3: Apply the product-facing rename**

Use `waimao-outreach-agent` for repository/package/path references and `Waimao Outreach Agent` for display text. Preserve API routes, database identifiers, environment variables, and serialized contracts unless they are purely presentation labels and changing them is backward compatible.

- [ ] **Step 4: Create domain-specific documentation assets**

Create the SVG banner and dual-language README set covering customer research, evidence chain, product matching, comparison XLSX, editable presentations, human approval, no-send/no-CRM-write boundary, architecture, local demo, production boundary, checks, repository map, and limitations.

- [ ] **Step 5: Run targeted and repository checks**

Run the naming regression test, `xmllint`, Markdown-link checks, `git diff --check`, privacy scans, and the manifest-supported Python and Node checks relevant to changed files. Inspect the full staged rename diff before committing.

- [ ] **Step 6: Commit and push old repository URL**

Commit as `docs: rebrand project as waimao outreach agent` and push to `main` while the GitHub repository is still named `letouch-outreach-agent`.

---

### Task 4: Refresh Enterprise NAS RAG

**Files:**
- Modify: `enterprise-nas-rag/README.md`
- Create: `enterprise-nas-rag/README.zh-CN.md`
- Create: `enterprise-nas-rag/assets/enterprise-nas-rag-banner.svg`
- Modify only if necessary: documentation links or validation files.

**Interfaces:**
- Consumes: current synchronization, structured Excel retrieval, portal, evaluation, operations, and pilot-state evidence from source/tests/docs.
- Produces: documentation that clearly separates initial pilot assumptions from current implemented capability.

- [ ] **Step 1: Build a verified capability timeline**

Read current source, tests, operations docs, and project-stage notes. Resolve conflicts by preferring current executable behavior and explicitly date or label historical pilot constraints.

- [ ] **Step 2: Audit public infrastructure details**

Classify NAS addresses, share names, accounts, mount paths, and examples. Replace sensitive or accidental values with documentation placeholders while preserving intentionally public sample structure.

- [ ] **Step 3: Create banner and dual-language guides**

Cover NAS ingestion, idempotent incremental sync, Excel row retrieval, retrieval/evidence flow, portal, evaluation, operations, quick start, configuration, repository map, limitations, and security boundaries.

- [ ] **Step 4: Validate and commit**

Run `xmllint`, link and privacy checks, `git diff --check`, and the relevant pytest suite. Commit as `docs: refresh project presentation` and push `main`.

---

### Task 5: Publish GitHub Metadata And Rename

**Files:**
- No repository content changes expected.
- Modify local remote URL for the outreach checkout after GitHub rename.

**Interfaces:**
- Consumes: verified commits already present on all three remote `main` branches.
- Produces: final repository names, descriptions, topics, redirects, and synchronized local remotes.

- [ ] **Step 1: Update descriptions and topics**

Use `gh api -X PATCH repos/luosir1123-ai/<repo>` for concise domain-specific descriptions and `PUT /repos/{owner}/{repo}/topics` for verified topics such as `document-translation`, `pdf`, `rag`, `nas`, `foreign-trade`, `langgraph`, `fastapi`, and `react` as applicable.

- [ ] **Step 2: Rename the outreach repository**

Run `gh api -X PATCH repos/luosir1123-ai/letouch-outreach-agent -f name=waimao-outreach-agent` only after its new-name commit is confirmed on remote `main`.

- [ ] **Step 3: Update local remote and verify redirects**

Set origin to `https://github.com/luosir1123-ai/waimao-outreach-agent.git`, fetch, and confirm the old GitHub URL resolves to the new repository.

- [ ] **Step 4: Verify all remote publication surfaces**

For each repository, compare local `HEAD` with remote `main`, inspect API metadata, confirm README/banner paths, and check the latest GitHub Actions run where a workflow exists.

- [ ] **Step 5: Final cleanliness check**

Confirm all three worktrees are clean and synchronized, the public product naming scan has no unintended `letouch`, and no temporary preview artifacts were committed.
