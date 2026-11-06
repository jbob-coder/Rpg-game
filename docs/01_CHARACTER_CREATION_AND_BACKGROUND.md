# 01. Creación inicial, clase y Background

**Estado:** especificación de diseño v0.1 · **Fecha:** 2026-11-05
**Alcance:** RPG independiente, exclusivamente de texto, sin mapa.

## 1. Propósito

La elección inicial define **quién es el personaje y en qué circunstancias comienza**, no toda la narración futura. Después, la historia emerge de decisiones, eventos programados, iniciativas de NPC y organizaciones, oportunidades y consecuencias. El mundo conserva autonomía.

## 2. Flujo de partida nueva

1. **Nueva partida** → abrir creador de personaje antes del mundo.
2. **Identidad** → nombre y atributos iniciales permitidos por diseño (lista aún por decidir).
3. **Class** → elegir entre opciones disponibles; mostrar descripción, enfoque y estado de desbloqueo.
4. **Background** → elegir origen/trasfondo con sus rasgos, rareza, circunstancias y relaciones iniciales.
5. **Resumen y confirmación** → exponer consecuencias conocidas sin revelar acontecimientos futuros.
6. **Generación del escenario inicial** → evaluar reglas de compatibilidad, contexto y semilla de partida; determinar punto de partida narrativo, relaciones y primeros eventos latentes.
7. **Comienzo de la partida** → abrir vista de historia, crear historial inicial y activar simulación de eventos.

Ninguna selección debe crear automáticamente una cadena principal obligatoria o un relato cerrado.

## 3. Responsabilidades separadas

- **Class:** describe rol, progresión, requisitos y acceso a habilidades/ramas de habilidades; se conserva su panel Character → Class.
- **Background:** historia previa, circunstancias sociales, vínculos, predisposiciones y oportunidades contextuales; se conserva Character → Background como **consulta e historial**, no como selector que reinicia la historia.
- **Scenario generator:** interpreta Class + Background + contexto + reglas para proponer un comienzo coherente. Debe admitir varias semillas/resultados válidos por combinación.
- **World event engine:** produce acontecimientos y cambios con o sin intervención del jugador. No debe depender de que el jugador abra el panel de historia.

Las habilidades de ramas pueden permanecer bloqueadas hasta que se cumpla el desbloqueo de clase/requisitos. **Pendiente:** precisar si toda clase se elige y queda desbloqueada al inicio o si ciertas clases requieren descubrimiento/desbloqueo. No inventar reglas ni umbrales.

## 4. Rareza de Background

La rareza pertenece a la **categoría del trasfondo**, no se confunde con posición social, clase de combate ni poder garantizado. Ejemplo ilustrativo: `Noble Heir` con rareza `Epic` en lugar de etiquetar `Noble` como rareza. Las demás categorías y probabilidades aún requieren decisión.

## 5. Persistencia y carácter inmutable

Guardar una instantánea versionada del origen elegido en la confirmación inicial:
- `character_id`, `class_id`, `background_id`, `background_rarity`
- `background_facts` (hechos fundacionales), `starting_relationships` y `starting_conditions`
- `creation_rules_version`, `world_seed`, `initial_scenario_id`

Los hechos fundacionales no se sustituyen retroactivamente mediante la UI. Cambios de reputación, alianzas, clase futura o situación familiar se guardan como **acontecimientos nuevos**. Si una revelación altera la interpretación del pasado, agregar un hecho de revelación; no borrar el hecho registrado.

**Background History Log** (solo lectura): entradas ordenadas con `event_id`, tiempo de juego, breve descripción, fuente/descubrimiento, relación con el background, visibilidad y consecuencias conocidas. Distinguir hechos que ocurrieron de lo que el personaje sabe.

## 6. Ejemplo exclusivamente ilustrativo

Un personaje selecciona una clase marcial y un trasfondo **Epic** ligado a una familia influyente. La partida puede abrir en una residencia, en una visita obligatoria o en una situación de desplazamiento, dependiendo de reglas y semilla. Una disputa entre organizaciones puede seguir evolucionando mientras el jugador estudia o viaja. Intervenir, traicionar, no hacer nada o llegar tarde conducen a desenlaces diferentes; no se necesita activar manualmente la disputa.

Este ejemplo **no establece nombres ni canon del juego**.

## 7. Criterios de aceptación

- No se entra a la historia antes de confirmar Class y Background válidos.
- El mismo conjunto de elecciones produce escenarios coherentes y reproducibles con la misma semilla y versión de reglas.
- Class y Background permanecen consultables durante la partida; Background no permite rehacer el pasado.
- Cambios posteriores se registran sin mutar elecciones históricas.
- La creación del personaje nunca es requisito para que un evento mundial espere una acción específica del jugador: una vez iniciada la partida, eventos autónomos pueden continuar.

## 8. Pendientes de decisión

Lista de clases, requisitos y clases bloqueadas; opciones de origen; categorías de rareza; posibilidad de reentrenamiento; efectos de las selecciones sobre atributos; política de revelaciones de información; reglas exactas de generación y su balance.
