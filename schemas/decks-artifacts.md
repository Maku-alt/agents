# Decks Artifact Contracts

This document is the human-readable index for deck artifacts.
JSON Schema files in `schemas/decks/` are the machine-readable source of truth for JSON artifacts.
Markdown structure is defined in `schemas/decks/markdown-contracts.md`.

## Contract Lifecycle

- `draft`: incomplete artifact allowed during progressive intake.
- `enriched`: usable by a specialist, with some open decisions.
- `ready`: required decision fields are complete for the next gated step.

Do not emit optional fields with empty values only to satisfy a shape.

## JSON Artifacts

### `brief.json`

Schema: `schemas/decks/brief.schema.json`

Minimum draft:

```json
{
  "brief_status": "draft",
  "language": "es",
  "source_materials": [],
  "constraints": [],
  "references": []
}
```

Ready brief:

```json
{
  "brief_status": "ready",
  "project_name": "Example deck",
  "objective": "Support an executive decision",
  "audience": "Leadership team",
  "decision_required": "Approve the recommended path",
  "deadline": "2026-06-30",
  "language": "es",
  "slide_count_target": 10,
  "brand_context": "Use the corporate brand as a constraint",
  "source_materials": [],
  "constraints": [],
  "references": []
}
```

### `slide-outline.json`

Schema: `schemas/decks/slide-outline.schema.json`

```json
[
  {
    "slide_number": 1,
    "slide_kicker": "Decision",
    "slide_title": "The recommended path concentrates value in two actions",
    "slide_takeaway": "Prioritize the two actions with the strongest evidence.",
    "purpose": "Frame the executive decision.",
    "key_points": ["Action one", "Action two"],
    "evidence_type": "recommendation",
    "recommended_chart_or_visual": "Two-column comparison"
  }
]
```

`speaker_notes_optional` may be added when notes provide real presentation value.

### `theme-spec.json`

Schema: `schemas/decks/theme-spec.schema.json`

```json
{
  "theme_name": "Bold Signal",
  "tone": "Executive and assertive",
  "style_family": "Editorial business",
  "palette": {
    "primary": "#101820",
    "secondary": "#334155",
    "accent": "#F04E30",
    "background": "#F7F5F0",
    "surface": "#FFFFFF",
    "text": "#101820",
    "muted_text": "#667085",
    "success_or_positive": "#138A72",
    "risk_or_tension": "#C63C32"
  },
  "typography": {
    "title": "Aptos Display",
    "body": "Aptos",
    "labels": "Aptos",
    "numeric": "Aptos Display"
  },
  "layout_system": "Asymmetric editorial grid",
  "signature_elements": ["Accent rule", "Large conclusion titles"],
  "title_style": "Left aligned, conclusion-led",
  "chart_style": "Muted context with one accent series",
  "table_style": "Light separators with emphasized decision rows",
  "image_treatment": "Editorial crops with intentional negative space"
}
```

### Other JSON Artifacts

- `workflow-state.json` -> `schemas/decks/workflow-state.schema.json`
- `agent-routing.json` -> `schemas/decks/agent-routing.schema.json`
- `image-prompts.json` -> `schemas/decks/image-prompts.schema.json`
- `fix-list.json` -> `schemas/decks/fix-list.schema.json`
- `deck-build-plan.json` -> `schemas/decks/deck-build-plan.schema.json`

## Markdown Artifacts

The required headings and fields for these artifacts are defined in `schemas/decks/markdown-contracts.md`:

- `storyline.md`
- `style-preview-set.md`
- `design-rules.md`
- `visual-brief.md`
- `closing-slide-brief.md`
- `review-report.md`
- `style-preset-catalog.md`
