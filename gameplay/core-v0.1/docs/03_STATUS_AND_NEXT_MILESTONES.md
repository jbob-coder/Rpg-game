# Continuidad y próximos hitos del RPG de texto

**Estado:** Plan de trabajo; fecha de referencia 2026-11-05. La documentación no ejecuta trabajos futuros ni demuestra que exista el motor avanzado.

## CURRENT_OBJECTIVE
Pasar de la resolución con umbrales fijos a acciones configurables con requisitos, factores contextuales, consecuencias causales y NPC autónomos, manteniendo una narración coherente y el motor desacoplado del frontend.

## REPOSITORY / BRANCHES
- `jbob-coder/Rpg-game`.
- `work/text-rpg-narrative-core-v01`: PR #2, gameplay y documentos de diseño.
- `docs/text-rpg-design-foundation-20261105`: PR #1, interfaz y guías visuales.
- Mantener `main` intacta hasta revisión. Verificar HEAD y cambios de otros colaboradores al retomar. No mezclar con otros RPG.

## VERIFIED_STATE
En `gameplay/core-v0.1/src/game.mjs` existen creación de personaje, dos acciones con umbrales, agotamiento, una cadena de mercado días 2/4/6, historial real y conocimiento separados, y funciones de guardado JSON. En una revisión anterior se informaron siete pruebas Node aprobadas del prototipo original; **añadir estos documentos no implica volver a ejecutarlas**. No hay integración de UI, APK ni motor genérico de NPC/acciones.

## DECISIONS
- Enfoque híbrido de perfiles configurables + contexto real.
- Selector de intenciones NPC independiente del evaluador compartido con el jugador.
- Requisitos físicos y lógicos previos a dificultad o azar.
- Incertidumbre solo cuando tenga sentido y siempre reproducible.
- Aplicación idempotente de consecuencias y ledger causal.
- Narración solo de hechos observados o descubiertos.
- Diseño e implementación independientes de imágenes, texturas y mapas.
- Todas las cifras del documento 01 son **propuestas**, no balance oficial.

## NEXT_ACTIONS
1. **M0 — Revisión del diseño:** confirmar escalas y nombres iniciales de Stats/Skills; clasificar acciones deterministas y variables. No bloquear la creación de tests por cuestiones estéticas.
2. **M1 — Contratos probados:** introducir esquemas versionados de `ActionProfile`, `ContextFact`, `ActionOutcome`; tests de validación, límites y fuentes; sin modificar el motor actual.
3. **M2 — Evaluador puro:** resolver una acción de demostración con contexto y resultados estructurados; repetir inputs debe dar igual resultado sin mutar el estado.
4. **M3 — Migración controlada:** conectar una acción actual al evaluador; verificar compatibilidad de costos, flags, save/load y condiciones; no migrar todas a la vez.
5. **M4 — Contexto y consecuencias:** ayuda, herramientas, fatiga, condiciones temporales, grado de resultado, idempotencia y pruebas de cadenas.
6. **M5 — NPCPlanner:** dos NPC con distintas metas y percepciones; mismas reglas de resolución; medir presupuesto de simulación.
7. **M6 — Narración y UI:** projection de conocimiento, mensajes no contradictorios e integración posterior en rama supervisada con PR #1.
8. **M7 — QA Android:** versión empaquetable, insets, guardado/carga, rendimiento y pruebas en equipo físico.

## RISKS / MITIGATIONS
- Factores infinitos o duplicados: catálogo explícito, límite de acumulación y auditoría.
- Fórmulas no equilibradas: simulaciones de sensibilidad y métricas por perfil antes de aprobar pesos.
- RNG cambiado por carga: guardar estado/versiones y resultados.
- NPC que siguen guiones rígidos: objetivos, percepciones y prioridades con tests.
- Narrador omnisciente: filtrar conocimiento y fuentes.
- Regresiones de guardado: versiones y migraciones expresas.
- Exceso de CPU: lotes discretos y estados agregados para regiones lejanas.

## OPEN QUESTIONS
Escalas de atributos; pesos finales; tipos de riesgo; condiciones de fracaso grave; reglas de experiencia; límites de NPC simulados; avance del mundo con app cerrada; primer catálogo de actividades. Resolver por hito, no imponer decisiones prematuras.

## NEXT SESSION CHECKPOINT
Leer README y los documentos 01–03, verificar el PR #2 y ejecutar `npm test` en `gameplay/core-v0.1/` cuando haya entorno Node. Registrar resultados observados, crear una rama de implementación si cambia la arquitectura, implementar M1 en el cambio reversible más pequeño y documentar decisiones nuevas. No inferir pruebas aprobadas a partir de este plan.
