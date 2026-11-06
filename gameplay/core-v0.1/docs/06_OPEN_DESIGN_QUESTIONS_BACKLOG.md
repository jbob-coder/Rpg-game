# 06 — Inventario de preguntas de diseño pendientes (para responder gradualmente)

**Estado:** backlog de decisiones **abiertas y resueltas**, sin confundir preguntas con requisitos aprobados. **Fecha:** 2026-11-06.
**Repo:** `jbob-coder/Rpg-game`, rama `work/text-rpg-narrative-core-v01`, PR #2 (borrador).
**Alcance:** RPG independiente exclusivamente de texto; sintetiza preguntas derivadas de los docs 01–05 de gameplay y los docs 01–03 de diseño del PR #1. Es el listado completo de decisiones abiertas **identificadas en esta auditoría**; podrán aparecer otras al implementar.

## Uso del listado

- **P0** = decisión de alto impacto o que desbloquea contratos; **P1** = importante, pero puede decidirse más adelante; **P2** = puede posponerse.
- Las preguntas abiertas mantienen estado **PENDIENTE**. Las ya contestadas figuran como **RESUELTA**; sus subpreguntas siguen siendo detalles de implementación por precisar. Registrar decisiones, fecha, consecuencias para código y pruebas antes de actualizar cada estado.
- **Q01 — RESUELTA el 2026-11-06:** el jugador solo elige entre opciones contextuales ofrecidas por el juego, como elecciones o botones; **no escribe acciones ni se necesita parser de texto libre**. Este cambio afecta los contratos `ActionIntent` y `ViewModel`, y la lista de acciones visibles. **Q02** aborda ahora opciones caducadas o inválidas, no interpretación de texto libre.
- No modificar el motor ni aprobar pesos, escalas o canon por redactar preguntas.

## Decisiones del propietario ya acordadas (NO volver a preguntar)

- RPG narrativo de texto independiente, sin mapas ni modelos 3D.
- **Interacción del protagonista:** seleccionar entre opciones contextuales presentadas por el juego, sin entrada de acciones por texto libre. El dominio vuelve a validar cada selección al ejecutarse.
- Class y Background se eligen al crear el personaje; el Background permanece consultable sin reescribir el pasado.
- Mundo causal con eventos que pueden ocurrir sin intervención del jugador; narración limitada al conocimiento del personaje.
- Resolución híbrida: perfiles de reglas, requisitos físicos/lógicos, factores contextuales y azar opcional; resultados con consecuencias; NPC comparten evaluador pero tienen planificador separado.
- Los NPC pueden elegir acciones poco convenientes por personalidad, emociones, relaciones, experiencias y conocimiento limitado.
- Las emociones fluctúan con lo cotidiano; sucesos especialmente significativos pueden cambiar rasgos de personalidad; esos rasgos pueden volver a cambiar con experiencias futuras, no son permanentemente fijos.
- Skills y Ability Tree son conceptos distintos; Abilities sin cooldowns; la UI del PR #1 no está integrada al motor del PR #2.
- **Decisión 2026-11-06:** el mundo debe avanzar automáticamente durante la partida activa, incluso mientras el jugador lee o decide, salvo que este active **Pausa**. Pausa congela el reloj de juego y el procesamiento de NPC/eventos; la interfaz debe seguir permitiendo consultar el estado. La velocidad del reloj y la política de segundo plano/app cerrada siguen pendientes.
- **Estado del prototipo v0.1:** todavía solo avanza por comandos `wait` o `rest` y eventos fijos. Ni el reloj continuo, ni Pausa, ni el planificador NPC están implementados.

## Ampliación: 100 subpreguntas por cada pregunta principal

El inventario de **43 preguntas principales** se amplió en **4,300 subpreguntas**, organizadas como diez subtemas específicos por diez dimensiones de revisión funcional para cada pregunta. Son preguntas de diseño, **no requisitos aprobados ni código implementado**.

| Categoría | Preguntas originales | Subpreguntas | Documento |
|---|---:|---:|---|
| A. Interacción y experiencia del jugador | Q01–Q05 | 500 | [A — Interacción](questions/07_A_100_PER_QUESTION.md) |
| B. Personaje, progreso, clases y habilidades | Q06–Q12 | 700 | [B — Personaje](questions/07_B_100_PER_QUESTION.md) |
| C. Resolución de acciones y consecuencias | Q13–Q21 | 900 | [C — Resolución](questions/07_C_100_PER_QUESTION.md) |
| D. Autonomía, psicología y sociedad NPC | Q22–Q28 | 700 | [D — NPC](questions/07_D_100_PER_QUESTION.md) |
| E. Mundo autónomo, tiempo y causalidad | Q29–Q35 | 700 | [E — Mundo](questions/07_E_100_PER_QUESTION.md) |
| F. Narración y presentación | Q36–Q39 | 400 | [F — Narración](questions/07_F_100_PER_QUESTION.md) |
| G. Implementación, guardado y verificación | Q40–Q43 | 400 | [G — Técnica](questions/07_G_100_PER_QUESTION.md) |
| **TOTAL** | **43** | **4,300** | |

Para responder después, cita el ID exacto, por ejemplo `Q01.001`, `Q24.053` o `Q43.100`. Las 43 preguntas principales conservan sus prioridades P0/P1/P2. **No es necesario contestar 4,300 preguntas para comenzar a implementar:** el propósito es no perder decisiones, identificar dependencias y elegir primero las cuestiones que más afectan al diseño. Conservar las respuestas y sus efectos en contratos/pruebas antes de moverlas a estado aprobado.

**Control de calidad documental:** se comprobó que los 43 grupos Q01–Q43 contienen 100 subpreguntas cada uno, con 4,300 identificadores distintos y formato interrogativo. No se ejecutaron nuevas pruebas del motor.

**Criterio de actualización (2026-11-06):** Q01 quedó resuelta. Las preguntas hipotéticas sobre escribir órdenes, usar un parser o combinar texto libre con botones fueron sustituidas por preguntas pertinentes a opciones contextuales. Las 4,300 subpreguntas son una **biblioteca exploratoria de pruebas y decisiones**, no 4,300 obligaciones ni mecánicas independientes.

## Decisión del propietario — reloj activo con pausa manual (2026-11-06)

**Aprobado a nivel funcional, todavía no implementado:** el reloj y los acontecimientos del mundo avanzan durante el juego activo aunque el usuario esté leyendo las opciones; el jugador puede **pausar y reanudar** voluntariamente. La pausa detiene tiempo de simulación, procesamiento de eventos y decisiones NPC. Consultar menús o revisar historial sigue disponible sin modificar el mundo mientras esté pausado. **Decisión confirmada:** durante Pausa no se puede ejecutar **ninguna acción de juego** ni progresar acciones en curso; únicamente consultar la interfaz y reanudar explícitamente. No hay excepciones de simulación.

**Aclaración del propietario (2026-11-06): «Pausa es pausa; todo se detiene».** Esto incluye tiempo, progreso de acciones del jugador, NPC, combate, viajes, producción, economía, eventos y consecuencias pendientes. No hay cómputo retroactivo durante el intervalo pausado. Solo siguen activos controles de consulta y **Reanudar** para que el usuario pueda salir de la pausa; no son acciones que alteran el mundo.

**Separación:** «pausa manual» ≠ «aplicación en segundo plano o cerrada»; la política para los últimos dos casos sigue abierta. La velocidad y cadencia del mundo también están pendientes. **El código v0.1 NO dispone aún de reloj continuo ni pausa**, por lo que la decisión es un requisito futuro, no una prueba superada.

## Decisión del propietario — duración de acciones y reloj del mundo (2026-11-06)

**Confirmado como dirección funcional, todavía no implementado:** además de avanzar automáticamente mientras la partida esté activa (salvo Pausa), determinadas **acciones elegidas por el jugador consumen tiempo dentro del juego**. Este tiempo pertenece al mismo reloj de simulación que utilizan eventos y NPC, no a un reloj paralelo; por ejemplo, trabajar o viajar puede adelantar acontecimientos y cambiar la disponibilidad de interlocutores.

**Requisito de coherencia:** cada acción tendrá un costo temporal definido por su perfil y método; los costos concretos siguen abiertos. El avance debe procesar eventos y decisiones NPC correspondientes al intervalo y **no contar dos veces tiempo real y tiempo de la acción**. Definir si la duración se simula progresivamente o se resuelve en un avance discreto; ambos métodos deben producir consecuencias consistentes. El estado pausado sigue congelando la simulación. Los menús de consulta no deben consumir tiempo de juego por sí mismos mientras la partida esté pausada.

**Pendiente:** duraciones por acción, acciones instantáneas, interrupciones y acciones que terminan a destiempo. La escala base para partida activa ya está decidida: 1:1. No implica que el prototipo v0.1 ya implemente reloj continuo ni decisiones NPC.

## Decisión del propietario — modelo de tiempo combinado (2026-11-06)

**Confirmado a nivel conceptual (no implementado):** el mundo avanza a razón de **1 minuto real = 1 minuto de juego (1:1)** cuando la partida está activa y no pausada, incluso mientras el jugador lee o decide. Determinadas acciones tienen **duración lógica propia**, que puede avanzar horas del mundo; sus duraciones exactas siguen pendientes. **Un solo reloj** compartido por jugador, NPC y eventos evita contar dos veces el tiempo. La **pausa absoluta** congela todo progreso del mundo y no acumula tiempo para recuperarlo al reanudar. El comportamiento con la app en segundo plano o cerrada no está decidido.

## Preguntas abiertas priorizadas

### A. Interacción y experiencia del jugador

01. **Q01 · P0 · RESUELTA (2026-11-06).** ¿Cómo introduce el jugador las acciones? **Respuesta:** mediante opciones contextuales seleccionables; no se permite escribir acciones. Las subpreguntas Q01.001–Q01.100 tratan detalles técnicos aún abiertos, no reabren esta elección.
02. **Q02 · P0 · PENDIENTE.** ¿Qué debe hacer el sistema si una opción seleccionable deja de estar disponible o ya no cumple sus requisitos cuando el jugador la pulsa?
03. **Q03 · P1 · PENDIENTE.** ¿Puede encadenar planes de varios pasos o debe confirmar cada acción antes de ejecutarla?
04. **Q04 · P0 · PARCIALMENTE RESUELTA (2026-11-06).** Las acciones pueden consumir tiempo de juego y deben avanzar el mismo reloj del mundo; **pendientes** sus duraciones por tipo, interacción con avance continuo, interrupciones y reglas concretas para lectura/menús.
05. **Q05 · P1 · PENDIENTE.** ¿Qué consecuencias tiene la derrota o muerte del protagonista: heridas, pérdida de recursos, continuación, final de partida u otras?

### B. Personaje, progreso, clases y habilidades

06. **Q06 · P0 · PENDIENTE.** ¿Cuáles son los Stats iniciales oficiales y qué significa cada uno mecánicamente?
07. **Q07 · P0 · PENDIENTE.** ¿Qué escala, límites iniciales y crecimiento tienen Stats, Skills y demás valores?
08. **Q08 · P0 · PENDIENTE.** ¿Cómo se distinguen Skills, Ability Proficiency, Abilities y Ability Tree en el cálculo y la progresión?
09. **Q09 · P0 · PENDIENTE.** ¿Por qué actividades se obtiene experiencia y cómo se distribuye entre atributos, competencias, clase y habilidades?
10. **Q10 · P1 · PENDIENTE.** ¿Qué clases se pueden seleccionar al inicio, cuáles se desbloquean y se permite cambiar o especializar la clase después?
11. **Q11 · P1 · PENDIENTE.** ¿Qué opciones de Background y rarezas existen y cuáles afectan hechos, recursos, relaciones u oportunidades sin determinar el destino?
12. **Q12 · P1 · PENDIENTE.** ¿Cómo se desbloquean y mejoran las Abilities y las ramas del árbol, sin introducir cooldowns?

### C. Resolución de acciones y consecuencias

13. **Q13 · P0 · PENDIENTE.** ¿Qué tipos de requisitos son absolutos (físicos, conocimiento, acceso, recursos) y cuáles solo modifican la dificultad?
14. **Q14 · P0 · PENDIENTE.** ¿Qué variables contextuales iniciales se registrarán y cuáles son sus unidades, fuentes, caducidad y ámbitos de aplicación?
15. **Q15 · P0 · PENDIENTE.** ¿Qué método normalizará valores y calibrará los pesos por tipo de acción sin mezclar escalas ni duplicar factores?
16. **Q16 · P0 · PENDIENTE.** ¿Qué acciones serán deterministas y cuáles tendrán incertidumbre reproducible y limitada?
17. **Q17 · P1 · PENDIENTE.** ¿Qué grados de resultado necesita cada familia de acciones y cuándo procede un fracaso grave?
18. **Q18 · P1 · PENDIENTE.** ¿Cuánto tiempo, resistencia, recursos, lesiones o repercusiones puede costar un intento válido fallido?
19. **Q19 · P1 · PENDIENTE.** ¿Cómo cambian los requisitos y resultados cuando se usa otra herramienta, método, ayuda o preparación?
20. **Q20 · P1 · PENDIENTE.** ¿El combate usará el mismo núcleo de evaluación con reglas especializadas o un subsistema aparte que comparta contratos?
21. **Q21 · P1 · PENDIENTE.** ¿Cómo se ajusta la dificultad de retos y regiones sin escalar todo automáticamente al nivel del jugador?

### D. Autonomía, psicología y sociedad de NPC

22. **Q22 · P1 · PENDIENTE.** ¿Qué rasgos de personalidad deben existir y cómo se representan sin reducir a los NPC a estereotipos?
23. **Q23 · P1 · PENDIENTE.** ¿Qué emociones influyen realmente en las decisiones, cómo se activan y cuánto duran?
24. **Q24 · P1 · PENDIENTE.** ¿Cómo se determina si un acontecimiento es suficientemente relevante para transformar una personalidad, y con qué intensidad?
25. **Q25 · P1 · PENDIENTE.** ¿Cómo se combinan experiencias acumuladas, vínculos y nuevas experiencias para cambios posteriores de personalidad?
26. **Q26 · P1 · PENDIENTE.** ¿Cuánto recuerdan los NPC y cómo gestionan información errónea, rumores, olvidos y confianza en la fuente?
27. **Q27 · P1 · PENDIENTE.** ¿Qué relaciones sociales cambian conducta y qué efectos producen confianza, lealtad, enemistad, prestigio u obligaciones?
28. **Q28 · P0 · PENDIENTE.** ¿Qué necesidades, objetivos y horizontes de planificación dirigirán a los NPC, y qué límites se ponen a decisiones extremas o autodestructivas?

### E. Mundo autónomo, tiempo y causalidad

29. **Q29 · P1 · PENDIENTE.** ¿Cuántos NPC/organizaciones deben simularse con detalle y cómo se resume a los actores distantes para Android?
30. **Q30 · P0 · PARCIALMENTE RESUELTA (2026-11-06).** El mundo avanza durante la partida activa con una **velocidad base fija**, admite acciones con duración propia y puede pausarse por completo. **Confirmado:** 1 minuto real = 1 minuto de juego durante la partida activa sin pausa. **Pendiente:** duración por acción, cadencia de NPC/eventos/economía y manejo de intervalos e interrupciones.
31. **Q31 · P0 · PENDIENTE.** ¿Qué ocurre con la simulación al poner la aplicación en segundo plano o cerrarla? Si se recupera tiempo al volver, ¿qué límites se aplican? **No confundir esta decisión con la pausa manual ya aprobada.**
32. **Q32 · P1 · PENDIENTE.** ¿Cómo se resuelven eventos simultáneos, incompatibles, cancelados o con participantes ausentes?
33. **Q33 · P1 · PENDIENTE.** ¿Qué profundidad tendrán oficios, recursos, precios, comercio, organizaciones y relaciones entre facciones en la primera versión?
34. **Q34 · P1 · PENDIENTE.** ¿Cómo se generan eventos nuevos y qué límites regionales/de intensidad evitan cadenas infinitas o cambios globales injustificados?
35. **Q35 · P1 · PENDIENTE.** ¿Qué puede descubrir cada personaje por presencia, observación, testimonio y rumor, y cómo se refleja la incertidumbre?

### F. Narración y presentación

36. **Q36 · P1 · PENDIENTE.** ¿Qué voz y estilo narrativo se buscan (perspectiva, tono, nivel literario y grado de detalle), manteniendo coherencia factual?
37. **Q37 · P1 · PENDIENTE.** ¿Cuánto texto debe presentar una escena típica y cómo se dosifica entre acciones, decisiones y consecuencias diferidas?
38. **Q38 · P1 · PENDIENTE.** ¿Qué información sobre requisitos, riesgos y opciones bloqueadas es visible al jugador sin revelar secretos?
39. **Q39 · P2 · PENDIENTE.** ¿Cómo se diferencian el Journal general, el historial de Background y objetivos opcionales sin imponer una historia principal?

### G. Implementación, guardado y verificación

40. **Q40 · P0 · PENDIENTE.** ¿Qué plataforma/arquitectura definitiva ejecutará el núcleo JavaScript del prototipo en Android y cómo se integrará la UI?
41. **Q41 · P1 · PENDIENTE.** ¿Cómo serán los slots, autoguardado, recuperación, migraciones y almacenamiento local (o eventual sincronización) de partidas?
42. **Q42 · P1 · PENDIENTE.** ¿Cuál es el dispositivo Android mínimo objetivo y qué presupuestos de rendimiento, memoria, accesibilidad y tamaños de texto debe cumplir?
43. **Q43 · P1 · PENDIENTE.** ¿Qué pruebas y criterios de aceptación deben superar los hitos antes de integrar ramas o declarar un módulo funcional?

## Punto de reanudación

**Ahora:** responder **solo Q01**; guardar la respuesta en este documento o un registro de decisiones y vincularla a `ActionIntent`, `ActionCatalog` y el contrato de UI. Las preguntas Q02–Q43 quedan en cola para cuando el propietario quiera contestarlas.

**Verificación pendiente:** este documento es diseño; no ejecuta las pruebas del gameplay ni prueba funcionamiento Android.
