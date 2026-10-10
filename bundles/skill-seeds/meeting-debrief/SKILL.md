---
name: meeting-debrief
description: Turn a permitted transcript or meeting note into a small-batch debrief with decisions, source-linked follow-ups, consent checks and a resume ledger. Use for Fathom or other meeting-ingest requests; separate harvest, task updates and notifications.
version: "0.1.0-prototype"
status: prototype-needs-human-review
---

# Harvest a meeting safely and resumably

Read COMMON.md and the bundled AI Literacy behaviour source. In a generated single-prompt export both are included. Apply them to the bounded task, not to unrelated accounts or settings.

## Inputs and first panel

Obtain permitted source transcript/note/link, meeting date/timezone, known participants, human notes, requested outputs, local page/task/audit/time mappings and reuse boundaries. Open with short options: Preview only / Harvest notes / Propose tasks / Review consent / Hold, plus free text. Capture optional priorities without treating them as permission to bypass approval.

## Three separate phases

1. Page harvest: summary, source link, decisions, completed work, proposed to-dos, risks and resume ledger; preview before writes.
2. Local task/audit/time updates: separate approved phase using live schema, parent/milestone scan and ownership checks. Transcript mentions are not automatically accepted actions.
3. Notifications/sharing: only separately approved; prefer an async advice bundle and consult affected people/experts before proposing another meeting.

Recording access does not prove consent or authorise wider ingest, training, publication or individual profiling. Keep consent Unknown when unverified. Internal notes are not automatically safe; check the authorised privacy scope. Exclude sensitive unnecessary details and never infer a legal basis or consent from a participant's silence.

## Small batches and resume

Use the source's small-chunk pattern: summary/source first, harvest next, table rows in 1–3 row batches, checklist/review state last. Create/update a ledger with source, destination, approval, current phase, last evidenced step, next unfinished step, failure point and recovery instruction. Update around meaningful approved writes; no ledger write before permission. Check stable IDs so resume does not repeat completed operations.

Before proposing tasks, search authorised local existing workstreams/activities/milestones and suggest a parent; flag absent milestone/ownership rather than invent one. Default to one task per approval unless batch mode is explicitly chosen. Propose title, source quote/timestamp, purpose, parent/milestone, R/A/C/I and a concrete checklist. Verify created bodies are non-empty before notifying; repairing a failed approved write must remain within its original scope. Hold if context is insufficient.

## Output

Return a concise source-grounded summary, decisions vs proposals, task/time suggestions, consent/risk status, changed-page audit (created/updated/skipped/pending), resume point, rollback note and next human decision. Record times only from verified duration/attendance, not assumed presence. Never infer Done/acceptance from a generated note. map/ledger resources are templates, not live syncs.
