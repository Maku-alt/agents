# Agents Registry

## Proposito

Este repositorio mantiene el catalogo reutilizable de custom agents de Codex. La fuente activa vive en `agents/<slug>/`; `~/.codex/agents` y los `.codex/agents` de otros proyectos son copias desplegadas.

## Orquestacion

- El hilo principal conserva objetivo, decisiones, plan, handoffs e integracion final.
- Usa un agente especializado solo para una tarea sustancial, acotada y compatible con su descripcion.
- No crees un agente `orchestrator`: la orquestacion es responsabilidad del hilo principal.
- No permitas que un builder apruebe su propio artefacto.
- Evita escrituras paralelas sobre los mismos archivos.

## Curacion

- Cada agente activo debe tener `agent.toml`, `metadata.json` e `instructions.md`.
- `agent.toml` debe ser autocontenido y definir `name`, `description` y `developer_instructions`.
- Los nombres usan `snake_case`; el directorio usa el mismo slug.
- Declara skills requeridas en metadata y tambien en las instrucciones ejecutables.
- No fijes modelo salvo que el rol lo necesite de forma material; heredar defaults mejora portabilidad entre PCs.
- Mueve agentes retirados a `archive/` en vez de borrarlos sin trazabilidad.

## Validacion

Antes de cerrar cambios ejecuta:

```powershell
python .\scripts\build_registry.py --check
.\sync-to-codex.ps1 -WhatIf
git diff --check
```
