# Decks Domain

Dominio para crear presentaciones ejecutivas de punta a punta.

## Objetivo

Transformar un brief de negocio en un deck listo para editar o presentar, con narrativa, direccion visual, sistema de diseno, revision de calidad y construccion real del `.pptx`.

La construccion PowerPoint usa la skill `pptx` como capa de ejecucion. Los agentes de este dominio no reemplazan esa skill: definen criterio, preservan decisiones aprobadas, enrutan trabajo y controlan gates.

## Agentes

- `orchestrator/`: dirige el flujo, identifica fase y activa especialistas.
- `narrative/`: construye tesis, storyline y contenido slide by slide.
- `design/`: define o preserva el sistema visual, incluyendo chart/table treatment e imagenes cuando aportan.
- `review/`: aprueba o rechaza narrativa, diseno o el archivo final con renders reales.
- `ppt-builder/`: ejecuta la construccion usando `pptx`, genera renders y entrega evidencia reproducible.

## Artefactos canonicos

- `brief.json`
- `workflow-state.json`
- `agent-routing.json`
- `storyline.md`
- `slide-outline.json`
- `style-preset-catalog.md`
- `visual-brief.md`
- `image-prompts.json`
- `data-viz-spec.json`
- `style-preview-set.md`
- `theme-spec.json`
- `design-rules.md`
- `closing-slide-brief.md`
- `review-report.md`
- `fix-list.json`
- `deck-build-plan.json`

## Contratos

- Los artefactos JSON tienen schemas en `schemas/decks/`.
- Los artefactos Markdown tienen contratos de secciones en `schemas/decks/markdown-contracts.md`.
- `schemas/decks-artifacts.md` es el indice legible; los JSON Schema son la fuente de verdad ejecutable.
- `brief.json` evoluciona por estados: `draft`, `enriched`, `ready`.
- Solo un brief `ready` exige objetivo, audiencia y decision esperada.
- Los campos marcados como opcionales no deben incluirse vacios solo para satisfacer un schema.
- Las visualizaciones de datos no son imagenes editoriales: se especifican en `data-viz-spec.json` y no se generan con `@imagegen`.

## Flujo recomendado

1. `orchestrator` clasifica la fase y hace preguntas de intake.
2. `narrative` produce tesis, storyline y outline de slides.
3. `design` produce 3 previews de direccion visual, define recursos visuales y fija el sistema elegido.
4. `review` hace el gate previo de narrativa, visual y diseno.
5. `ppt-builder` arma el deck con la skill `pptx` y genera renders/evidencia.
6. `review` inspecciona la ejecucion real antes de aprobar la entrega final.

Un deck no esta terminado solo porque el `.pptx` abre. Debe pasar revision visual sobre renders reales y, cuando exista una version previa preferida, no debe retroceder en naturalidad o polish.

## Uso proporcional de agentes

No todos los pedidos de slides necesitan el flujo completo de agentes. Si el
usuario ya trae research, contenido listo o una estructura operativa clara, y el
deck es corto o explicativo, puede ser mejor construir directamente con la skill
`pptx` y aplicar solo revision final.

Usa el flujo completo de agentes cuando agregue criterio real:

- presentaciones ejecutivas con decision, persuasion o audiencia sensible;
- decks largos o con storyline incierto;
- contenido tecnico duro que necesita jerarquia narrativa;
- redisenos donde el sistema visual todavia no esta decidido;
- trabajos donde el riesgo principal no es construir el archivo, sino decidir
  que debe decir y como debe leerse.

Para decks simples del tipo "explicame X en N slides", "que es / que necesito /
como empiezo / que puedo hacer", o cuando el usuario ya definio el contenido,
preserva esa estructura y evita convertirla en una tesis ejecutiva salvo pedido
explicito.

## Principios importados al dominio

- toda deck parte de una tesis, no de un tema suelto;
- los titulos de slides deben ser conclusiones, no encabezados genericos;
- cada slide debe tener lectura ejecutiva y prueba visible;
- la slide final debe cerrar con intencion editorial, no como resumen tecnico;
- la definicion de estilo debe hacerse con previews comparables, no solo con descripciones abstractas;
- el deck debe sentirse intencional y distintivo, no como una plantilla corporativa generica.
- la calidad visual final pesa mas que la elegancia de los artefactos conceptuales;
- si el usuario prefiere una version anterior, se preserva su sistema visual salvo pedido explicito de rediseno.
- cuando el encargo ya trae una estructura de preguntas operativas, esa
  estructura es el backbone del deck y no debe reemplazarse por una narrativa
  ejecutiva sin razon.

## Biblioteca de estilos

El dominio puede apoyarse en una biblioteca de presets visuales para acelerar la fase de `style-discovery`.

Uso recomendado:

- usar los presets como puntos de partida, no como plantillas rigidas;
- traducir cada preset a reglas de PPT: paleta, tipografia, layouts, tablas, charts y cierre;
- evitar aplicar presets muy teatrales si la audiencia no lo tolera;
- conservar siempre una opcion editorial segura, una opcion mas audaz y una wildcard defendible.

## Pendientes

- Ejecutar un ejercicio comparativo mas con el flujo actualizado: mismo brief,
  una version con agentes y una version directa con `pptx`, midiendo alineacion
  al encargo, calidad visual, costo de contexto y tiempo de ejecucion.
