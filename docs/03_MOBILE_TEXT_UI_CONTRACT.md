# 03. UI móvil de texto y contrato de validación

**Estado:** propuesta de interfaz v0.1 · **Fecha:** 2026-11-05

## Identidad visual y límites

Android en retrato, texto legible, interacción táctil, diseño adaptativo. La pantalla prioriza lectura y decisiones. **Prohibidos:** mapas/minimapas, ilustraciones del escenario, modelos de personaje, terreno o interfaces heredadas de otros proyectos. Un encabezado y elementos funcionales de texto pueden usar jerarquía tipográfica y contraste, sin convertirse en un panel de estadísticas que desplace la historia.

## Navegación propuesta

- **Story:** prosa actual, consecuencias que el jugador conoce y **opciones contextuales seleccionables exclusivamente**. El jugador **no escribe acciones** ni existe caja de comandos libres (decisión del propietario, 2026-11-06).
- **Character → Class:** estado y progresión de clase, requisitos, ramas/habilidades bloqueadas según reglas pendientes.
- **Character → Background:** origen confirmado, rareza y hechos fundacionales, registro cronológico de eventos relacionados. Consultable, no editable retroactivamente.
- **Character → Stats / Skills:** datos de atributos y habilidades, separados de la narración habitual.
- **Inventory / Journal:** objetos, objetivos opcionales, eventos conocidos y registros consultables.

Estas pestañas son propuesta funcional, no pantallas implementadas. La prioridad es reducir navegación excesiva en teléfonos pequeños.

## Control de pausa del tiempo (decisión del propietario, 2026-11-06)

La futura interfaz debe ofrecer **Pausar / Reanudar** en un lugar accesible. Con la partida activa, el mundo continúa avanzando aunque el jugador esté leyendo y no pulse ninguna opción; al pausar se detienen reloj, eventos y decisiones temporizadas de NPC. Los paneles de lectura, estadísticas e historial siguen siendo consultables. La UI envía un comando de pausa al dominio; **no detiene ni avanza el reloj por su cuenta**. **Decisión confirmada (2026-11-06):** no se permite ejecutar acciones que alteren la partida mientras está pausada; el progreso de acciones ya iniciadas también se congela. Las opciones de jugabilidad deben quedar inactivas hasta que el usuario pulse **Reanudar** explícitamente. No se suman minutos transcurridos durante la pausa al volver a jugar. La política para app cerrada/segundo plano y la escala temporal todavía no se han aprobado. Esta sección es una **especificación**, no una función implementada.

**Prueba futura:** mientras Pausa esté activa, leer y navegar sin que avancen reloj, progreso de acciones, NPC ni sucesos; intentar seleccionar acciones no debe producir efectos; Reanudar continúa desde el instante exacto.

## Reloj combinado y acciones con duración (decisión del propietario, 2026-11-06)

La partida utiliza un reloj continuo de velocidad base fija mientras está activa y sin pausa. Algunas elecciones representan actividades que consumen tiempo de juego —por ejemplo viajar, trabajar o descansar—, y sus duraciones se aplican al **mismo reloj** que gobierna NPC y acontecimientos, sin duplicar el tiempo transcurrido. El dominio es responsable de calcular/procesar el tiempo; la UI solo muestra el estado, las elecciones y el control de Pausa/Reanudar. **Velocidad base aprobada: 1 minuto real = 1 minuto de juego (1:1)** cuando la partida está activa y sin pausa, incluso durante la lectura. Al pausar, el reloj y toda acción en curso se congelan por completo; al reanudar no se recupera tiempo pausado. Las duraciones concretas de cada acción y la política de segundo plano/app cerrada todavía no están definidas. **Especificación futura, no funcionalidad implementada.**

## Proporciones adaptativas

Usar el alto disponible después de barras del sistema, teclado y áreas seguras; narrativa desplazable con mayor espacio posible. Opciones en un área inferior que se adapte al número de acciones y pueda colapsarse sin perder acceso. No fijar porcentajes universales ni cajas altas que impidan leer en teléfonos pequeños. Evitar desplazamiento horizontal.

Requisitos de diseño sugeridos: zonas táctiles de al menos 48 dp, texto escalable, alto contraste, longitud de línea cómoda, indicadores no dependientes de color, foco y navegación accesible. Son objetivos de diseño, **no resultados de pruebas**.

## Estados y respuesta al usuario

Una acción envía una decisión identificada al motor, que valida condiciones y actualiza estado del mundo, reloj y ledger; la UI muestra el desenlace conocido y opciones nuevas. No fabricar decisiones disponibles si están bloqueadas, caducadas o sus precondiciones dejaron de existir.

El jugador puede leer rumores o el historial para descubrir eventos que ocurrieron sin su intervención. El Background History Log filtra por relevancia al origen; el Journal general no debe mezclar hechos secretos con hechos descubiertos.

## Verificación futura (no ejecutada)

Probar tamaños estrechos y altos, cambio de tamaño de fuente, teclado abierto, pantallas largas, opciones abundantes, cero opciones, estados de bloqueo, guardado/carga, interrupción de app y navegación atrás. Revisar que nunca se genere un mapa ni una ilustración por dependencia accidental.

## Pendientes

Motor/plataforma final, estructura de menú definitiva, políticas de selección/confirmación de opciones contextuales, accesibilidad, localización de idiomas y benchmarks en hardware Android.

## Guía oficial de consistencia (adenda v0.2)
La especificación concreta y los esquemas por pantalla se encuentran en:
- [04. Sistema visual y proporciones responsivas](04_UI_DESIGN_SYSTEM_AND_RESPONSIVE_LAYOUT.md)
- [05. Wireframes y contratos de interacción](05_PANEL_WIREFRAMES_AND_INTERACTION_CONTRACT.md)
- [06. Registro de las ocho referencias y conflictos resueltos](06_UI_REFERENCE_REGISTER_AND_INCONSISTENCIES.md)

Las ocho imágenes son referencias visuales principales, **no una fuente de verdad mecánica**. Los documentos 04–06 prevalecen ante defectos de espacio, tipografía o nomenclatura de una imagen. No confundir el árbol de habilidades de clase con Skills, ni incluir cooldowns, ni agregar mapa.
