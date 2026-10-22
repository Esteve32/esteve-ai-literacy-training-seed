# My AI, my voice, one useful email

A portable, connection-free action-learning prototype. Version 0.1.0, 22 October 2026. Fresh-agent, participant and Microsoft work-Copilot trials are **pending**.

## For a learner — no coding required
1. Get the single journey ZIP from your facilitator or the GitHub Actions build artifact. Extract it using your computer's normal Extract/Unzip action.
2. Open a new chat in your organisation's approved AI. Upload **START-HERE.txt** and send the activation message from **ACTIVATE.txt**. If uploads are blocked, open START-HERE.txt in a text editor and paste its complete contents into chat.
3. Follow one short question at a time. You may type, dictate, answer in your own words, challenge the AI, skip or stop.

A ZIP does not auto-run. Microsoft currently lists TXT and MD uploads, not ZIP; extraction is the default Copilot route. An upload alone is not adoption. No installation, account connection, browser extension or administrator access is required. Your AI may still need an online service and a permitted account.

## What you will do
Check the environment → choose observation/privacy → try a small task → calibrate the AI's manner and your draft voice → steer a revision → check evidence → compose a new skill → carry a handover to another chat.

Use synthetic material throughout. A suggested 15–25 minute duration is a planning estimate, not an attention measurement or time limit. Pause freely. There is no ability score.

## For a facilitator
Read facilitator/GUIDE.md privately. Keep blank notes in your organisation's approved private location; never commit completed notes, participant profiles or chats. Ask separately for observation, note-taking, screen sharing and any recording. No hidden monitoring or automatic collection is installed. The journey works as unobserved self-study too.

Keep facilitator notes and MAINTAINER files out of the learner's AI context. If your AI can inspect a ZIP, explicitly adopt START-HERE.txt only, not every instruction file. The simplest route is always to upload START-HERE.txt alone.

## For a maintainer
From the repository root:
```sh
python3 bundles/learning-journey/build.py
python3 bundles/learning-journey/build.py --check
python3 -m unittest discover -s bundles/learning-journey/tests -v
```
The builder uses only Python's standard library. It rebuilds the ten public seed exports in an isolated temporary copy and includes their complete ZIP contents under LIBRARY/, plus the current repo behaviour source. It does not change the existing packs. Learners do not run these commands.

The new GitHub workflow runs build/check/tests on relevant pushes and pull requests and uploads a ZIP artifact; it does not auto-merge, publish releases or connect to Notion/Drive. It must be on the default branch and Actions must be enabled for the default distribution path. CI success remains unverified until a real run is inspected.

## Sources, freshness and rights
The learning shell adapts DB11 11.19 interaction choices, 11.43 style calibration and the current repository teaching/evidence principles. Source review hashes are in source-review.json; private originals, URLs, identities and raw examples are excluded. The source 11.43 was marked internal-only: this is a bounded generic adaptation authorised for prototyping, not a verbatim export, licence grant or onward-release approval. Do not infer rights from technical availability.

The approved public repository collection is carried with this journey, not every private DB11 record. GitHub CI ensures a rebuild from the checked-out source snapshot, not live DB11 freshness. Online source refresh is a separate, supervised maintainer skill in maintainer/UPGRADE-SKILL.md. Existing downloads and Drive copies never update themselves. See FRESHNESS.md and RIGHTS.md.

Product guidance checked 22 October 2026: https://support.microsoft.com/en-gb/topic/file-upload-in-microsoft-copilot-8b7bf432-9576-4b16-9dee-6c19a4169e62 . Exact product/tenant behaviour still requires a real trial.
