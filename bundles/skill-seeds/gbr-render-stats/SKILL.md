---
name: gbr-render-stats
description: Render already-decoded Green/Blue/Red tagged text without changing its wording, count characters deterministically and compare to a human-chosen reference mix. Use for GBR rendering or statistics, not for reclassifying the message.
version: "0.1.0-prototype"
status: prototype-needs-human-review
---

# Render and count GBR-tagged text

Read COMMON.md and the bundled AI Literacy behaviour source. In a generated single-prompt export both are included. Apply them to the bounded task, not to unrelated accounts or settings.

## Inputs

Obtain well-formed tagged text, desired output (full render / excerpt / stats only / review only), local destination and an explicit reference ratio. Offer the source's 75/20/5 as an optional training comparator, never a validated ideal or pass/fail judgement.

## Procedure and counting contract

Use counts.py for deterministic counts. Accept g/b/r colour elements and optional L1–L8 wrappers; wrappers do not validate lens meanings. Exclude all tags; include spaces and punctuation inside colour elements. Count Unicode code points, not bytes or grapheme clusters; disclose this explicit prototype convention. Colour nesting is forbidden because it would double-count. Reject malformed markup, unknown attributes/tags, non-whitespace untagged text and an empty coloured denominator. Do not silently repair the text. XML entities decode to their visible character, and external whitespace is excluded.

The script emits counts, percentages and signed percentage-point differences. Require three finite non-negative comparator values totalling 100. Counts do not measure communication quality or people. Preserve actual text in the rendered message. In Notion convert colour tags to green/blue/red spans; elsewhere use labelled segments so colour is not the only meaning cue. Literal g/b/r tags are interchange data, not ordinary HTML or Markdown styling instructions. Do not reinterpret classification unless separately asked.

## Output and approval

Show a key, unchanged rendered text, count/%/reference/delta table, counting convention, brief limits and one copy-ready block. Optional charts require an available supported chart tool and accessible labels; omit them honestly if unavailable. For stats-only do not rewrite. Preview the exact destination and local audit trail; wait for approval to write, then read back. Never substitute a new standalone destination without permission.
