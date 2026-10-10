# 🌱 Portable skill seeds — prototype collection

Ten selectable seeds for learning how to work with AI: nine new public-safe adaptations plus the existing Workstream Template. These are prototypes, not production-certified skills or a complete export of proprietary/internal source material.

## Choose one

| Seed | Version | State |
| --- | --- | --- |
| [Jedi communication orchestration — reference scaffold](jedi-orchestration/SKILL.md) | 0.1.0-prototype | prototype-needs-human-review |
| [Render and count GBR-tagged text](gbr-render-stats/SKILL.md) | 0.1.0-prototype | prototype-needs-human-review |
| [Workstream Template — Human + AI](../workstream-template/SKILL.md) | 0.2 | existing-pack-needs-human-review |
| [Build a portable organisational knowledge kit](portable-knowledge-kit/SKILL.md) | 0.1.0-prototype | prototype-needs-human-review |
| [Create or refine a portable skill seed](create-skill-seed/SKILL.md) | 0.1.0-prototype | prototype-needs-human-review |
| [Apply a human-approved brand styling core](brand-styling-core/SKILL.md) | 0.1.0-prototype | prototype-needs-human-review |
| [Decode and rewrite a message consciously](email-decode-rewrite/SKILL.md) | 0.1.0-prototype | prototype-needs-human-review |
| [Set up a connected project with human gates](project-setup/SKILL.md) | 0.1.0-prototype | prototype-needs-human-review |
| [Harvest a meeting safely and resumably](meeting-debrief/SKILL.md) | 0.1.0-prototype | prototype-needs-human-review |
| [Turn one source into action learning](source-to-microlearning/SKILL.md) | 0.1.0-prototype | prototype-needs-human-review |

## Use in one prompt

From this folder run `python3 export_collection.py`, then `python3 export_collection.py --check`. Open `prompts/<seed-id>.md`: each generated prompt includes the selected seed, dependency instructions, relevant resources, shared human-gate contract and the pinned AI Literacy behaviour source. Paste the complete prompt into an AI, name your destination/goal/source, and explicitly adopt the instructions. If the tool reads archives, upload the generated collection ZIP and select that prompt. Uploading alone may not activate a skill or grant tool access.

The ZIP keeps `skill-seeds/` and the unchanged `workstream-template/` sibling so relative resources resolve. The repository stores readable source/prompts/manifests; the binary ZIP is built on demand in `dist/`. Refresh is included in approved content edits by default; downloaded archives do not auto-update.

## Safety and review

Read COMMON.md and PROVENANCE.md before use. Replace OPEN local mappings deliberately. Never copy another organisation's database/user IDs, signatures, task logs or agent settings. Full restricted Jedi references and the internal SEED archive are intentionally omitted; this catalogue does not imply they were exported. The brand is an explicit Arbora example, not a mandatory identity for adopters.

This collection depends on the unchanged workstream files in PR #1. The new PR is stacked onto `feat/workstream-template-v0-2`; after PR #1 merges, retarget this PR to main. Do not merge the stack accidentally as a substitute for review. No source Notion pages, production systems, account settings, licences or sync services are changed.

[Standalone AI Literacy behaviour repository](https://github.com/Esteve32/esteve-ai-literacy-training-seed.git). Behaviour snapshot pinned to a874a4fb5ca375814c6d5faff35de574f5057c30. Review later updates explicitly and preserve stronger local rules.

## Checks and acceptance

Run `python3 tests/test_tools.py` for executable synthetic checks, then the export builder/check. TESTS.md in each new seed describes behavioural scenarios; these have not been run with a fresh agent or accepted by a human. See VALIDATION.md for actual mechanical evidence. Review rights/licensing before wider release. No unattended monitoring, automatic registry sync or merge is installed.
