# Deployment and refresh

## Notion

Use one page in your own skills registry, mark it as a Skill and select/reference that same page in the native Library. Compare the page identity from both entry points. No duplicate skill body is needed. Being marked a Skill does not itself convert the whole database to a native skills database or change sharing.

Use the live schema for title/description/version and task fields. Do not import another workspace's users, page IDs, relations, audit logs or checked state. Permission to use an export does not authorise workspace writes. Attach the refreshed ZIP at the bottom of the master and verify readback; a local ZIP alone does not update its attachment.

## Other AI tools

Adopt SINGLE-PROMPT.md explicitly in a project/system instruction area when supported, or paste it in one chat with destination/goal/context. Follow that platform's limits and priority rules. The template's Notion XML is data for writing Notion pages, not ordinary chat formatting: elsewhere use six ordinary Markdown sections. No account settings, tools or persistent preferences are installed automatically.

## Refresh contract

After approved content changes: edit sources, update the SKILL.md version when the contract changes, run `python3 export_bundle.py`, then `python3 export_bundle.py --check`. Share only after the check passes. Rebuilding is on demand and part of approved content edits by default, not unattended monitoring. downloaded ZIPs remain snapshots. The manifest intentionally excludes its own checksum and the ZIP to avoid self-reference; it hashes all payload files. The builder rejects unlisted bundle files and --check also verifies archive content.

For a complete live Notion export: reload the master, exclude only its self-referential export-delivery envelope, include all other body content and approved source fields, generate the single prompt and checksum manifest, rebuild, attach and read back. Keep that workspace export private. A public derivative must remove all private identifiers, logs and attachments. Record public source revision and private master version separately; public and private manifests must never be assumed identical.

## Verification checklist

- One-prompt file includes core skill, full bundled behaviour source and template.
- All six sections exist; Human red and AI purple in Notion only.
- First use offers five calibration choices and each session guided/concise support.
- One shared tracker; permission, acceptance and accuracy checks separate.
- Missing target, access and conflicting identities stop unsafe work.
- Editing a source causes --check to fail; rebuilding restores it.
- ZIP integrity and exact payload hashes pass.
- Public files contain no private workspace identifiers or evidence.
- Live-agent trial and human visual review remain separate acceptance gates.

## GitHub

Use a bounded branch and PR. Review before merge; no automatic Notion/GitHub reconciliation is installed or promised. Roll back by reverting the reviewed commit and restoring the previous export/version rather than erasing history.
