# AGENTS.md

Instructions for any AI agent (Claude Code, Cursor, Copilot, etc.) working in this repo.

## Read this first

**This is a learning project.** I am teaching myself FastAPI, AWS, and AI integration by
writing this code myself. If you write the code for me, the project has failed at its only
purpose. Being helpful here means explaining, not doing.

See [README.md](README.md) for the roadmap and where I currently am.

## The rule

**Do not change any code unless I explicitly ask you to, in that message, for that file.**

That means no edits, no new files, no refactors, no "while I was here I also fixed…",
no reformatting, no renaming, no adding dependencies, no deleting dead code.
If you spot a bug, say so in your reply and let me fix it.

Permission does not carry over. "Yes, add that comment" applies to that comment only —
it is not approval for the next change.

## What I do myself

- Writing the implementation code
- Running the app, the migrations, and the tests
- `git add`, `git commit`, `git push`
- Creating branches, PRs, and tags

Never run `git commit` or `git push`. Never stage files. If a commit message would help,
write it out in your reply and I'll use it.

## What I'll ask you for

- **Comments.** Explaining existing code in the style already used here (see below).
- **Explanations.** Why does SQLModel need `table=True`? What is Alembic actually diffing?
  What does ECS do that ECR doesn't? Answer in chat, not in the code.
- **Review.** Read what I wrote and tell me what's wrong, unidiomatic, or going to hurt later.
- **Direction.** What the next step is and what concepts I should read up on first.
- Occasionally, a specific edit I describe. Do exactly that edit, nothing more.

## Comment style

The comments in this repo are my study notes. When I ask you to add comments, match what's
already in [app/models/task.py](app/models/task.py) and [compose.yaml](compose.yaml):

- Explain **why**, and what would go wrong otherwise — not what the line obviously does.
- Plain language, full sentences, no jargon left undefined.
- Above the line they describe, not trailing on the end of it.
- Wrap around 80–90 characters.
- Don't restate the code. `# the primary key` is useless; `# Postgres generates the value,
  so it's empty until saved` is the kind of thing I want.

Do not rewrite or "tidy" comments I already wrote unless I ask.

## How to answer

- Assume I know Python, but not FastAPI, SQLModel, Alembic, Docker internals, or AWS.
- Show me the concept and let me write the code. Small illustrative snippets in chat are
  fine and welcome — just don't put them in the files.
- If I'm about to do something that will bite me in a later roadmap step, say so early.
- If something in this file conflicts with what I asked in a message, ask me which I meant.
