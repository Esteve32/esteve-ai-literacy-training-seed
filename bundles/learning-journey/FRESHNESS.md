# Freshness contract

“Latest” has three different meanings. Always state which one you verified.

1. **Repository build freshness:** the generated prompt and ZIP match approved inputs in the checked-out commit. build.py --check verifies this mechanically. GitHub Actions builds a new artifact when relevant repository paths change, if the workflow is present/enabled.
2. **DB11 source freshness:** a maintainer with authorised Notion access reloads the selected source bodies, checks identity/lifecycle/rights and records capture time + content hash after a human-reviewed portable adaptation. This prototype reviewed 11.19 and 11.43 on 22 October 2026. It does not assert every DB11 skill is audited/current. No scheduled Notion polling, credentials, source export service or private DB11 dump is installed.
3. **Distribution freshness:** a person downloads and replaces the training ZIP in the approved Drive folder or training programme. A downloaded or Drive copy is a snapshot. It does not update itself or read private sources when opened.

The pack includes the existing ten approved public prototype seeds, generated from current repository source at build time, and a catalogue of them. “Included” is not “all skills active”, human verification or a rights grant. Source capture hashes are not inferred from a status field. The versioned manifest is the exact build receipt. Do not call it the latest DB11 library without a new, evidenced, scoped source review.

## Supervised refresh
Use maintainer/UPGRADE-SKILL.md. Discovery may inspect titles/descriptions across DB11 to find candidates; content export stays within a reviewed allowlist. New sources require a scope/privacy/rights decision and no silent copying of internal-only material. Keep private source-to-page mappings and sign-in hints outside this public repo and outside participant ZIPs. Verify the authenticated GitHub login is Esteve32 or obtain an explicit change decision. A sign-in email is not proof of the active GitHub identity; use the actual connection.

The workflow is build-on-change, not an automatic GitHub merge, live course updater or Drive upload. Automatic cross-service sync requires a separately scoped implementation, credentials kept in secret storage and tested permissions. Until then report source refresh or distribution replacement as pending, never silently stale-success.
