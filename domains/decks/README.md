# Decks Domain

Dominio para crear presentaciones ejecutivas de punta a punta.

## Objetivo

Transformar un brief de negocio en un deck listo para editar o presentar, con narrativa, direccion visual, sistema de diseno, revision de calidad y construccion del `.pptx`.

## Agentes

- `orchestrator/`: dirige el flujo, identifica fase y activa especialistas.
- `narrative/`: construye tesis, storyline y contenido slide by slide.
- `design/`: define previews de estilo, tema visual, metaforas graficas, prompts de imagen, layouts, paleta y reglas de estilo.
- `review/`: detecta huecos de mensaje, consistencia y problemas de calidad.
- `ppt-builder/`: convierte especificaciones en un deck real.

## Artefactos canonicos

- `brief.json`
- `storyline.md`
- `slide-outline.json`
- `visual-brief.md`
- `image-prompts.json`
- `style-preview-set.md`
- `theme-spec.json`
- `design-rules.md`
- `closing-slide-brief.md`
- `review-report.md`
- `fix-list.json`
- `deck-build-plan.json`

## Flujo recomendado

1. `orchestrator` clasifica la fase y hace preguntas de intake.
2. `narrative` produce tesis, storyline y outline de slides.
3. `design` produce 3 previews de direccion visual, define recursos visuales y fija el sistema elegido.
4. `review` evalua narrativa, visual y diseno.
5. `ppt-builder` arma el deck con los artefactos aprobados.

## Principios importados al dominio

- toda deck parte de una tesis, no de un tema suelto;
- los titulos de slides deben ser conclusiones, no encabezados genericos;
- cada slide debe tener lectura ejecutiva y prueba visible;
- la slide final debe cerrar con intencion editorial, no como resumen tecnico;
- la definicion de estilo debe hacerse con previews comparables, no solo con descripciones abstractas;
- el deck debe sentirse intencional y distintivo, no como una plantilla corporativa generica.
