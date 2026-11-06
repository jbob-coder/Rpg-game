# RPG de texto para móvil — Base de diseño

**Estado:** documentación de diseño, sin motor de juego implementado.
**Proyecto:** independiente de otros juegos y repositorios.
**Plataforma objetivo:** Android, interfaz adaptable en orientación vertical.

## Identidad del proyecto

RPG basado en texto y decisiones, con creación inicial de personaje y un mundo narrativo que evoluciona por procesos propios. La historia **no depende exclusivamente** de que el jugador active eventos o participe en ellos. Los personajes, organizaciones, el tiempo y las cadenas causales pueden cambiar las circunstancias sin su intervención.

**Restricción explícita:** no se diseñan ni implementan mapas, minimapas, terrenos 2D/3D, modelos de personajes o representaciones visuales del mundo. Las ubicaciones, cuando existan, son identificadores y descripciones narrativas, no coordenadas ni superficies cartográficas. No reutilizar lore, nombres, escenas ni mecánicas de otros proyectos sin decisión explícita del propietario.

## Documentos

1. [Creación de personaje, clase y background](docs/01_CHARACTER_CREATION_AND_BACKGROUND.md) — decisiones iniciales, generación del comienzo y registro histórico.
2. [Mundo autónomo y motor de eventos](docs/02_AUTONOMOUS_WORLD_AND_EVENT_CHAINS.md) — eventos temporizados y condicionales, cadenas narrativas, desenlaces, persistencia y pruebas de diseño.
3. [Contrato de interfaz móvil y criterios de validación](docs/03_MOBILE_TEXT_UI_CONTRACT.md) — experiencia Android de solo texto, navegación, accesibilidad y verificación.

## Acuerdos confirmados al 2026-11-05

- El jugador selecciona clase y background **antes** de empezar la partida; esas elecciones condicionan el escenario inicial.
- El panel **Background** permanece accesible en Character durante el juego. Incluye origen y un historial cronológico de eventos relacionados; el origen establecido no se reescribe a voluntad.
- El panel **Class** permanece para consultar su estado y progresión.
- Los eventos ocurren por tiempo, condiciones, acciones de terceros o cadenas causales, incluso cuando el jugador los ignora.
- El jugador puede intervenir, desviarlos o descubrir consecuencias después, pero no controla todo el mundo.
- La interfaz es solo texto y no incorpora mapa.

**No confirmado:** nombres definitivos, clases y backgrounds concretos, lista de rarezas completa, método exacto de desbloqueo de clases, ritmo de reloj y avance fuera de sesión. Se etiquetan como decisiones pendientes en los documentos.

## Estado de implementación

Este commit solo incorpora documentos Markdown. No se han creado juego, APK, motor de eventos, pruebas ejecutables ni pruebas en dispositivo. Cualquier ejemplo de historia es ilustrativo y no canon.
