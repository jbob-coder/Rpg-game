# 05 — Función del sistema y plan verificable de construcción

**Estado:** arquitectura propuesta para revisión, NO motor implementado. **Revisión:** 2026-11-06.  
**Proyecto:** `jbob-coder/Rpg-game` — RPG móvil de texto independiente; sin mapas, modelos 3D ni mezcla con otros juegos.  
**Fuentes:** [01 Resolución contextual](01_CONTEXTUAL_ACTION_RESOLUTION.md), [02 NPC y narración](02_NPC_WORLD_NARRATION.md), [03 Hitos](03_STATUS_AND_NEXT_MILESTONES.md) y especificaciones del PR #1. Este documento consolida el **comportamiento esperado**, las **fronteras** y la **secuencia de construcción**. No sustituye decisiones de balance pendientes.

## 1. Para qué existe

Permitir que un personaje o NPC intente actividades coherentes con sus capacidades y el estado del mundo; determinar si se pueden intentar, cómo se resuelven y qué consecuencias dejan; registrar esos resultados y narrar al protagonista solo lo que puede conocer. El mundo debe avanzar mediante eventos y agentes **sin depender del panel abierto ni de una intervención del jugador**.

La meta NO es un generador de porcentajes arbitrarios ni una IA narrativa que cambie reglas sobre la marcha. Los números proceden de reglas versionadas y datos del mundo; la prosa se genera **después** de resolver los efectos.

## 2. Flujo completo de una acción

```text
Jugador elige acción conocida  ─┐
                                ├─> ActionIntent
NPCPlanner escoge intención    ─┘         |
                                           v
                                  ActionCatalog (reglas)
                                           |
                                           v
                            Elegibilidad + snapshot contextual
                                           |
                                           v
                                  ActionResolver (puro)
                                           |
                                           v
                       ConsequenceApplier + EventScheduler
                                           |
                                           v
                     WorldState/WorldLedger + guardado versionado
                                           |
                                           v
                        KnowledgeProjection (por observador)
                                           |
                                           v
                         Narrator -> ViewModel -> interfaz
```

1. **Seleccionar intención**: el protagonista **solo selecciona una opción contextual presentada por el juego**, mediante un identificador estable; **no escribe acciones** ni usa parser de texto libre. La UI obtiene elecciones del ViewModel y el dominio revalida requisitos al recibir el ID. El NPCPlanner elige según percepción, metas y recursos. Ninguno garantiza el desenlace.
2. **Validar elegibilidad**: acción, método y objetivo existentes; acceso, conocimientos, recursos y límites físicos. Si es imposible, devolver motivo accesible sin efectuar gastos ni cambios. Una herramienta o aliado puede habilitar un **método alternativo**, no hacer desaparecer un requisito absoluto por azar.
3. **Construir contexto**: extraer solo hechos relevantes, con valor, fuente, unidad, versión, ámbito y vencimiento. Separar verdad del mundo de lo que el actor sabe: el motor verifica hechos reales; la selección de intenciones no debe usar información desconocida por el NPC.
4. **Resolver**: transformar valores a escalas comparables definidas por las reglas, evaluar dificultad y riesgos, aplicar límites de modificación y azar controlado **solo cuando corresponda**. Devolver un resultado estructurado; no escribir estado ni texto.
5. **Confirmar consecuencias**: revalidar precondiciones frente al estado vigente y aplicar una sola vez costos, recursos, relaciones, experiencia si está definida, consecuencias y eventos diferidos. Registrar intento y resultado bajo ID único. Si el contexto cambió, rechazar/recalcular según una política versionada; jamás aplicar un resultado obsoleto silenciosamente.
6. **Actualizar conocimiento y narración**: revelar hechos por observación, conversación o descubrimiento; producir texto desde hechos autorizados, sin exponer intenciones secretas, variables ocultas ni resultados no observados.

**Contrato de consistencia:** el intento debe resolverse sobre una instantánea coherente, y la aplicación del resultado debe ser atómica e idempotente. Una acción válida fallida puede gastar tiempo/resistencia según perfil; una acción inválida no consume recursos. Guardar/cargar nunca vuelve a ejecutar efectos ya confirmados.

## Decisión del propietario: simulación activa y pausa manual (2026-11-06)

**Objetivo funcional — NO implementado:** el mundo sigue avanzando mientras la app está en primer plano y la partida activa, incluso si el jugador lee la narración o considera una opción. El usuario dispone de **Pausar / Reanudar**. El reloj de juego, la cola de eventos y los planes y acciones temporizadas de NPC se congelan mientras la partida está pausada; se permite navegar y consultar información sin consumir tiempo. No debe aplicarse ningún suceso vencido durante Pausa ni «recuperar» retroactivamente ese intervalo al reanudar.

**Contrato propuesto:** `GameClock` mantiene `simulation_time`, `clock_mode = running | paused`, factor de escala y último instante monotónico de ejecución. `SimulationScheduler` avanza con deltas acotados del tiempo real **solo en modo running** y ejecuta lotes discretos de eventos, sin un tick por NPC cada milisegundo. `PauseController` acepta comandos explícitos de pausa/reanudación idempotentes; `ViewModel` muestra el estado y control correspondiente. Evitar temporizadores basados únicamente en hora del sistema para impedir saltos inesperados tras reanudar. **Decisión confirmada:** mientras el juego está pausado, se bloquea toda orden que cambie el mundo o progrese una acción; no hay ejecución excepcional ni reanudación automática al pulsarla. El usuario debe seleccionar **Reanudar** explícitamente. Solo la UI de consulta, ajustes que no alteren la partida y el control de reanudar permanecen disponibles.

**Persistencia/QA:** definir la política de restauración del estado pausado; probar pausa durante lectura, eventos programados y guardado, reanudación sin ejecución doble ni salto temporal, y controles táctiles Android. La **velocidad real→tiempo del mundo**, el comportamiento al ir a segundo plano o cerrar, y la recuperación fuera de sesión siguen **pendientes**. No confundir pausa manual con suspensión automática del sistema operativo.

## Decisión del propietario: duración de las acciones (2026-11-06)

**Objetivo funcional — NO implementado en el prototipo v0.1:** algunas acciones elegidas consumen tiempo del mundo, adicional a la existencia de un reloj que avanza mientras se juega. No son dos relojes: existe una **única línea temporal de simulación** que gobierna NPC, relaciones, economía y eventos.

- Un `ActionProfile` declara reglas de duración/costo temporal según actividad y método, sin asignar minutos definitivos todavía. Ejemplos ilustrativos: una conversación puede durar unos minutos, una entrega puede requerir horas, consultar un panel no impone un costo de acción.
- El motor valida la opción, inicia el intento y procesa su intervalo de ejecución con el `SimulationScheduler`. En ese intervalo el mundo continúa y pueden cambiar circunstancias, cancelarse un plan o aparecer eventos derivados; el resultado se decide conforme a las reglas de resolución e interrupción.
- **Evitar doble cómputo:** si una actividad tarda tiempo real y el reloj ya estuvo avanzando, no sumar nuevamente toda su duración al completarla. Para acciones de avance discreto, procesar el intervalo lógico exactamente una vez, mediante el mismo reloj.
- **Pausa absoluta (propietario, 2026-11-06):** se detiene el reloj de juego y se congela el progreso de **todas** las acciones, incluidos trabajos, viajes, combates y acciones de NPC, además de eventos, economía y consecuencias temporizadas. Ninguna opción de gameplay se ejecuta mientras esté pausado; reanudar requiere una orden explícita del usuario. La interfaz de consulta y el botón Reanudar siguen funcionando; no constituyen progreso del juego. El período pausado no se recupera ni se suma al reloj después.
- Guardar inicio, fin lógico, progreso e IDs de eventos relevantes cuando corresponda, con reintentos idempotentes. Probar inicio→pausa→reanudar→fin, interrupciones, guardado/carga, orden de sucesos intermedios y ausencia de doble avance.

**Aún por definir:** escala temporal real/juego, duraciones exactas, acciones instantáneas frente a diferidas y política del juego en segundo plano o cerrado.

**Pruebas adicionales de pausa absoluta:** iniciar una acción prolongada, pausar, transcurrir tiempo real, confirmar que tiempo, progreso, recursos, estado de NPC y eventos permanecen idénticos; pulsar una opción de jugabilidad durante pausa no cambia estado; reanudar explícitamente y verificar continuación desde el mismo punto, sin saltos ni efectos duplicados.

## Decisión del propietario — modelo combinado de tiempo (2026-11-06)

**Aprobado como diseño; aún NO implementado:** un **reloj continuo con velocidad base fija mientras la partida esté activa**, combinado con **acciones que consumen la duración apropiada a su actividad** (viajar, trabajar, descansar, conversar, etc.). Los ejemplos de 1 minuto real = 10 minutos de juego o de 3/4 horas por acción eran ilustrativos; **ninguna proporción ni duración numérica quedó aprobada**. La pausa absoluta, ya acordada, congela ambos mecanismos y requiere reanudación explícita.

**Semántica recomendada del único reloj:** cada acción declara una duración lógica en sus reglas y se procesa mediante `GameClock`/`SimulationScheduler`. Si se ejecuta progresivamente durante el avance continuo, su duración **no se vuelve a sumar al terminar**. Si una acción se resuelve mediante un salto de tiempo de juego, el scheduler procesa ese intervalo una sola vez, con NPC y sucesos intermedios. No añadir un segundo reloj independiente ni congelar el resto del mundo cuando se calcula la acción. Registrar el inicio y final lógico, y manejar interrupciones, guardado/carga y pausa sin duplicar avance ni consecuencias.

**Velocidad base confirmada por el propietario (2026-11-06):** **1 minuto real = 1 minuto de juego (1:1)**, siempre que la partida esté activa y el reloj no esté pausado; la lectura y la reflexión del jugador no detienen ese avance. **Pausa absoluta:** tiempo de simulación y progreso de todas las acciones, NPC y eventos permanecen congelados, sin recuperación del tiempo pausado al reanudar. Las acciones de duración propia utilizan el mismo reloj; no se duplica tiempo ya contado. **Por decidir:** duraciones y categorías por acción, mecanismo de avance/salto, accesibilidad y política de segundo plano/app cerrada. No se ha aprobado acelerar o ralentizar automáticamente la velocidad base según contexto.

## 3. Responsabilidad de cada módulo

| Módulo | Recibe | Devuelve / persiste | No debe hacer |
|---|---|---|---|
| `ActionCatalog` | ID de acción y versión de reglas | Perfil con métodos, condiciones, factores aplicables, grados y costos | Leer UI o inventar balance en tiempo de ejecución |
| `NPCPlanner` | Percepción, necesidades, metas, personalidad, memoria y recursos conocidos | Intención y método elegidos | Decidir éxito o conocer secretos del mundo |
| `ContextProvider` | Actor, objetivos, hechos del mundo, tiempo y perfil | Snapshot reproducible con procedencia | Alterar el mundo ni mezclar factores irrelevantes |
| `ActionResolver` | Intención, perfil, snapshot y estado aleatorio si aplica | Elegibilidad, factores usados, margen/riesgo, grado, costos y efectos propuestos | Persistir o redactar narrativa |
| `ConsequenceApplier` | Resultado, versión actual de estado e ID de intento | Cambios atómicos, recibo de aplicación y entradas causales | Aplicar dos veces el mismo intento |
| `EventScheduler` | Eventos pendientes, reloj y condiciones vigentes | Eventos vencidos, cancelados, transformados y programados | Basar progresión en abrir una pantalla |
| `WorldLedger` y almacenamiento | Eventos aplicados, IDs, versiones, snapshots | Verdad persistente y restaurable | Confundir evento real con rumor |
| `KnowledgeProjection` | Verdad, posición/percepción del observador y descubrimientos | Hechos permitidos por personaje con fuente y certeza | Revelar secretos o alterar la verdad |
| `Narrator` / `ViewModel` | Hechos conocidos y resultados estructurados | Narración legible y acciones/requisitos visibles | Calcular éxito, conceder XP o mutar inventario |

Estos nombres son **contratos propuestos**; no representan clases ya escritas ni obligan a servicios separados. Pueden vivir dentro de una app Android sin conexión.

## 4. Modelo mínimo de datos, aún provisional

- **ActionProfile**: `action_id`, `rules_version`, métodos admitidos, requisitos absolutos, factores permitidos, normalización, límites, costos por resultado, opciones de incertidumbre, efectos, visibilidad.
- **ActionIntent**: `attempt_id` estable, actor, objetivo, acción, método y tiempo de solicitud. El ID permite deduplicar reintentos.
- **ContextFact**: ID semántico, valor, unidad, escala, fuente, alcance, sello temporal/vencimiento y versión de la entidad. Los datos ausentes se tratan como **desconocidos**, no como cero.
- **ActionResolution**: permitido/no permitido, razones internas, snapshot/versiones utilizadas, factores y sus contribuciones, grado de resultado, costos y efectos propuestos, eventos derivados y política de descubrimiento. Un fallo de elegibilidad NO equivale a un fracaso narrativo.
- **WorldEvent / WorldLedgerEntry**: ID de evento/causa, fecha de juego, transición, resultado, versiones y vínculo al intento, cuando proceda.
- **KnowledgeEntry**: observador, hecho referido, vía de descubrimiento, momento, fuente y fiabilidad; no copia sin filtro de todos los datos del mundo.
- **SaveSnapshot**: versión de formato, versión de reglas, estado, reloj, eventos pendientes/procesados, ledger, conocimientos, estado de incertidumbre y recibos de aplicación.

Las claves son ilustrativas: M1 deberá cerrar esquemas compatibles con guardados existentes. Versionar reglas **y** datos; una futura migración no debe cambiar de forma silenciosa resultados pasados.

## 5. Cómo se determinan éxito y fracaso

**Puerta 1 — posibilidad real:** sin acceso a la carga o sin ruta válida no hay intento de transporte manual. Buscar otro método constituye **otra evaluación** (por ejemplo, contratar ayuda o usar una carreta si el mundo dispone de ella).

**Puerta 2 — capacidad frente a dificultad:** normalizar atributos/skills a una escala común *antes* de calcular pesos. Solo combinar factores relevantes para el método y objetivo. Un esquema conceptual —no una fórmula aprobada— es:

```text
capacidad = combinación_versionada(atributos, habilidades, método)
dificultad = exigencia_base(objetivo, método) + condiciones_adversas
margen = capacidad + ayudas_acotadas - fatiga_no_duplicada - dificultad
```

La masa real de la carga, la lluvia o una lesión no son porcentajes universales. Deben tener unidades, alcance, duración y reglas explícitas. La carreta puede cambiar capacidad y riesgo del método; no sumar automáticamente el mismo beneficio varias veces. Definir un origen canónico por variable para evitar duplicación.

**Puerta 3 — incertidumbre opcional:** acciones triviales, físicamente imposibles o suficientemente dominadas pueden ser deterministas. En otras, aplicar una variación limitada y reproducible que no invalide restricciones duras. Registrar estado RNG/semilla, secuencia de uso y resultado confirmado para impedir volver a tirar al cargar.

**Puerta 4 — grados y costos:** éxito completo, parcial, fallo recuperable o grave **solo si tienen significado para esa actividad**. Cada grado define cambios verificables en tiempo, resistencia, inventario, lesiones, confianza, reputación, recursos y eventos. No convertir todo fallo en castigo grave. Las reglas precisas de XP, pesos, límites y probabilidades **siguen pendientes**.

## 6. Escenario de principio a fin: entrega de suministros (no canon)

Un comerciante necesita entregar alimentos. Su NPCPlanner detecta una obligación, conoce que la ruta habitual está cerrada y considera alternativas: esperar, usar ruta secundaria o contratar ayuda. La elección depende de costo, urgencia, riesgo y recursos **que ese NPC conozca**.

Elige contratar dos trabajadores y usar una carreta. El catálogo admite ese método si hay carreta, personal, carga y ruta transitables; el contexto confirma herramientas, masa, estado del camino, fatiga y costo. El evaluador calcula un resultado bajo la versión de reglas correspondiente; una demora puede ser éxito parcial, con entrega más tarde y costo adicional. El aplicador descuenta recursos, registra la entrega y programa una posible variación de abastecimiento. El narrador no anuncia al jugador esos movimientos si no estaba presente; al visitar el mercado después puede observar nuevos precios o escuchar una explicación fiable o un rumor.

**Prueba de causalidad:** cambiar solo el método, los recursos o el clima debe alterar exclusivamente las variables que esas reglas declaran pertinentes. El ledger debe permitir reconstruir *qué regla, hecho e intento* causaron el desenlace sin dar conocimiento omnisciente al protagonista.

## 7. Plan de implementación con criterios de salida

| Hito | Entregable reversible | Condición para avanzar |
|---|---|---|
| **M0 — reglas iniciales** | Inventario de stats/skills, unidades, rangos, métodos y variables relevantes; decisiones pendientes etiquetadas | No hay pesos finales asumidos; casos normales y extremos definidos |
| **M1 — contratos** | Esquemas versionados y validadores de `ActionProfile`, `ContextFact` y `ActionResolution`; tests de entradas ausentes/corruptas | Tests de validación y compatibilidad sin cambiar `dispatch` actual |
| **M2 — resolver puro** | Evaluación aislada de **una** acción ilustrativa; snapshot de contexto y trazas de cálculo | Mismos inputs/versiones -> mismo resultado; sin mutación ni secretos |
| **M3 — adaptador** | Integración opcional de **una** acción existente y pruebas de comparación con umbrales v0.1 | Costos, disponibilidad, flags y carga de partidas previas se preservan o la migración se justifica explícitamente |
| **M4 — consecuencias** | Factores temporales, resultados parciales, transacciones idempotentes y cola causal | Reintentos, interrupciones, colisiones, guardado/carga y cancelación no duplican efectos |
| **M5 — autonomía NPC** | Dos NPC con metas/percepciones diferentes usando el mismo resolver | Decisiones distintas justificadas por contexto; sin datos omniscientes; coste de simulación medido |
| **M6 — conocimiento y UI** | Proyección por observador, narración verificable e integración contractual con PR #1 | Eventos no observados no aparecen como hechos conocidos; interfaz no altera estado por sí misma |
| **M7 — QA móvil** | Paquete probatorio de funcionamiento en Android + batería de rendimiento/guardado/accesibilidad | Métricas y pruebas en dispositivo físico, no solo simulación de navegador |

**Orden de trabajo:** contratos → resolver aislado → migración de una acción → consecuencias → decisión NPC → narración/UI → Android. Cada hito se desarrolla en rama separada o commits revertibles, revisando HEAD de PR #1 y PR #2 antes de integrar. No fusionar a `main` por la sola existencia de documentación.

## 8. Invariantes y pruebas obligatorias

1. **Misma semilla, reglas, estado y decisiones** generan el mismo ledger y desenlace; variar idioma/skin/layout no cambia cálculos.
2. **Elegibilidad no es probabilidad:** recursos inexistentes y restricciones duras no se superan mediante tirada.
3. **Sin doble aplicación:** dos envíos del mismo `attempt_id`, dos cargas o un evento reintentado no duplican costos, XP, bienes ni consecuencias.
4. **Aislamiento de información:** cada NPC planea con su percepción; cada usuario recibe solo hechos observados/descubiertos. Auditar filtraciones en texto, UI y logs accesibles.
5. **Causalidad verificable:** todo cambio persistido identifica origen, versión, efecto y momento; eventos incompatibles se cancelan o transforman.
6. **Compatibilidad:** restaurar partidas v0.1 en pruebas de migración; rechazar entradas corruptas de forma controlada.
7. **Escalabilidad móvil:** cola y presupuestos de CPU/memoria por lote; simulación agregada de actores lejanos, sin exigir un tick por NPC por segundo. Objetivos cuantitativos: **pendientes de medición**.
8. **Diseño consistente:** Background es origen histórico consultable; Skills y Ability Tree permanecen diferenciados; no introducir cooldowns a Abilities; ninguna regla se calcula en componentes visuales.

Los tests actuales del núcleo v0.1 son **siete tests de demostración**; no certifican ninguno de los módulos M1–M7. Registrar comandos, versión del entorno y resultados reales al ejecutarlos.

## 9. Decisiones aún abiertas (no inventar canon)

Escalas y progresión de Stats/Skills; pesos por perfil; si se usan probabilidades y en qué acciones; límites de ayuda/fatiga; costos, lesiones y fracaso grave; aprendizaje/XP; políticas para hechos desconocidos; relojes y eventos simultáneos; avance con la app cerrada; objetivos de rendimiento Android; estrategias de migración y framework Android definitivo. Deben aprobarse durante el hito correspondiente, no suponer que están resueltas.

## 10. Relación con el código existente

**Implementado en v0.1:** validación inicial de clase/Background; dos comprobaciones fijas (`empathy + negotiation >= 7` y `strength + endurance + labor >= 12`); consumo de stamina; cadena comercial fija en días 2/4/6; descubrimiento diferido; guardado/carga JSON básico. Los eventos avanzan con `wait`/`rest`. **No hay planificador de NPC, catálogo general, normalización de stats, azar efectivo, simulación con app cerrada, integración de UI ni APK.** La semilla se guarda pero todavía no se utiliza para sorteos.

**Definición de completitud documental:** el plan especifica función, responsabilidad, contrato propuesto, ejemplo causal, orden de implementación y pruebas de salida. **No constituye aprobación de parámetros ni verificación de ejecución futura.**
