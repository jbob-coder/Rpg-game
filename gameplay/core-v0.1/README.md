# RPG de texto — primera base de gameplay (NO canon)

Esto es una **prueba vertical de dominio narrativo** independiente del motor de interfaz. No es un APK, ni reemplaza la documentación/maqueta del PR #1. Todo nombre, stat, umbral, día y conflicto de mercado es **contenido ilustrativo**, pendiente de aprobación. No hay mapa ni modelos.

## Qué funciona

- Creación con clase y background elegidos antes de empezar. El background conserva su rareza y hechos fundacionales.
- Atributos medibles que cambian resultados: empatía + negociación para mediar; fuerza + aguante + trabajo para descargar suministros. La resistencia cuesta recursos y el descanso recupera energía.
- Un conflicto comercial transcurre por sí mismo los días 2, 4 y 6. Puede terminar en acuerdo, abastecimiento o cierre parcial; afecta precios después. No espera a que el jugador abra una misión.
- Un registro de **verdad del mundo** separado del historial de lo que sabe el jugador. Una visita descubre hechos sin reescribir eventos.
- Guardado y carga JSON con versión y comprobaciones iniciales de consistencia. Actualización del estado mediante comandos; la UI solo recibe un ViewModel, nunca flags secretos.
- Narrativa en español basada en contexto y consecuencias comprobables, no un párrafo generado al azar que decide las reglas del juego.

## Cómo ejecutarlo (Node.js >=20, sin dependencias)

```bash
npm test
npm run demo
```

Ejemplo: comenzar con Guardia y Familia artesana, avanzar al día 2, visitar el mercado, transportar suministros y esperar hasta el día 6. En una partida sin intervención, los comerciantes restringen las descargas y los precios suben. Elegir Escribiente/Heredero noble ofrece una ruta de mediación distinta. Son rutas de demostración, no una historia principal obligatoria.

## Contrato con el frontend

`createGame({name,classId,backgroundId,seed})` crea una partida después de validar opciones. `getViewModel(state)` entrega solo stats, narrativa, historial conocido y elecciones disponibles. `dispatch(state,{type})` valida y devuelve estado nuevo. `saveGame(state)` y `loadGame(json)` sirven para persistencia en almacenamiento definido por la plataforma. El frontend que aparece en `design/ui/` podrá consumir este adaptador en una etapa futura; no se conectó aquí.

La narración **nunca debe adelantarse** al conocimiento del personaje: los sucesos ocultos existen en `worldLedger`, pero solo llegan a texto/journal tras ser descubiertos. Los resultados no se aplican desde los botones ni desde frases narrativas.

## Lo que falta

Balance definitivo y nombres canon; clases/rareza/currículos de origen aprobados; sistema completo Stats/Skills/Abilities/Ability Tree y combate; simulación de NPC en múltiples regiones; contenido narrativo más variado; localización, UI real y pruebas Android. El atributo `seed` queda reservado en esta versión, **no genera variaciones aleatorias**.

Este módulo tiene un ejemplo determinista, no un narrador general ni un mundo completo. Los test de Node validan ese alcance y no deben interpretarse como tests de APK.

## Arquitectura futura, documentada y no implementada

- [Resolución contextual de acciones](docs/01_CONTEXTUAL_ACTION_RESOLUTION.md): perfiles, reglas, requisitos y factores.
- [NPC autónomos y narración causal](docs/02_NPC_WORLD_NARRATION.md): decidir, resolver, aplicar y narrar.
- [Estado y próximos hitos](docs/03_STATUS_AND_NEXT_MILESTONES.md): continuidad y verificación para la siguiente sesión.

Los ejemplos de cifras no son balance aprobado. No se ha modificado el motor actual en esta etapa documental.
