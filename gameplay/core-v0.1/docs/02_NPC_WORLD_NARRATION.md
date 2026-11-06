# NPC autónomos, causalidad y narración del RPG

**Estado:** Propuesta conceptual pendiente de implementación. **Fecha:** 2026-11-05.

## Regla central

Separar **decidir qué hacer**, **evaluar qué sucede**, **aplicar consecuencias** y **narrar lo conocido**. Un NPC no obtiene resultados automáticamente por elegir una tarea, y el narrador no decide cómo se calcula una acción.

## Selección autónoma de acciones

Un `NPCPlanner` procesa objetivos, necesidades, rol, personalidad, recursos, relaciones, memoria y percepción local. Genera candidatas del catálogo, descarta las inviables según lo que sabe, compara utilidad (beneficio esperado, costo, riesgo, tiempo y urgencia) y elige una intención de modo reproducible. Luego invoca el mismo ActionResolver que utiliza el jugador.

La utilidad selecciona una **intención**, no garantiza éxito. NPC con idénticas estadísticas pueden actuar distinto por metas o información distinta. No atribuir conocimiento omnisciente a comerciantes, guardias o aldeanos.

## Decisión del propietario — criterio de elección de NPC (2026-11-06)

**Aprobado como comportamiento objetivo, NO implementado:** los NPC **no** elegirán siempre la acción objetivamente más ventajosa. Sus decisiones estarán influidas por su personalidad, emociones, experiencias previas, relaciones y percepción limitada del mundo, incluso si ello les lleva a actuar de forma poco conveniente.

**Implicaciones funcionales para el futuro `NPCPlanner`:**
- Construir candidatas compatibles con los métodos que conoce el actor; los requisitos físicos y recursos disponibles siguen siendo validados por el motor de acciones.
- Evaluar las candidatas desde la **perspectiva del NPC**, no desde un cálculo omnisciente: objetivos/necesidades, urgencia, recompensa percibida, costo, riesgo percibido, vínculos, memoria y estado emocional.
- Personalidad y relaciones modulan prioridades; emociones y experiencias pueden alterar valoración y percepción. Un NPC orgulloso puede rechazar ayuda; uno temeroso puede evitar una ruta viable; uno leal puede asumir un costo por alguien cercano.
- La selección genera **intención**, nunca éxito automático. El `ActionResolver` común evalúa viabilidad y resultado según reglas, capacidades y contexto verdadero. No inventar recursos, alterar probabilidades a escondidas ni usar información desconocida.
- Conservar trazabilidad interna de factores de decisión y reproducibilidad mediante estado/semilla versionados; permitir elecciones imperfectas sin volverlas arbitrarias o incoherentes.
- **Por definir con el propietario:** qué rasgos son relativamente estables, cómo cambian las emociones, duración/intensidad de recuerdos y relaciones, y límites de decisiones autodestructivas o gravemente arriesgadas.

**Pruebas de aceptación futuras:** (1) misma situación externa pero distintas personalidades puede cambiar la intención; (2) misma personalidad pero emoción, recuerdos o relaciones distintos puede alterar la decisión; (3) un NPC nunca actúa con hechos secretos como si los conociera; (4) decidir no concede éxito ni evita requisitos; (5) guardar/cargar preserva decisiones ya confirmadas sin recalcularlas silenciosamente.

## Simulación de mundo eficiente

**Propuesta futura:** utilizar avances discretos, colas de eventos y simulación agregada para NPC/facciones distantes. No simular cada NPC a cada segundo en Android. Los acontecimientos pueden iniciarse, evolucionar, expirar y producir consecuencias sin que el jugador los observe. Si desaparecen precondiciones, cancelar o transformar resultados pendientes en vez de aplicar ambos desenlaces.

Entidades previstas:
- `WorldFact`: estado verdadero y versionado de recursos, relaciones y condiciones.
- `EventInstance`: suceso con estado, participantes, disparador, plazo y dependencias.
- `ActionAttempt`: intención, factores utilizados y resultado.
- `Consequence`: cambio idempotente y posibles seguimientos.
- `WorldLedger`: acontecimientos realmente ocurridos.
- `KnowledgeLedger`: hechos que cada personaje conoce, cómo los conoció y con qué certeza.
- `NarrativeView`: prosa y opciones derivadas de hechos perceptibles.

## Narración realista

La narración toma hechos estructurados del motor. Puede expresar esfuerzo, tensión, cansancio, señales del entorno y reacción social, siempre que estén respaldados por hechos observados. No mostrar automáticamente todas las cifras ni revelar motivos ocultos, resultados distantes o conspiraciones desconocidas.

Por ejemplo, una entrega se retrasa sin intervención del jugador. Al regresar días después, ve menos mercancía y precios mayores; puede investigar posteriormente por qué sucedió. Primero se aplican cambios a la economía; después el personaje descubre lo que puede conocer.

Comenzar con plantillas contextuales y combinaciones de texto verificables. La generación libre de narración, si se usa posteriormente, debe estar restringida por el conjunto de hechos y verificaciones de coherencia.

## Límites con el frontend

La UI del PR #1 es actualmente una **maqueta independiente**, sin conexión a `gameplay/core-v0.1`. **En una integración futura**, debería consumir una vista de presentación como `NarrativeView` y despachar identificadores de acciones; nunca modificar progreso, NPC ni eventos por sí misma. El motor no conoce bordes, botones, texturas ni ratios. Character → Background consulta un origen inmutable y entradas de su cronología, no reescribe la historia inicial. Skills y Ability Tree siguen separados; las Abilities no usan cooldowns.

## Casos de prueba pendientes

- Dos NPC con metas diferentes escogen acciones diferentes con atributos iguales.
- El mismo evaluador genera resultados coherentes para jugadores y NPC.
- Los eventos progresan aun cuando el jugador nunca visite el escenario.
- Guardar/cargar no duplica efectos ni rehace resultados de incertidumbre.
- El protagonista no conoce hechos ocultos antes de descubrirlos.
- Simular muchos actores y regiones no consume recursos ilimitados en Android.
- La prosa nunca contradice inventario, daños, relaciones o hechos del ledger.
