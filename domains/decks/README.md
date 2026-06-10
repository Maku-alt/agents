# Decks Domain

Dominio para crear presentaciones ejecutivas de punta a punta.

## Objetivo

Transformar un brief de negocio en un deck listo para editar o presentar, con narrativa, direccion visual, sistema de diseno, revision de calidad y construccion del `.pptx`.

## Agentes

- `orchestrator/`: dirige el flujo, hace intake y activa especialistas.
- `narrative/`: construye storyline y contenido slide by slide.
- `visual/`: define metaforas visuales, prompts y uso de recursos graficos.
- `design/`: define tema visual, layouts, paleta y reglas de estilo.
- `review/`: detecta huecos de mensaje, consistencia y problemas de calidad.
- `ppt-builder/`: convierte especificaciones en un deck real.

## Artefactos canonicos

- `brief.json`
- `storyline.md`
- `slide-outline.json`
- `visual-brief.md`
- `image-prompts.json`
- `theme-spec.json`
- `design-rules.md`
- `review-report.md`
- `fix-list.json`
- `deck-build-plan.json`

## Flujo recomendado

1. `orchestrator` valida el brief y hace preguntas de intake.
2. `narrative` produce storyline y outline de slides.
3. `visual` y `design` trabajan sobre el outline aprobado.
4. `review` evalua narrativa, visual y diseno.
5. `ppt-builder` arma el deck con los artefactos aprobados.
