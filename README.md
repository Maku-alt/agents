# Agents Repo

Repositorio transversal para agentes reutilizables de Codex.

## Principios

- `domains/` contiene agentes por dominio.
- `domains/decks/` es el primer dominio y resuelve la creacion de presentaciones.
- `domains/sql/` resuelve trabajo analitico SQL/Teradata organizado por casos.
- `domains/research/` resuelve investigaciones con evidencia externa, sintesis critica y recomendaciones.
- Cada agente debe producir artefactos claros, reutilizables y revisables.
- El repo es la fuente de verdad; luego se copia al runtime o a otros repos segun necesidad.

## Estructura

```text
agents/
  domains/
    decks/
      orchestrator/
      narrative/
      design/
      review/
      ppt-builder/
    sql/
      orchestrator/
      sql-analyst/
      sql-reviewer/
      documenter/
    research/
      researcher/
  schemas/
  templates/
```

## Flujo del dominio decks

`brief -> orchestrator -> narrative -> design -> review -> ppt-builder`

## Reglas del dominio decks

- Los agentes deben hacer preguntas cuando falte contexto critico.
- Las preguntas deben ser minimas y orientadas a destrabar la siguiente salida.
- Cada agente recibe inputs estructurados y devuelve outputs estructurados.
- Ningun agente debe saltarse el contrato de salida.
- Los artefactos JSON se validan con JSON Schema.
- Los artefactos Markdown respetan las secciones definidas en `schemas/decks/markdown-contracts.md`.

## Portabilidad

Para reutilizar este dominio en otro repo:

1. Copia `domains/decks/`.
2. Copia `schemas/decks/` y `schemas/decks-artifacts.md`.
3. Copia `templates/decks/`.
4. Conserva la misma estructura relativa para no romper referencias.

Minimo utilizable en otro repo:

- `domains/decks/orchestrator/agent.md`
- `domains/decks/narrative/agent.md`
- `domains/decks/design/agent.md`
- `domains/decks/review/agent.md`
- `domains/decks/ppt-builder/agent.md`
- `schemas/decks/`
- `templates/decks/`

Minimo utilizable del dominio SQL:

- `domains/sql/orchestrator/agent.md`
- `domains/sql/sql-analyst/agent.md`
- `domains/sql/sql-reviewer/agent.md`
- `domains/sql/documenter/agent.md`
- `domains/sql/README.md`
- `templates/sql/`

Minimo utilizable del dominio Research:

- `domains/research/researcher/agent.md`
- `domains/research/README.md`
