# 02. Mundo autónomo, eventos encadenados y múltiples desenlaces

**Estado:** especificación de arquitectura v0.1 · **Fecha:** 2026-11-05
**Objetivo:** que el mundo narrativo se transforme aunque el jugador no actúe.

## 1. Principios confirmados

1. **Autonomía:** NPC, grupos y facciones pueden perseguir objetivos y generar sucesos.
2. **Tiempo:** algunos cambios empiezan o vencen en fechas del reloj de juego.
3. **Causalidad:** sucesos crean condiciones que hacen posibles, desvían o impiden otros sucesos.
4. **Elecciones con impacto:** intervenir puede ayudar, perjudicar, retrasar o transformar una cadena.
5. **No participación:** ignorar un evento es un camino válido con resultados propios; el mundo no se congela.
6. **Persistencia:** efectos sobre relaciones, disponibilidad, recursos y estado social sobreviven a guardar/cargar.
7. **Información limitada:** un evento puede ocurrir sin ser anunciado; el jugador puede conocerlo por observación, conversación o noticias textuales posteriores.

No hay mapas, sistemas de terreno ni representación visual del mundo. La localización narrativa es un atributo de contexto (`location_id` / `region_tag`), no una coordenada de navegación.

## 2. Entidades de diseño propuestas

- **WorldState:** `game_time`, `seed`, `world_flags`, estados agregados de organizaciones/personajes y recursos necesarios.
- **EventDefinition** (contenido estático, versionado): `event_id`, `scope`, `trigger`, `preconditions`, `deadline`, `priority`, `participants`, `possible_outcomes`, `followups`, `visibility_rule`.
- **EventInstance** (estado vivo): ID único, definición, `scheduled_at`, estado, participante, decisiones relevantes y `resolved_outcome_id`.
- **Consequence:** cambio de mundo con identificador idempotente, aplicación temporal/inmediata, hechos que habilita o invalida.
- **EventLedger:** registro append-only de sucesos reales, consecuencias, descubrimientos del jugador y versión de reglas; con filtro de Background cuando se relacionen con el origen.
- **KnowledgeState:** qué conoce el jugador frente a qué ocurrió realmente.

Los nombres de campos son **propuestas**, no APIs implementadas.

## 3. Ciclo de vida

`DORMANT → SCHEDULED → ACTIVE → RESOLVED`, con salidas a `CANCELLED` y `EXPIRED` según condiciones. Cada transición debe tener reglas claras; **RESOLVED** no vuelve a aplicar consecuencias tras recargar.

El reloj de juego y eventos pendientes se persisten. Un avance de tiempo procesa los sucesos vencidos en orden determinista (fecha + prioridad + ID). Cada evento reevalúa precondiciones; el motor elige un resultado válido según estado y acciones observadas; aplica consecuencias una sola vez; programa seguimientos; añade entradas al ledger; actualiza el conocimiento del jugador solo si corresponde.

## 4. Ejemplo de cadena (no canon)

**Día 1:** dos grupos compiten por una ruta comercial (evento activo por conflictos y recursos, no por visita del jugador).

**Día 3:** representantes negocian. La negociación ocurre independientemente del jugador.

**Posibles resultados:**
- El jugador media y se satisfacen condiciones → acuerdo temporal, mejores relaciones con ambas partes.
- El jugador favorece a un grupo → gana acceso especial, pero deteriora una relación rival.
- El jugador sabotea una reunión → se abre investigación y una cadena posterior de persecución.
- El jugador ignora todo → otros actores resuelven o escalan el conflicto según su fuerza, intereses y recursos.

**Día 10:** el resultado cambia precios, oportunidades o alianzas. Si el jugador regresa, puede descubrir las consecuencias. No se muestra un aviso universal antes del descubrimiento.

La secuencia no es un árbol de diálogo rígido: fechas, objetivos, decisiones y precondiciones pueden reencaminar la cadena.

## 5. Reglas para consecuencias diferidas

Cada consecuencia pendiente incluye condición/fecha de ejecución, acción correctiva posible, expiración, alcance y causa. Si la cadena cambia, se cancela o transforma explícitamente la consecuencia anterior y se registra la razón. Evitar activar resultados incompatibles simultáneamente.

Los eventos de gran impacto deben tener controles de coherencia y límites de intensidad; un evento menor no debe producir cambios globales arbitrarios.

## 6. Autonomía eficiente en Android

No simular cada segundo de cada NPC fuera de la escena narrativa. Usar una **simulación agregada y discreta** de organizaciones/personajes relevantes; avanzar por lotes cuando el reloj de juego progresa y materializar solo el detalle necesario para texto, decisiones o consecuencias.

- Presupuesto de eventos procesados por actualización y cola persistente para trabajo pendiente.
- Idempotencia para evitar duplicaciones después de interrupción/guardado.
- Orden estable y semilla persistente para reproducibilidad.
- Registro compacto y snapshots para guardar/cargar sin reconstruir todo el historial a cada acción.
- No inventar progresión real fuera de sesión: **pendiente de decisión** si el mundo avanza con la aplicación cerrada.

## 7. Separación entre estado real y texto mostrado

Una narración es una **vista del estado**, no la fuente de verdad. El motor produce resultados estructurados y luego genera/despliega el texto apropiado. Evitar que el texto mostrado altere estados por accidente. La UI puede ocultar sucesos no conocidos mientras sus consecuencias físicas/sociales ya existen.

## 8. Pruebas de aceptación futuras (no ejecutadas)

- **Sin participación:** avanzar diez días de juego; una cadena alcanza un estado válido sin interacción del jugador.
- **Ramificación:** misma semilla/estado inicial con dos decisiones distintas lleva a resultados distintos, sin estados imposibles.
- **Repetibilidad:** misma semilla, versión y secuencia de acciones producen el mismo ledger y estado final.
- **Guardado/carga:** evento vencido no se aplica dos veces y las consecuencias pendientes permanecen.
- **Conocimiento:** eventos ocultos no aparecen en el historial visible hasta descubrirse, pero sus efectos existen.
- **Cambio de condiciones:** si un NPC crucial desaparece, la cadena se cancela, redirige o resuelve por fallback documentado.
- **Rendimiento móvil:** se mide y limita el coste de procesar eventos; cifras objetivo pendientes de decidir.

## 9. Decisiones abiertas

Cadencia y reglas del tiempo; avance fuera de sesión; número inicial de organizaciones; escalas de simulación; algoritmo de ponderación de resultados; política de eventos simultáneos; límites de cambios globales; contenido de las primeras cadenas; condiciones de visibilidad.
