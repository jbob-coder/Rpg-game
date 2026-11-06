# 06 — Inventario de preguntas de diseño pendientes (para responder gradualmente)

**Estado:** backlog de decisiones **abiertas**, no soluciones aprobadas. **Fecha:** 2026-11-06.
**Repo:** `jbob-coder/Rpg-game`, rama `work/text-rpg-narrative-core-v01`, PR #2 (borrador).
**Alcance:** RPG independiente exclusivamente de texto; sintetiza preguntas derivadas de los docs 01–05 de gameplay y los docs 01–03 de diseño del PR #1. Es el listado completo de decisiones abiertas **identificadas en esta auditoría**; podrán aparecer otras al implementar.

## Uso del listado

- **P0** = decisión de alto impacto o que desbloquea contratos; **P1** = importante, pero puede decidirse más adelante; **P2** = puede posponerse.
- Todas las preguntas empiezan con estado **PENDIENTE**; no implican que haya que contestarlas ahora. Al recibir respuesta, registrar decisión, fecha, justificación, consecuencias para código y pruebas, y actualizar estado.
- **Primera pregunta recomendada: Q01.** La modalidad de entrada define el contrato de `ActionIntent`, la UI, el parser opcional, la disponibilidad de acciones y cómo el juego comunica sus límites. El motor híbrido reglas+contexto acordado **no** determina si el usuario escribe texto libre.
- No modificar el motor ni aprobar pesos, escalas o canon por redactar preguntas.

## Decisiones del propietario ya acordadas (NO volver a preguntar)

- RPG narrativo de texto independiente, sin mapas ni modelos 3D.
- Class y Background se eligen al crear el personaje; el Background permanece consultable sin reescribir el pasado.
- Mundo causal con eventos que pueden ocurrir sin intervención del jugador; narración limitada al conocimiento del personaje.
- Resolución híbrida: perfiles de reglas, requisitos físicos/lógicos, factores contextuales y azar opcional; resultados con consecuencias; NPC comparten evaluador pero tienen planificador separado.
- Los NPC pueden elegir acciones poco convenientes por personalidad, emociones, relaciones, experiencias y conocimiento limitado.
- Las emociones fluctúan con lo cotidiano; sucesos especialmente significativos pueden cambiar rasgos de personalidad; esos rasgos pueden volver a cambiar con experiencias futuras, no son permanentemente fijos.
- Skills y Ability Tree son conceptos distintos; Abilities sin cooldowns; la UI del PR #1 no está integrada al motor del PR #2.
- Actualmente el reloj avanza por comandos `wait` o `rest` y eventos fijos; no existe avance verificado con app cerrada ni planificador NPC implementado.

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

## Preguntas abiertas priorizadas

### A. Interacción y experiencia del jugador

01. **Q01 · P0 · PENDIENTE.** ¿Cómo introduce el jugador las acciones: opciones contextuales, texto libre o una combinación de ambas?
02. **Q02 · P0 · PENDIENTE.** Si acepta texto libre, ¿qué debe pasar cuando la intención es ambigua, imposible o todavía no existe una acción compatible en el catálogo?
03. **Q03 · P1 · PENDIENTE.** ¿Puede encadenar planes de varios pasos o debe confirmar cada acción antes de ejecutarla?
04. **Q04 · P0 · PENDIENTE.** ¿Qué tiempo de juego consumen acciones, desplazamientos, descanso y lectura de menús?
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
30. **Q30 · P0 · PENDIENTE.** ¿Cuál es la escala temporal del mundo y con qué frecuencia se actualizan agentes, eventos y economía?
31. **Q31 · P0 · PENDIENTE.** ¿El mundo avanza con la aplicación cerrada o solo durante una partida activa? Si hay recuperación temporal, ¿con qué límites?
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
