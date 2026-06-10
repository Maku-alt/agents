# Agents Repo

Repositorio transversal para agentes reutilizables de Codex.

## Principios

- `core/` contiene contratos y convenciones compartidas.
- `domains/` contiene agentes por dominio.
- `domains/decks/` es el primer dominio y resuelve la creacion de presentaciones.
- Cada agente debe producir artefactos claros, reutilizables y revisables.
- El repo es la fuente de verdad; luego se copia al runtime o a otros repos segun necesidad.

## Estructura

```text
agents/
  core/
  domains/
    decks/
      orchestrator/
      narrative/
      visual/
      design/
      review/
      ppt-builder/
  schemas/
  templates/
  scripts/
```

## Flujo del dominio decks

`brief -> orchestrator -> narrative -> visual/design -> review -> ppt-builder`

## Reglas del dominio decks

- Los agentes deben hacer preguntas cuando falte contexto critico.
- Las preguntas deben ser minimas y orientadas a destrabar la siguiente salida.
- Cada agente recibe inputs estructurados y devuelve outputs estructurados.
- Ningun agente debe saltarse el contrato de salida.
