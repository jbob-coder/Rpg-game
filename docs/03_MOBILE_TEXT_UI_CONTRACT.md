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
