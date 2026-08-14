# qiuzhao Vault Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a GitHub-readable Obsidian Vault containing a six-week, six-hours-per-day interview-preparation system for an AI Agent/RAG applicant learning Python from near zero.

**Architecture:** Standard Markdown and YAML files form the durable data model. Dashboards link to weekly plans, daily notes, reusable knowledge records, and interview evidence without requiring community plugins. Small helper scripts validate links, YAML boundaries, schedule totals, and secret-like content.

**Tech Stack:** Markdown, YAML frontmatter, Obsidian core features, POSIX shell, Python 3 standard library, Git

## Global Constraints

- The learner is already applying and must reach minimum interview readiness within seven days.
- The default workload is exactly 360 planned minutes per day.
- Core content must remain readable on GitHub without Obsidian community plugins.
- Real progress and interview records may be public, but credentials, cookies, API keys, access tokens, and government identifiers must never be stored.
- Algorithm mastery uses exactly `new`, `learning`, `reviewing`, and `mastered`.
- Git commits and remote upload are deferred at the user's request.

---

### Task 1: Vault foundation and public entry points

**Files:**
- Create: `.obsidian/app.json`
- Create: `.obsidian/core-plugins.json`
- Create: `.gitignore`
- Create: `LICENSE`
- Create: `CONTRIBUTING.md`
- Create: `README.md`

**Interfaces:**
- Consumes: approved design in `docs/superpowers/specs/2026-08-14-qiuzhao-vault-design.md`
- Produces: a standalone Vault and GitHub landing page linking all major sections

- [ ] Create minimal Obsidian configuration using only core features.
- [ ] Add ignore rules for OS files, Obsidian workspace state, Python caches, environment files, and credentials.
- [ ] Add MIT license and a contribution guide describing evidence and content standards.
- [ ] Add README with audience, learning method, six-week overview, daily allocation, navigation, progress states, and usage instructions.
- [ ] Verify `README.md` contains links to the dashboard, curriculum, templates, and contribution guide.

### Task 2: Dashboard and curriculum

**Files:**
- Create: `00-Dashboard/学习总览.md`
- Create: `00-Dashboard/本周计划.md`
- Create: `00-Dashboard/面试就绪度.md`
- Create: `00-Dashboard/投递与面试看板.md`
- Create: `08-Weekly/六周总路线.md`
- Create: `08-Weekly/第1周-最低面试能力.md`
- Create: `08-Weekly/第2周-独立基础编码.md`
- Create: `08-Weekly/第3周-常见解题框架.md`
- Create: `08-Weekly/第4周-岗位专项工程.md`
- Create: `08-Weekly/第5周-面试强化.md`
- Create: `08-Weekly/第6周-查漏补缺.md`

**Interfaces:**
- Consumes: the daily allocation and curriculum topics from the approved design
- Produces: navigable weekly goals and evidence-based readiness scoring

- [ ] Write the dashboard with current priorities and links to Day 01 and Week 1.
- [ ] Define five readiness dimensions, scoring anchors, and evidence-link requirements.
- [ ] Write a six-week overview showing goals, topics, outputs, and exit checks.
- [ ] Write seven daily schedules for each week; every day must total 360 minutes.
- [ ] Include dynamic replanning rules for a coding test, scheduled interview, missed days, and post-interview review.
- [ ] Verify all 42 daily schedule totals equal 360.

### Task 3: Knowledge maps and starter content

**Files:**
- Create: `01-Python/Python学习路线.md`
- Create: `01-Python/Python基础速查.md`
- Create: `01-Python/Python面试题.md`
- Create: `02-Algorithms/算法路线图.md`
- Create: `02-Algorithms/错题本.md`
- Create: `02-Algorithms/模板总结/复杂度分析.md`
- Create: `03-CS-Fundamentals/计算机基础路线.md`
- Create: `03-CS-Fundamentals/操作系统.md`
- Create: `03-CS-Fundamentals/计算机网络.md`
- Create: `03-CS-Fundamentals/数据库.md`
- Create: `03-CS-Fundamentals/Linux与Git.md`
- Create: `04-Agent-RAG/Agent-RAG路线图.md`
- Create: `04-Agent-RAG/LLM基础.md`
- Create: `04-Agent-RAG/RAG.md`
- Create: `04-Agent-RAG/Agent与Tool-Calling.md`
- Create: `04-Agent-RAG/MCP.md`
- Create: `04-Agent-RAG/评估与可观测性.md`
- Create: `04-Agent-RAG/高频面试题.md`

**Interfaces:**
- Consumes: weekly curriculum topics
- Produces: concise knowledge maps that daily and weekly notes can link as evidence

- [ ] Write route maps with ordered topics and completion checkboxes.
- [ ] Add compact starter notes for Week 1 concepts, using conclusion, mechanism, limitation, follow-up, and project-connection fields.
- [ ] Add algorithm workflow, hint policy, review cadence, and mastery definitions.
- [ ] Add Agent/RAG interview questions covering pipeline, retrieval, evaluation, failure modes, latency, cost, and security.
- [ ] Verify every Week 1 topic links to an existing note or daily exercise.

### Task 4: Project and interview preparation

**Files:**
- Create: `05-Projects/项目总览.md`
- Create: `05-Projects/项目深挖模板.md`
- Create: `05-Projects/模拟追问.md`
- Create: `06-Interview/自我介绍.md`
- Create: `06-Interview/高频八股.md`
- Create: `06-Interview/反问面试官.md`
- Create: `06-Interview/模拟面试/第1次模拟面试.md`

**Interfaces:**
- Consumes: existing local AI Agent/RAG roadmap as contextual guidance, without importing unverifiable claims
- Produces: evidence-first project narratives and a first mock-interview script

- [ ] Create a project inventory that distinguishes verified facts from future work.
- [ ] Add architecture, trade-off, metrics, failure, ownership, and adversarial-follow-up prompts.
- [ ] Draft a fillable 60-second introduction without inventing personal experience.
- [ ] Create a Week 1 mock interview containing Python, algorithms, fundamentals, RAG, and project questions.
- [ ] Verify all personal or project-specific claims remain blank prompts until supplied by the learner.

### Task 5: Reusable templates and Day 01

**Files:**
- Create: `Templates/每日学习模板.md`
- Create: `Templates/LeetCode题目模板.md`
- Create: `Templates/八股知识点模板.md`
- Create: `Templates/项目实验模板.md`
- Create: `Templates/面试复盘模板.md`
- Create: `Templates/每周复盘模板.md`
- Create: `07-Daily/2026-08-14-Day01.md`
- Create: `09-Resources/学习资源.md`

**Interfaces:**
- Consumes: record contracts and Day 01 topics
- Produces: valid YAML records and an immediately executable first day

- [ ] Create templates with valid YAML, required fields, evidence links, and review prompts.
- [ ] Create Day 01 with three outcomes and six activities totaling 360 minutes.
- [ ] Include closed-book Python exercises, one algorithm problem, fundamentals prompts, a RAG task, and project narration.
- [ ] Add a curated resource list with one primary resource per learning purpose and rules for when to consult alternatives.
- [ ] Verify Day 01 can be followed without creating any additional planning document.

### Task 6: Automated verification and handoff

**Files:**
- Create: `scripts/validate_vault.py`
- Create: `scripts/check.sh`

**Interfaces:**
- Consumes: all Markdown and YAML files in the repository
- Produces: exit code 0 only when structural checks pass

- [ ] Implement a Python standard-library validator for required paths, local Markdown links, YAML delimiters, 42 schedule totals, forbidden placeholders, and common secret patterns.
- [ ] Add a shell entry point that runs the validator and `git diff --check`.
- [ ] Run `python3 scripts/validate_vault.py`; expect all checks to pass.
- [ ] Run `bash scripts/check.sh`; expect all checks to pass.
- [ ] Inspect `git status --short` and leave all changes uncommitted for later unified publication.
