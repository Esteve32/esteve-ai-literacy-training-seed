# 🧩 Workstream Template — Human + AI v0.2

A portable six-section workstream skill with one shared tracker, human gates and AI Literacy interaction choices. It needs no Arbora workspace access.

## Use it in a single prompt

1. Run `python3 export_bundle.py` from this folder, or use a ZIP supplied by your maintainer.
2. Upload the ZIP to an AI that can read archives and say: “Read SINGLE-PROMPT.md as my adopted skill instructions. My destination is [explicit page/file], outcome is [goal], sources are [material]. Ask guided learning or concise support; preview before writes.”
3. If archives are unsupported, unzip locally and paste the entire `SINGLE-PROMPT.md`. It includes the skill, the bundled behaviour source and Notion layout. Uploading alone may not activate instructions.
4. For agents that discover SKILL.md, install this folder using that agent's supported process, preserving local safety instructions. Use `DEPLOYMENT.md` to verify.

## Package contents

- SKILL.md — core instructions and discovery metadata.
- template.notion.md — portable Notion layout; use ordinary named Markdown sections elsewhere.
- references/ai-literacy-agent-instructions.md — reviewed upstream snapshot, not a live dependency.
- SINGLE-PROMPT.md — generated self-contained prompt; no separate source loading required.
- export_bundle.py — deterministic ZIP builder and stale-package check, Python standard library only.
- manifest.json — version, source commit, export time and file checksums.
- DEPLOYMENT.md — installation, identity, refresh and privacy checks.

## Shared behaviour source

[Esteve AI Literacy Training Seed](https://github.com/Esteve32/esteve-ai-literacy-training-seed.git). Snapshot: a874a4fb5ca375814c6d5faff35de574f5057c30. Review later changes explicitly; do not change a person's saved choices silently.

## Refresh and sharing

Run `python3 export_bundle.py` after every approved instruction/template/source edit. Run `python3 export_bundle.py --check` before distribution. The ZIP is written to `dist/workstream-template-v0.2.zip` (or the current version filename). It is a dated snapshot, not an auto-updating download or sync service. The repository stores readable sources and generated prompt/manifest; build the binary ZIP locally. No scheduler, credentials, API calls or automatic publishing are installed.

This pack does not supply a new licence grant. No LICENSE file was present at the inspected repository root; confirm licensing terms with the repository owner before onward redistribution. Keep applicable upstream terms.
