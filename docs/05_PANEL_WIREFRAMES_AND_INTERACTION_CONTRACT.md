# 05. Esquemas por panel y contratos de interacción
**Estado:** wireframes textuales v0.2 · **Fecha:** 2026-11-05  
**Alcance:** estructura funcional y distribución, no arte final ni aplicación implementada.

**Regla común:** aplicar \`docs/04_UI_DESIGN_SYSTEM_AND_RESPONSIVE_LAYOUT.md\`; todas las pantallas comparten cabecera compacta, menú inferior, espaciados, estados y tipografía. Los bloques entre corchetes son componentes, no tamaños fijos.

## W0. Nueva partida — creación de identidad y origen (referencia visual R01)
\`\`\`text
[New Game]                           [Paso 2 de 4]
[Identidad] — datos básicos
[Clase]  Elegida / Elegible / Bloqueada — elegir y revisar
[Background]  Rareza, resumen, condiciones, elegir
[Resumen de combinación y escenario probable]
[Confirmar y comenzar]   (solo si selección válida)
\`\`\`
Crear **antes** de la partida; clase y trasfondo son decisiones iniciales diferenciadas. En **Background**, «Noble Heir» es el nombre de un origen **ilustrativo** y «Epic» es su rareza, no «Noble» como rareza. La confirmación produce una instantánea de elecciones y genera el escenario inicial con reglas/versionado/semilla. Evitar revelar cadenas ocultas. Una clase avanzada bloqueada puede aparecer como informativa, pero no se selecciona sin requisitos; el catálogo concreto está pendiente. Nunca meter todo el formulario, sus rarezas y su historia en dos columnas estrechas.

## W1. Story — pantalla principal (R08)
\`\`\`text
[Contexto pequeño: hora · lugar narrativo · situación]
[Progreso relevante: opcional y compacto]
[ESCENA: título corto]
[NARRACIÓN DE LONGITUD VARIABLE; SCROLL]
[Información conocida / consecuencia reciente]
[Qué haces?] [Opción 1] [Opción 2] [Más acciones…]
[Barra global]
\`\`\`
Prioridad a prosa y elecciones. La historia no avanza exclusivamente por pulsar una opción: los eventos autónomos se ejecutan según reglas del motor, y se muestran al jugador solo cuando los percibe o conoce. Opciones condicionadas explican requisitos conocidos. Cero acciones significa un estado válido («Esperar», «Descansar», o navegación, **solo si** la mecánica existe). Jamás un mapa ni un mundo dibujado.

## W2. Character → Overview (R07)
\`\`\`text
[Character] [pestañas desplazables]
[Identidad: nombre · nivel · clase]
[Condición: HP / MP / stamina / XP; solo lo aplicable]
[Resumen de atributos]             [Ver Stats]
[Equipo actual]                   [Ver Inventory]
[Clase y progreso]                    [Ver Class]
[Estados/efectos activos]
\`\`\`
Priorizar vistazo de 5 segundos. En teléfono: **una columna**, datos pares solo cuando no se aprieten. No duplicar toda la ficha Stats. Si la clase ya se eligió al crear personaje, mostrar clase coherente, no «Unassigned» salvo guardado anterior/estado explícito de error.

## W3. Character → Stats (R06)
\`\`\`text
[Resumen: condición, nivel, experiencia]
[Atributos principales]         (lista ordenada)
[Estadísticas de combate]       (acordeón)
[Resistencias]                  (acordeón)
[Crecimiento y aptitudes]       (acordeón)
[Explicación de puntos disponibles, si aplica]
\`\`\`
Separar **atributo base**, **derivado** y **modificadores**; no juntar números de distinto origen sin unidades. No afirmar que todos los personajes usan exactamente los valores de las imágenes. Botones +/− solo si existe asignación de puntos; de lo contrario, valores de solo lectura. En 320–479 dp prohibida tabla apretada de dos columnas.

## W4. Character → Skills (R05; imagen previa X01)
\`\`\`text
[Resumen de puntos de habilidad, si se implementan]
[Categorías de habilidades]      (chips con scroll o selector)
[Lista de skills: nombre · nivel · progreso · estado]
[Detalle de skill seleccionada]
[Requisitos] [Efecto actual] [Próximo nivel]
[Acción: mejorar / bloqueado / sin puntos]
\`\`\`
**Skills** son competencias entrenables y su dominio (combate, oficio, supervivencia, etc. como ejemplos, no lista confirmada). Si hay un árbol de especializaciones de Skills, se abre como detalle con alternativa en lista; no es el mismo árbol de Abilities. La vieja composición de dos columnas siempre abiertas se adapta a categorías → lista → detalle. La asignación de SP, costes y reset sigue **pendiente de reglas**, nunca se establece por una cifra dibujada.

## W5. Character → Abilities (R03 vigente; R04 legado)
\`\`\`text
[Clase actual / requisito de clase, si está bloqueada]
[Ability Proficiency]              (categorías de dominio)
[Ability Tree] [rama/filtrar] [vista árbol ↔ vista lista]
  [Nodos por nivel y prerequisitos]
  [Ramas cerradas con candado y condición explicada]
[Detalle de nodo: descripción · requisito · efecto · costo]
[Desbloquear / Requisito pendiente]
\`\`\`
Nomenclatura **obligatoria**: «Ability Proficiency», NO «Ability Sets»; «Ability Tree», NO «Combat Ability». El árbol tiene ramas, nodos, prerequisitos, conexiones, inversión de puntos y cambios de disponibilidad; **sin cooldowns** en ningún nodo ni detalle. Ramas bloqueadas mientras la clase requerida no esté desbloqueada o no se cumplan sus condiciones; la UI diferencia visualmente visible/bloqueado/oculto. Progresión compleja sin convertirla en un diagrama ilegible a 320 dp: usar vista lista jerárquica cuando el lienzo sea difícil de leer. No suponer que el jugador nace sin clase si la escogió antes de iniciar.

## W6. Character → Class (R02)
\`\`\`text
[Clase actual · nivel/progreso · estado]
[Descripción corta / especialidad]
[Clases conocidas, elegibles y bloqueadas]
[Requisitos del cambio/desbloqueo]
[Beneficios e influencia sobre Ability Tree]
[Acción válida: consultar / seleccionar / desbloquear]
\`\`\`
En **Nueva partida** se escoge clase inicial. En juego, el panel consulta y administra progresión y eventuales nuevas clases (desbloqueo/reglas pendientes). El «Class Ability Tree» decorativo de la imagen no crea un árbol paralelo contradictorio: enlaza al **Ability Tree** único con el filtro de clase. Si no está permitido cambiar clase, nunca presentar un botón funcional de cambio.

## W7. Character → Background (estado posterior a crear; derivado de R01)
\`\`\`text
[Origen seleccionado · rareza]
[Hechos establecidos · familia/región/circunstancias]
[Rasgos o vínculos conocidos]
[Background History Log]   (cronología legible)
  [fecha] [acontecimiento] [fuente/descubrimiento]
  [fecha] [consecuencia relacionada]
[Ver detalles del evento]
\`\`\`
La pantalla **permanece** después de comenzar. Origen inmutable, historial append-only (nuevos eventos no reescriben el pasado), distinción entre hecho real y conocimiento del personaje. No reabrir «Select Background» desde el juego. No duplicar el Journal general, que incluye sucesos conocidos no ligados al origen.

## W8. Inventory, Journal y More (derivados del shell; sin imagen aprobada)
\`\`\`text
[Inventory] [Lista de objetos] [Detalle / usar si permitido]
[Journal] [Eventos conocidos] [Pendientes] [Cronología]
[More] [Ajustes de lectura] [Ayuda] [Guardar/Cargar]
\`\`\`
**Propuesta**, no decisión visual cerrada. Mantenerlos sobrios hasta recibir referencia. Cualquier menú «World» de capturas históricas se retira si implica mapa.

## Interacciones y transiciones comunes
1. Cada acción se define por identificador y requisitos; el motor valida al ejecutarla.
2. UI muestra **consecuencias conocidas**, no el estado oculto del mundo.
3. Story y Journal son visiones diferentes del mismo registro; Background filtra por procedencia.
4. Al regresar a un panel se recuperan filtro, desplazamiento razonable y selección, sin aplicar acciones otra vez.
5. Cuando una clase no está disponible, el árbol muestra bloqueos y requisitos sin inventar temporizadores.
6. Los títulos, números y habilidades dibujados en referencias NO son contenido canon ni reglas de balance.

## Matriz de aceptación por pantalla — pendiente de ejecución
- W0: impide iniciar sin clase/background válidos; origen guardado y visible.
- W1: escena y acciones permanecen legibles con 0/12 opciones y fuente 200%.
- W2: información general sin duplicación extensa de Stats.
- W3: números/unidades correctos, sin columnas forzadas ni botones ficticios.
- W4: cambia categoría y detalle sin perder selección; estados bloqueados explicados.
- W5: árbol y lista concuerdan; ramas bloqueadas correctamente; **cero cooldowns**.
- W6: clase seleccionada en creación coincide con clase actual y con desbloqueos.
- W7: origen inmutable y eventos históricos ordenados; secretos no filtrados.
- W8: sin contenido cartográfico y sin duplicar funciones globales.
**No son pruebas ejecutadas.**
