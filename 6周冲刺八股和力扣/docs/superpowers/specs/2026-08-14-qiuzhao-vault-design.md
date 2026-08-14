# 六周冲刺八股和力扣 Obsidian Vault Design

## Purpose

Create a public, GitHub-ready Obsidian Vault for a graduate student who is already applying for AI Agent and RAG application-development roles. The learner can recognize basic Python syntax but cannot yet write programs independently and can study six hours per day.

The system must build minimum interview readiness within seven days, then improve it through a six-week rolling program. Python coding, algorithms, computer-science fundamentals, Agent/RAG knowledge, project communication, and application review advance in parallel.

## Success Criteria

- The learner can open the repository directly as an Obsidian Vault.
- All core content remains readable as plain Markdown on GitHub.
- Every day has a concrete six-hour plan with observable outputs.
- The six-week curriculum includes Python, algorithms, fundamentals, Agent/RAG, projects, and interview practice.
- Reusable templates capture algorithm attempts, fundamentals, experiments, daily work, weekly reviews, and interviews.
- A dashboard shows current work and interview readiness without requiring a community plugin.
- The repository can record real applications and interview reviews. Credentials, authentication material, government identifiers, and secrets are never stored.

## Repository Structure

```text
6周冲刺八股和力扣/
├── README.md
├── 00-Dashboard/
├── 01-Python/
├── 02-Algorithms/
├── 03-CS-Fundamentals/
├── 04-Agent-RAG/
├── 05-Projects/
├── 06-Interview/
├── 07-Daily/
├── 08-Weekly/
├── 09-Resources/
├── Templates/
├── docs/superpowers/specs/
├── CONTRIBUTING.md
├── LICENSE
└── .gitignore
```

Directories `01` through `06` hold durable knowledge. Directories `07` and `08` hold chronological evidence. `00-Dashboard` presents navigation, current work, and readiness. Templates keep records consistent. The README explains the system to GitHub visitors.

Obsidian community plugins are optional. YAML properties, standard Markdown links, checkboxes, and relative links provide the baseline experience.

## Daily Operating Model

The default six-hour day is:

| Track | Minutes | Required output |
|---|---:|---|
| Python | 60 | One closed-book coding exercise |
| Algorithms | 90 | One new problem and one review problem |
| Fundamentals | 75 | One spoken answer set with follow-ups |
| Agent/RAG | 75 | One concept note or reproducible experiment |
| Project/interview | 30 | One recorded explanation or mock segment |
| Applications/review | 30 | Updated applications and next-day priorities |

The schedule may be split into three two-hour blocks. A daily note identifies three priority outcomes, actual work, errors, what can now be explained independently, and the first task for the next day.

## Six-Week Curriculum

### Week 1: Minimum interview readiness

- Python: variables, conditions, loops, functions, lists, dictionaries, sets, and strings.
- Algorithms: complexity, arrays, hash maps, binary search, and two pointers.
- Fundamentals: processes and threads, TCP and HTTP, indexes and transactions.
- Agent/RAG: LLM basics, embeddings, vector retrieval, and the basic RAG pipeline.
- Interview output: 60-second introduction, project architecture explanation, and first high-frequency Q&A set.

### Week 2: Independent basic coding

- Python: classes, exceptions, files, modules, and iterator basics.
- Algorithms: linked lists, stacks, queues, and sliding windows.
- Fundamentals: Python object model, GIL, network layers, and database locks.
- Agent/RAG: chunking, retrieval, Top-K, metadata filters, and citations.
- Interview output: second 45-minute mock interview and first error-review cycle.

### Week 3: Common solution frameworks

- Python: decorators, generators, context managers, and type hints.
- Algorithms: binary trees, DFS, BFS, and recursion.
- Fundamentals: memory management, coroutines, AsyncIO, and Redis.
- Agent/RAG: tool calling, structured output, workflows, and state.
- Interview output: independent end-to-end Agent/RAG request walkthrough.

### Week 4: Role-specific engineering

- Python: FastAPI, Pydantic, asynchronous endpoints, and pytest basics.
- Algorithms: backtracking, heaps, greedy algorithms, and dynamic-programming basics.
- Fundamentals: caching, queues, concurrency, rate limiting, timeouts, retries, and idempotency.
- Agent/RAG: hybrid retrieval, RRF, reranking, evaluation sets, and Recall@K.
- Interview output: project metrics, failure cases, and improvement plan.

### Week 5: Interview strengthening

- Algorithms: common dynamic-programming patterns, graph basics, and disjoint sets.
- Fundamentals: Docker, deployment, logging, monitoring, and elementary system design.
- Agent/RAG: MCP, authorization boundaries, prompt injection, and human approval.
- Practice: two timed coding sessions and two mock interviews.
- Interview output: project deep-dive question bank with adversarial follow-ups.

### Week 6: Consolidation

- Review algorithm errors and high-frequency problems.
- Reprioritize fundamentals against active job descriptions.
- Complete two 60-minute comprehensive mock interviews.
- Refine introduction, project explanation, and interviewer questions.
- Publish a stage report and refresh the repository README.

## Record Contracts

### Algorithm problem

Each record includes problem identity, topic, difficulty, first-attempt result, brute-force reasoning, optimized reasoning, code, complexity, boundary cases, error cause, mastery state, and next review date.

Mastery states are `new`, `learning`, `reviewing`, and `mastered`. A problem is mastered only when it can be coded independently under time pressure and explained aloud.

### Fundamentals note

Each note answers: one-sentence conclusion, mechanism, design reason, limitations, likely follow-ups, and connection to a real project.

### Agent/RAG experiment

Each experiment includes its question, hypothesis, data, environment, parameters, procedure, measured results, failures, conclusion, and next action. Unmeasured improvements are explicitly labeled as future work.

### Daily and weekly review

Daily notes record planned and actual minutes plus evidence links. Weekly reviews compare planned and completed work, reassess readiness, identify recurring errors, and set the next week's priorities.

## Interview Readiness

The dashboard scores five areas from 0 to 20: Python coding, algorithms, computer-science fundamentals, Agent/RAG, and project communication. Scores must cite evidence links rather than rely on confidence alone.

- 0-39: foundations in progress
- 40-59: interview participation is useful, with visible gaps
- 60-79: competitive for common interviews
- 80-100: company-specific strengthening

The score is diagnostic, not a promise of interview performance.

## Dynamic Replanning

- A scheduled coding test raises algorithms and ACM input/output practice to three hours per day.
- A scheduled interview assigns about 40% of study time to its job description and likely follow-ups.
- Every completed interview receives a review within 24 hours.
- Two consecutive incomplete days trigger scope reduction and review-first scheduling.
- After 30 minutes on an algorithm problem, the learner uses graduated hints. After reading a solution, the learner closes it and rewrites the answer.

## Publishing Boundary

The repository intentionally publishes real progress, applications, and interview learning where the learner chooses to record them. It must never contain passwords, cookies, API keys, access tokens, government identifiers, or other authentication material.

The repository uses an MIT license and a concise contribution guide. Commit messages describe learning evidence, such as `study: complete day 01` or `notes: add RAG retrieval`.

## Verification

Before delivery:

- Check all internal Markdown links and required files.
- Scan for placeholders and contradictory schedules.
- Confirm every curriculum day totals 360 minutes.
- Confirm templates render as valid Markdown and YAML.
- Confirm the repository contains no secret-like values.
- Inspect Git status and leave the generated baseline uncommitted until the learner chooses to publish it.
