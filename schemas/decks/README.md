# Deck Schemas

JSON Schema files are the machine-readable contracts for structured deck artifacts.

## Validation Gates

- Intake may use `brief_status: draft` with incomplete context.
- Specialist work may begin with `brief_status: enriched` when the required context for that specialist exists.
- Build should require `brief_status: ready` plus valid narrative, design, review, and build artifacts.

## JSON Contracts

- `brief.schema.json`
- `workflow-state.schema.json`
- `agent-routing.schema.json`
- `slide-outline.schema.json`
- `theme-spec.schema.json`
- `image-prompts.schema.json`
- `fix-list.schema.json`
- `deck-build-plan.schema.json`

## Markdown Contracts

See `markdown-contracts.md`.

## Source Of Truth

- JSON artifacts: the corresponding `.schema.json` file.
- Markdown artifacts: `markdown-contracts.md`.
- Examples and starter files: `templates/decks/`.
