# 04 — Auditoría de consistencia de documentación y código

**Estado:** auditoría documental realizada el 2026-11-05; sin cambios de gameplay.  
**Repositorio/PR:** `jbob-coder/Rpg-game`, rama `work/text-rpg-narrative-core-v01`, PR #2 en borrador.

## Alcance contrastado

- `docs/01_CONTEXTUAL_ACTION_RESOLUTION.md`
- `docs/02_NPC_WORLD_NARRATION.md`
- `docs/03_STATUS_AND_NEXT_MILESTONES.md`
- `README.md`
- `src/game.mjs` y `tests/game.test.mjs` del prototipo implementado.

## Evidencia

- Fuente implementada `src/game.mjs`: hash Git `d34151ad925a92735c704c97fcb71930de10fbe5`.
- Pruebas `tests/game.test.mjs`: hash Git `40404ffad619823f94dba1f1eeae97c1c4921bec`.
- Los hashes de esos archivos en el workspace coinciden con los recuperados del PR #2.
- `npm test` ejecutado en workspace con Node.js 22.16.0: **7 pruebas aprobadas; 0 fallos**. No se probaron el futuro `ActionResolver` ni un `NPCPlanner`.
- Verificación de PR: borrador sin fusionar a `main`.

## Hallazgos y correcciones de esta revisión

**D01 — Redacción incorrecta sobre frontend:** el documento 02 decía que la UI del PR #1 ya consultaba `NarrativeView`. **Corregido:** el PR #1 es una maqueta sin integración de gameplay; el contrato se establece como requisito futuro.

**D02 — Ambigüedad sobre autonomía temporal:** se podía interpretar que el mundo progresaba en tiempo real o con la app cerrada. **Corregido:** el prototipo actual procesa una agenda fija al adelantar el reloj con `wait` o `rest`. El avance fuera de sesión es una decisión pendiente; el `EventScheduler` ampliado es una propuesta.

**D03 — Alcance de autonomía NPC:** los eventos del mercado son programados, no decisiones de agentes con objetivos propios. Se precisa explícitamente en los documentos 01–03. El `NPCPlanner` sigue pendiente.

**D04 — Atribuciones y porcentajes:** los pesos 30/20/50, los umbrales del código y los cuatro grados de resultado están declarados como ejemplos o propuestas, **no balance confirmado**. Verificado sin cambios.

**D05 — Continuidad y pruebas:** el plan del documento 03 distingue la verificación real de las pruebas del código de las pruebas futuras de arquitectura. Se actualizó con resultados observados.

## Consistencia con acuerdos del propietario

- RPG de texto independiente, sin mapas; sin contenido de otros proyectos.
- Class y Background se eligen al crear el personaje; Background permanece como registro.
- Skills y Ability Tree son funciones diferentes; Abilities no usa cooldowns.
- NPC deben poder actuar por objetivos en la **futura arquitectura**, con las mismas reglas de resolución que el jugador.
- Capacidades y requisitos + factores contextuales relevantes + incertidumbre solo cuando corresponda.
- Consecuencias persistentes y narración limitada a conocimientos reales del personaje.
- Frontend/skins desacoplados de reglas del juego.
- `main` no se cambia por la documentación.

## Riesgos y próximos pasos

1. Validar rangos/unidades de Stats y Skills antes de fijar pesos.
2. Añadir tests para esquema de factores, puertas de viabilidad y cálculo reproducible.
3. Migrar una acción con un adaptador compatible, no todas a la vez.
4. Probar idempotencia, save/load, filtrado de conocimiento y costes.
5. Sólo después introducir selección de intenciones de NPC y conectar con la UI.

**Resultado:** la arquitectura descrita coincide con la dirección discutida, tras corregir las afirmaciones que confundían propuestas con funciones implementadas. No se afirma que el motor avanzado funcione ni que exista validación Android.
