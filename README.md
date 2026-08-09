# Agents Registry

Repositorio fuente de verdad para agentes personalizados reutilizables de Codex.

## Modelo vigente

Codex carga agentes personalizados desde archivos TOML independientes:

- `~/.codex/agents/*.toml` para agentes personales disponibles entre proyectos;
- `.codex/agents/*.toml` para agentes propios de un proyecto.

`agents/openai.yaml` no configura el comportamiento de un custom agent: es metadata de interfaz para skills y plugins. Los contratos Markdown siguen siendo utiles como documentacion, pero la configuracion ejecutable de un subagente es TOML.

Este repositorio sigue el mismo principio de `skills-registry`:

- `agents/`: paquetes activos y curados;
- `catalog/`: diccionario humano e indice generado;
- `archive/`: configuraciones retiradas que conservamos por trazabilidad;
- `config/`: politica del catalogo;
- `scripts/`: validacion y generacion del indice;
- `sync-to-codex.ps1`: instalacion explicita en el runtime personal.

## Arquitectura de trabajo

El chat principal es el orquestador. Conserva objetivo, decisiones, estado, handoffs e integracion final. Los agentes de este catalogo son workers especializados; no sustituyen al hilo principal ni deciden por su cuenta la siguiente fase.

Set activo:

| Agente | Uso principal |
| --- | --- |
| `researcher` | Investigar preguntas abiertas con evidencia, contradicciones y trazabilidad. |
| `narrative_strategist` | Convertir evidencia aprobada en tesis, arco y contrato de contenido para una presentacion. |
| `experience_designer_builder` | Disenar y construir presentaciones HTML con `impeccable`. |
| `experience_reviewer` | Revisar de forma independiente el candidato web exacto y su evidencia. |
| `cross_functional_advisor` | Analizar tradeoffs complejos sin ejecutar ni aprobar fases. |

`experience_designer_builder` reemplaza la antigua cascada `design -> ppt-builder` para Web Talks. Si el usuario pide explicitamente PowerPoint, el hilo principal usa la skill `pptx` directamente; `impeccable` no es un builder de `.pptx`.

## Sincronizar con Codex

Vista previa:

```powershell
.\sync-to-codex.ps1 -WhatIf
```

Instalacion global:

```powershell
.\sync-to-codex.ps1
```

Instalar solo algunos agentes:

```powershell
.\sync-to-codex.ps1 -Names researcher,experience_reviewer
```

Instalar en un proyecto:

```powershell
.\sync-to-codex.ps1 -Destination C:\ruta\proyecto\.codex\agents
```

La sincronizacion no elimina agentes extra del destino salvo que se indique `-Prune`. La fuente permanente es este repo, no la copia runtime.

## Validacion

```powershell
python .\scripts\build_registry.py --check
.\sync-to-codex.ps1 -WhatIf
git diff --check
```

Para regenerar `catalog/agents-index.json` y `catalog/agents-dictionary.md`:

```powershell
python .\scripts\build_registry.py
```

## Legado

La arquitectura anterior por dominios, incluidos SQL, schemas y templates de decks, se conserva en `archive/legacy-domains-v1/`. No forma parte del set instalable y puede consultarse al reabrir un flujo historico.
