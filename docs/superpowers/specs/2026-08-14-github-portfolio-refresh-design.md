# GitHub Portfolio Refresh Design

## Goal

Bring the owner's three remaining public repositories up to the presentation standard established by `qiuzhao`, while preserving each project's actual capabilities and technical identity. Public project naming must not use `letouch`; the foreign-trade project will use `waimao` instead.

## Scope

| Current repository | Final repository | Positioning |
|---|---|---|
| `local-translation-agent` | unchanged | Local-first document translation with layout preservation and Office/PDF coverage |
| `letouch-outreach-agent` | `waimao-outreach-agent` | Evidence-backed foreign-trade customer development, product recommendation, comparison, and presentation workflows |
| `enterprise-nas-rag` | unchanged | Enterprise NAS knowledge ingestion, structured retrieval, evaluation, and evidence traceability |

All work goes directly to each repository's `main` branch. Repository history must be preserved. The renamed repository's old GitHub URL should redirect to the new URL.

## Shared Presentation Standard

Each repository receives:

- a repository-owned, self-contained SVG banner with a distinct project-specific visual identity;
- a detailed Chinese primary guide and a concise English companion, linked from the top of each README;
- accurate status badges for license, tested runtime, checks, and core platform only when verified by repository configuration;
- a clear project definition, problem statement, capability matrix, architecture or data-flow diagram, quick start, configuration boundary, repository map, verification commands, limitations, privacy notes, and license section;
- a detailed GitHub description and relevant topic tags;
- relative links that work on GitHub and do not depend on local paths.

The three banners share restrained typography, compact badges, and the same information hierarchy, but use different accent colors and domain imagery. They must not look like copies with only the title changed.

## Repository-Specific Direction

### Local Translation Agent

- Visual language: document pages, translation flow, and layout-preservation cues.
- Lead with supported formats, local/remote engine boundary, cleanup lifecycle, and format-quality checks.
- Do not claim that data always stays local when remote translation engines are configured.

### Waimao Outreach Agent

- Rename the repository and visible product title from `letouch-outreach-agent` / `LeTouch Outreach Agent` to `waimao-outreach-agent` / `Waimao Outreach Agent`.
- Replace internal documentation links, commands, examples, package-facing labels, and public textual branding where they refer to the product. Do not rewrite historical business facts or third-party identifiers unless they are product branding.
- Visual language: account research, product evidence, comparison tables, outreach drafts, and editable customer presentations.
- State prominently that exports require human review and that the application does not send email or write to CRM automatically.

### Enterprise NAS RAG

- Visual language: NAS sources, incremental synchronization, retrieval layers, evaluation, and citations.
- Separate the original NAS pilot assumptions from currently implemented platform capabilities.
- Treat infrastructure addresses, credentials, internal share names, and deployment details carefully; preserve only values intentionally suitable for a public example.

## Naming And Privacy Rules

- Public repository names, README titles, badges, and install commands must not contain `letouch`; use `waimao` for the outreach product.
- Scan tracked text and SVG assets for local home-directory paths, credentials, private contact details, and unintended internal endpoints before publishing.
- Do not mechanically replace legal company names, resume facts, third-party service names, or historical references without checking their meaning.
- Use fictional examples and reserved domains such as `example.com`.

## Change Boundaries

This refresh may edit documentation, repository metadata, validation scripts/tests, and product-facing names required by the outreach rename. It must not redesign application behavior, change APIs without necessity, or invent screenshots, benchmarks, deployment support, or completed features.

## Verification And Publication

For each repository:

1. Discover and run its existing tests, linters, type checks, build checks, and documentation validators in proportion to the changes.
2. Validate SVG XML, local Markdown links, renamed paths, and the absence of stale product URLs.
3. Review the complete staged snapshot before committing.
4. Push the verified commit to `main`.
5. Update GitHub description and topics; rename the outreach repository only after its new-name content is on `main`.
6. Confirm the remote default branch SHA, rendered README assets, workflow status, new URL, and old-URL redirect.

## Success Criteria

- All three repository homepages have detailed, domain-specific, visually consistent documentation.
- `letouch` is absent from public project naming; the outreach repository is named `waimao-outreach-agent`.
- Existing project facts and safety boundaries remain accurate.
- Repository checks pass locally and on GitHub where workflows exist.
- No unrelated application refactor or user data is introduced.
