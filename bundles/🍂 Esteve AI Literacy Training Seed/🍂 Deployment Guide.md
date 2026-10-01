# 🍂 Deployment Guide

Use this guide to install the seed in an AI tool with agent features.

## Before you start

This bundle contains Markdown instructions. Some tools use uploaded files as reference material but do not automatically follow them. For the strongest effect, put the text from **🍂 Agent Instructions.md** into the tool's main instructions or system prompt area.

## General installation path

1. Open **🍂 Agent Instructions.md**.
2. Copy all of its text.
3. Open your AI tool's settings, agent builder, notebook settings, or project instructions.
4. Find a field called something like **Instructions**, **System prompt**, **Agent rules**, **Behavior**, or **Custom instructions**.
5. Paste the text and save.
6. If the tool supports files, also upload this bundle so the README and deployment notes stay available.
7. Start a new chat or run: **“Read the Esteve AI Literacy Training Seed instructions and run the first-time setup workshop.”**
8. Answer the five questions with letters, short phrases, or **“recommended defaults.”**
9. Ask the agent to summarize your choices. Correct anything it misunderstood.
10. Try a small task and check whether the agent explains its reasoning, marks uncertainty, and respectfully checks your thinking.

## ChatGPT

Add the instruction text to the available custom instruction or project instruction area. If you use a Project, add the file or paste the instructions into that Project's settings so they apply to that work. Account-level memory and custom instructions are separate from this Markdown bundle; this file does not change them automatically.

## Copilot and local coding agents

For a coding project, merge the instructions into the project's `AGENTS.md` or the instruction file used by that agent. If the project already has an instruction file, read it first and combine rules carefully. Keep project-specific build steps and safety rules.

A common layout is:

```text
my-project/
├── AGENTS.md
├── src/
└── README.md
```

Do not replace an existing `AGENTS.md` without checking it. Keep passwords, keys, tokens, and private personal details out of shared files.

## Gemini, Gems, notebooks, and other agent tools

Look for an instruction field in the Gem, notebook, workspace, or agent setup. Paste the main instructions there. If the tool only accepts uploaded documents, upload the bundle and explicitly tell the agent to read **🍂 Agent Instructions.md** and run the five-question setup.

If there is a character limit, use the short version below. Keep the full file as the reference copy.

## Short version for small instruction fields

> Use clear eighth-grade English. Be visual when that helps. Teach through action: do a useful task, explain the key idea, and say what we learned. Show a short rationale for important suggestions. Separate facts, inferences, and unknowns. Do not invent facts or claim actions succeeded without checking. Avoid automatic agreement: respectfully check my reasoning and flag meaningful errors, weak evidence, conflicts, or risks. When useful, use workshop mode with decision-sized steps, tick boxes, simple answers, and clear reasons. Ask five short setup questions the first time: tone, learning/work modes, traffic lights, uncertainty handling, and how directly to challenge my thinking. Explain code and commands in plain English and give copy-ready code in code blocks. Keep me in control of important choices. Remind me that I can update these instructions.

## Team calibration

Each person can choose different settings. Have them answer the five setup questions rather than sharing personal account memory. For team use, agree on shared defaults, then let each person adjust tone and challenge level.

## Update and iterate

1. Edit **🍂 Agent Instructions.md** when a setting should change for everyone using the bundle.
2. Edit the README or this guide if the first-use path changes.
3. Upload or paste the updated instructions into the AI tool again.
4. Test one real task and note what worked or failed.
5. Keep a dated copy if you need to compare versions.

The seed is a living template. Improve it as people learn what helps them work and learn well.
