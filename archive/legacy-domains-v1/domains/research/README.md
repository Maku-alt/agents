# Research Domain

Dominio transversal para investigaciones con evidencia externa, sintesis critica y recomendaciones accionables.

## Objetivo

Convertir preguntas abiertas, comparaciones, decisiones o exploraciones en research estructurado. El dominio prioriza evidencia confiable, perspectivas relevantes, contradicciones explicitas, calibracion de esfuerzo y self-review cuando la profundidad lo justifica.

## Agentes

- `researcher/`: investiga temas con fuentes externas confiables, ajustando el nivel de esfuerzo entre `quick`, `standard` y `deep`.

## Flujo recomendado

1. `researcher` calibra el nivel de esfuerzo segun la pregunta, el riesgo y las instrucciones del usuario.
2. Reformula la pregunta y define el modo de trabajo.
3. Busca y evalua evidencia externa.
4. Contrasta fuentes, perspectivas y contradicciones.
5. Sintetiza hallazgos, limites y recomendacion.
6. Declara fuentes, confianza y puntos donde conviene profundizar.

## Principios del dominio

- no maximizar volumen: ajustar rigor al valor real de la investigacion;
- no entregar solo links ni teoria;
- distinguir hechos, inferencias, hipotesis y claims debiles;
- no esconder contradicciones;
- priorizar fuentes primarias o de alta autoridad;
- usar modo `deep` cuando el usuario lo pida explicitamente o el tema lo amerite.

## Minimo utilizable en otro repo

- `domains/research/researcher/agent.md`

