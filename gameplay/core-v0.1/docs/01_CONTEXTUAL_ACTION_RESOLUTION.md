# Arquitectura propuesta: resolución contextual de acciones

**Estado:** Diseño para revisión, no implementación. **Fecha:** 2026-11-05.  
**Alcance:** RPG narrativo de texto independiente de otros proyectos, sin mapas ni modelos 3D.

## Decisión arquitectónica

Adoptar una solución híbrida: perfiles de acción con reglas configurables + evaluación de los factores relevantes del estado verdadero del mundo. No usar porcentajes inventados por el narrador ni sustituir toda actividad por una tirada. El jugador y los NPC usarán el mismo evaluador de acciones; elegir qué intentar será una responsabilidad distinta.

Flujo de una acción:

1. **Intención:** el jugador selecciona una opción conocida o un NPC elige una intención según objetivos y percepción.
2. **Elegibilidad:** validar requisitos absolutos (conocimiento, acceso, recursos, herramientas o capacidad mínima real). Proponer enfoques alternativos para una acción imposible.
3. **Contexto:** consultar solo factores que corresponden a esa actividad, desde fuentes verificables del mundo.
4. **Resolución:** calcular capacidad, dificultad, riesgos y costos, con incertidumbre limitada solo si procede.
5. **Consecuencias:** aplicar cambios una sola vez, registrar el intento y programar eventos derivados.
6. **Conocimiento y narración:** revelar únicamente los resultados perceptibles o descubiertos por el personaje.

## Componentes y límites

- `ActionCatalog`: perfiles de acción versionados, requisitos, enfoques, factores, grados de resultados y costos.
- `ContextProvider`: extrae una instantánea limitada y reproducible de personaje, mundo y objetivos.
- `ActionResolver`: función pura; verifica elegibilidad y genera una resolución estructurada; no cambia el mundo ni escribe prosa.
- `ConsequenceApplier`: aplica cambios y eventos derivados de manera atómica e idempotente.
- `EventScheduler`: procesa eventos temporales y condicionales aunque el protagonista no intervenga.
- `KnowledgeProjection`: separa verdad del mundo de hechos conocidos por cada personaje.
- `Narrator`: transforma observaciones y consecuencias conocidas en texto coherente, sin establecer reglas.
- `SaveSystem`: versiona reglas y estado, almacena resultados y cualquier estado aleatorio.

## Variables y escalas

Cada variable contextual tendrá: ID semántico, unidad y escala, fuente del valor, ámbito donde es aplicable, duración/caducidad, conocimiento necesario, efecto permitido, límites de acumulación y versión. No aplicar la lluvia a toda conversación, ni la reputación ante una persona a todos los NPC. Evitar contar la fatiga dos veces o tratar datos ausentes como cero por defecto.

**Requisitos duros** son distintos de dificultad: un personaje no puede levantar una carga imposible por obtener un valor aleatorio favorable. Con carreta, aliados o un método distinto se puede abrir otra forma de realizar la actividad.

Un perfil ilustrativo de transporte:

```json
{
  "id": "transport_goods",
  "version": 1,
  "methods": ["manual", "cart", "team"],
  "hard_requirements": ["cargo_exists", "route_accessible"],
  "capacity_terms": [
    {"stat": "strength", "weight": 0.30},
    {"stat": "endurance", "weight": 0.20},
    {"skill": "labor", "weight": 0.50}
  ],
  "context": ["cargo_mass", "weather", "road", "tools", "fatigue", "helpers"],
  "uncertainty": "bounded_if_applicable",
  "possible_results": ["full", "partial", "recoverable_failure", "severe_failure"]
}
```

**Estos pesos son ejemplos, no reglas finales.** Primero definir escalas compatibles y después calibrar pesos y dificultad mediante simulaciones. Algunas acciones serán deterministas; otras tendrán azar limitado. Los resultados propuestos tampoco obligan a que todo intento tenga cuatro grados de desenlace.

Una formulación conceptual sería: `margen = capacidad_normalizada + modificadores_relevantes_acotados - dificultad_contextual`. Los modificadores son auditables, pero la interfaz no recibe factores secretos del mundo.

## Contrato de ejecución y seguridad

Entrada: actor, acción y método, objetivos, versión de reglas, snapshot relevante, semilla/estado RNG si corresponde.

Salida: `attempt_id`, elegibilidad, razones internas, factores usados, grado, costos, efectos propuestos, eventos derivados y registro de conocimiento. Revalidar requisitos al ejecutar, no confiar en un botón habilitado anteriormente. Acciones inválidas no consumen recursos. Los intentos válidos pueden tener costos incluso si fallan, según el perfil.

Guardar resultados y semilla/versiones para impedir que cargar una partida vuelva a tirar o aplique consecuencias duplicadas. Los cambios de formato de partida requieren migraciones y pruebas.

## Estado actual frente a propuesta

**Confirmado en `src/game.mjs`:** `empathy + negotiation >= 7` en mediación y `strength + endurance + labor >= 12` para trasladar suministros. Hay validaciones de disponibilidad, resistencia y eventos del mercado por días; se distingue `worldLedger` del conocimiento visible. La `seed` se almacena pero no se usa para aleatoriedad.

**NO implementado:** ActionCatalog general, ponderación normalizada, ContextProvider formal, ActionResolver reusable, incertidumbre registrada y planificador autónomo de NPC. Los umbrales actuales son demostrativos y no deben reemplazarse sin pruebas de compatibilidad.

## Pruebas de aceptación futuras

Verificar requisitos absolutos, factores irrelevantes, efectos temporales, ausencia de doble cómputo, resultados y costos por grado, límites numéricos, inputs corruptos, reproducibilidad de semilla, idempotencia, guardado/carga y ausencia de filtración de secretos. Migrar primero una única acción y comparar con el comportamiento actual antes de ampliar el catálogo.
