# Agents Dictionary

Catalogo generado desde `agents/*/agent.toml` y `metadata.json`. No editar a mano.

| Agent | Status | Last reviewed | Role | Sandbox | Required skills | Tags | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `cross_functional_advisor` | `active` | `2026-08-02` | `worker` | `read-only` | — | `advisory`, `architecture`, `tradeoffs` | Analiza tradeoffs transversales complejos y recomienda una decision con evidencia y consecuencias. |
| `experience_designer_builder` | `active` | `2026-08-02` | `worker` | `workspace-write` | `impeccable` | `presentations`, `html`, `frontend`, `design`, `build` | Diseña y construye presentaciones HTML autocontenidas con Impeccable, incluyendo visuales, interaccion, renders y QA. |
| `experience_reviewer` | `active` | `2026-08-02` | `worker` | `read-only` | — | `presentations`, `review`, `qa`, `accessibility` | Revisa de forma independiente una presentacion HTML exacta, sus renders, runtime, accesibilidad y evidencia. |
| `narrative_strategist` | `active` | `2026-08-02` | `worker` | `workspace-write` | — | `presentations`, `narrative`, `storytelling` | Convierte tesis y evidencia aprobadas en un arco presentable, momentos claros y contrato de contenido. |
| `researcher` | `active` | `2026-08-02` | `worker` | `read-only` | — | `research`, `evidence`, `web` | Investiga preguntas abiertas con fuentes confiables, contradicciones explicitas y conclusiones calibradas. |

## Convenciones

- El hilo principal orquesta; las entradas del catalogo son workers.
- `impeccable` aplica a experiencias frontend/HTML, no a PowerPoint.
- Los agentes read-only revisan o asesoran; no corrigen artefactos.
- El hash permite detectar drift entre el repo y una copia instalada.
