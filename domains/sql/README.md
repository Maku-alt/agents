# SQL Domain

Dominio transversal para trabajo analitico SQL/Teradata organizado por casos.

## Objetivo

Convertir requerimientos analiticos en flujos de trabajo claros para construir, revisar y documentar SQL reusable, con foco en grano correcto, trazabilidad, validaciones y convenciones del repo anfitrion.

## Roles

- `orchestrator/`: decide encaje del pedido, etapa, particion y siguiente agente.
- `sql-analyst/`: traduce la necesidad a SQL o bloques SQL con validaciones.
- `sql-reviewer/`: revisa riesgos tecnicos, grano, joins, duplicidad y performance basica.
- `documenter/`: convierte un caso maduro en documentacion breve y reusable.

## Flujo recomendado

1. `orchestrator` identifica el caso y la etapa.
2. `sql-analyst` construye o adapta SQL.
3. `sql-reviewer` revisa riesgos y controles.
4. `documenter` documenta la version madura.

## Contratos que espera del repo anfitrion

Este dominio funciona mejor si el repo donde se instale tiene:

- `AGENTS.md`
- `memory.md`
- una guia de convenciones SQL, por ejemplo `knowledge/sql-conventions.md`
- un arbol por caso, por ejemplo `desarrollo/cases/<case-id>/`
- `state.md` por caso
- `hypothesis.md` por caso cuando el caso aun esta abierto

Si el repo no usa exactamente esas rutas, debes adaptar las referencias de contexto en los prompts.

## Artefactos operativos recomendados

- `memory.md`
- `desarrollo/cases/<case-id>/state.md`
- `desarrollo/cases/<case-id>/hypothesis.md`
- SQL exploratorio
- SQL reusable
- documentacion final del caso

## Principios del dominio

- no mezclar casos por conveniencia;
- no cambiar el grano sin declararlo;
- separar construccion, revision y documentacion;
- explicitar supuestos y validaciones;
- preferir el menor cambio util sobre una reescritura total.
