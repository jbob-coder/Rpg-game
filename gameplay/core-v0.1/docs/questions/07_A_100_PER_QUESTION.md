# Banco de subpreguntas — A. Interacción y experiencia del jugador

**Estado:** Q01 resuelta en su modalidad de interacción; los demás detalles y Q02–Q05 siguen pendientes, salvo decisiones registradas expresamente. **Fecha:** 2026-11-06.
**Origen:** [Q01–Q43, inventario principal](../06_OPEN_DESIGN_QUESTIONS_BACKLOG.md). Cada pregunta principal se desglosa en exactamente 100 subpreguntas de análisis funcional.
**Rango:** Q01–Q05.

La lista es una herramienta para aclarar funciones del código, no un requisito de contestar todo ahora. Los números concretos del motor siguen sin aprobarse.

## Q01 · P0 — Acciones mediante opciones contextuales seleccionables: elección confirmada

**Decisión del propietario: RESUELTA el 2026-11-06.** El jugador elige exclusivamente opciones que el juego presenta. No puede escribir acciones. Las 100 preguntas siguientes cubren el comportamiento detallado pendiente, sin reconsiderar texto libre.

### Subtema 1: presentación de opciones en cada escena

- **Q01.001** ¿Qué situación de juego debería activar «presentación de opciones en cada escena»?
- **Q01.002** ¿Qué datos del mundo y del personaje necesita «presentación de opciones en cada escena»?
- **Q01.003** ¿Qué acción o elección seleccionable representa «presentación de opciones en cada escena» en el ViewModel?
- **Q01.004** ¿Qué información puede mostrarse en «presentación de opciones en cada escena» sin revelar hechos desconocidos?
- **Q01.005** ¿Qué requisito debe revalidar el dominio al ejecutar «presentación de opciones en cada escena»?
- **Q01.006** ¿Cómo debe verse o funcionar «presentación de opciones en cada escena» en una pantalla Android pequeña?
- **Q01.007** ¿Qué sucede con «presentación de opciones en cada escena» cuando cambian los recursos, la ubicación o el tiempo?
- **Q01.008** ¿Qué respuesta debe ofrecer la interfaz si el jugador cancela o no usa «presentación de opciones en cada escena»?
- **Q01.009** ¿Qué estado de «presentación de opciones en cada escena» conviene persistir y qué parte debe reconstruirse al cargar?
- **Q01.010** ¿Qué prueba automatizada y qué caso táctil verificarían «presentación de opciones en cada escena»?

### Subtema 2: identificadores estables de cada elección

- **Q01.011** ¿Qué situación de juego debería activar «identificadores estables de cada elección»?
- **Q01.012** ¿Qué datos del mundo y del personaje necesita «identificadores estables de cada elección»?
- **Q01.013** ¿Qué acción o elección seleccionable representa «identificadores estables de cada elección» en el ViewModel?
- **Q01.014** ¿Qué información puede mostrarse en «identificadores estables de cada elección» sin revelar hechos desconocidos?
- **Q01.015** ¿Qué requisito debe revalidar el dominio al ejecutar «identificadores estables de cada elección»?
- **Q01.016** ¿Cómo debe verse o funcionar «identificadores estables de cada elección» en una pantalla Android pequeña?
- **Q01.017** ¿Qué sucede con «identificadores estables de cada elección» cuando cambian los recursos, la ubicación o el tiempo?
- **Q01.018** ¿Qué respuesta debe ofrecer la interfaz si el jugador cancela o no usa «identificadores estables de cada elección»?
- **Q01.019** ¿Qué estado de «identificadores estables de cada elección» conviene persistir y qué parte debe reconstruirse al cargar?
- **Q01.020** ¿Qué prueba automatizada y qué caso táctil verificarían «identificadores estables de cada elección»?

### Subtema 3: acciones disponibles según conocimiento y contexto

- **Q01.021** ¿Qué situación de juego debería activar «acciones disponibles según conocimiento y contexto»?
- **Q01.022** ¿Qué datos del mundo y del personaje necesita «acciones disponibles según conocimiento y contexto»?
- **Q01.023** ¿Qué acción o elección seleccionable representa «acciones disponibles según conocimiento y contexto» en el ViewModel?
- **Q01.024** ¿Qué información puede mostrarse en «acciones disponibles según conocimiento y contexto» sin revelar hechos desconocidos?
- **Q01.025** ¿Qué requisito debe revalidar el dominio al ejecutar «acciones disponibles según conocimiento y contexto»?
- **Q01.026** ¿Cómo debe verse o funcionar «acciones disponibles según conocimiento y contexto» en una pantalla Android pequeña?
- **Q01.027** ¿Qué sucede con «acciones disponibles según conocimiento y contexto» cuando cambian los recursos, la ubicación o el tiempo?
- **Q01.028** ¿Qué respuesta debe ofrecer la interfaz si el jugador cancela o no usa «acciones disponibles según conocimiento y contexto»?
- **Q01.029** ¿Qué estado de «acciones disponibles según conocimiento y contexto» conviene persistir y qué parte debe reconstruirse al cargar?
- **Q01.030** ¿Qué prueba automatizada y qué caso táctil verificarían «acciones disponibles según conocimiento y contexto»?

### Subtema 4: requisitos conocidos y estados deshabilitados

- **Q01.031** ¿Qué situación de juego debería activar «requisitos conocidos y estados deshabilitados»?
- **Q01.032** ¿Qué datos del mundo y del personaje necesita «requisitos conocidos y estados deshabilitados»?
- **Q01.033** ¿Qué acción o elección seleccionable representa «requisitos conocidos y estados deshabilitados» en el ViewModel?
- **Q01.034** ¿Qué información puede mostrarse en «requisitos conocidos y estados deshabilitados» sin revelar hechos desconocidos?
- **Q01.035** ¿Qué requisito debe revalidar el dominio al ejecutar «requisitos conocidos y estados deshabilitados»?
- **Q01.036** ¿Cómo debe verse o funcionar «requisitos conocidos y estados deshabilitados» en una pantalla Android pequeña?
- **Q01.037** ¿Qué sucede con «requisitos conocidos y estados deshabilitados» cuando cambian los recursos, la ubicación o el tiempo?
- **Q01.038** ¿Qué respuesta debe ofrecer la interfaz si el jugador cancela o no usa «requisitos conocidos y estados deshabilitados»?
- **Q01.039** ¿Qué estado de «requisitos conocidos y estados deshabilitados» conviene persistir y qué parte debe reconstruirse al cargar?
- **Q01.040** ¿Qué prueba automatizada y qué caso táctil verificarían «requisitos conocidos y estados deshabilitados»?

### Subtema 5: opciones descubiertas por habilidades y relaciones

- **Q01.041** ¿Qué situación de juego debería activar «opciones descubiertas por habilidades y relaciones»?
- **Q01.042** ¿Qué datos del mundo y del personaje necesita «opciones descubiertas por habilidades y relaciones»?
- **Q01.043** ¿Qué acción o elección seleccionable representa «opciones descubiertas por habilidades y relaciones» en el ViewModel?
- **Q01.044** ¿Qué información puede mostrarse en «opciones descubiertas por habilidades y relaciones» sin revelar hechos desconocidos?
- **Q01.045** ¿Qué requisito debe revalidar el dominio al ejecutar «opciones descubiertas por habilidades y relaciones»?
- **Q01.046** ¿Cómo debe verse o funcionar «opciones descubiertas por habilidades y relaciones» en una pantalla Android pequeña?
- **Q01.047** ¿Qué sucede con «opciones descubiertas por habilidades y relaciones» cuando cambian los recursos, la ubicación o el tiempo?
- **Q01.048** ¿Qué respuesta debe ofrecer la interfaz si el jugador cancela o no usa «opciones descubiertas por habilidades y relaciones»?
- **Q01.049** ¿Qué estado de «opciones descubiertas por habilidades y relaciones» conviene persistir y qué parte debe reconstruirse al cargar?
- **Q01.050** ¿Qué prueba automatizada y qué caso táctil verificarían «opciones descubiertas por habilidades y relaciones»?

### Subtema 6: agrupación de numerosas alternativas en Android

- **Q01.051** ¿Qué situación de juego debería activar «agrupación de numerosas alternativas en Android»?
- **Q01.052** ¿Qué datos del mundo y del personaje necesita «agrupación de numerosas alternativas en Android»?
- **Q01.053** ¿Qué acción o elección seleccionable representa «agrupación de numerosas alternativas en Android» en el ViewModel?
- **Q01.054** ¿Qué información puede mostrarse en «agrupación de numerosas alternativas en Android» sin revelar hechos desconocidos?
- **Q01.055** ¿Qué requisito debe revalidar el dominio al ejecutar «agrupación de numerosas alternativas en Android»?
- **Q01.056** ¿Cómo debe verse o funcionar «agrupación de numerosas alternativas en Android» en una pantalla Android pequeña?
- **Q01.057** ¿Qué sucede con «agrupación de numerosas alternativas en Android» cuando cambian los recursos, la ubicación o el tiempo?
- **Q01.058** ¿Qué respuesta debe ofrecer la interfaz si el jugador cancela o no usa «agrupación de numerosas alternativas en Android»?
- **Q01.059** ¿Qué estado de «agrupación de numerosas alternativas en Android» conviene persistir y qué parte debe reconstruirse al cargar?
- **Q01.060** ¿Qué prueba automatizada y qué caso táctil verificarían «agrupación de numerosas alternativas en Android»?

### Subtema 7: elección de objetivos cuando hay varios

- **Q01.061** ¿Qué situación de juego debería activar «elección de objetivos cuando hay varios»?
- **Q01.062** ¿Qué datos del mundo y del personaje necesita «elección de objetivos cuando hay varios»?
- **Q01.063** ¿Qué acción o elección seleccionable representa «elección de objetivos cuando hay varios» en el ViewModel?
- **Q01.064** ¿Qué información puede mostrarse en «elección de objetivos cuando hay varios» sin revelar hechos desconocidos?
- **Q01.065** ¿Qué requisito debe revalidar el dominio al ejecutar «elección de objetivos cuando hay varios»?
- **Q01.066** ¿Cómo debe verse o funcionar «elección de objetivos cuando hay varios» en una pantalla Android pequeña?
- **Q01.067** ¿Qué sucede con «elección de objetivos cuando hay varios» cuando cambian los recursos, la ubicación o el tiempo?
- **Q01.068** ¿Qué respuesta debe ofrecer la interfaz si el jugador cancela o no usa «elección de objetivos cuando hay varios»?
- **Q01.069** ¿Qué estado de «elección de objetivos cuando hay varios» conviene persistir y qué parte debe reconstruirse al cargar?
- **Q01.070** ¿Qué prueba automatizada y qué caso táctil verificarían «elección de objetivos cuando hay varios»?

### Subtema 8: accesibilidad y controles táctiles

- **Q01.071** ¿Qué situación de juego debería activar «accesibilidad y controles táctiles»?
- **Q01.072** ¿Qué datos del mundo y del personaje necesita «accesibilidad y controles táctiles»?
- **Q01.073** ¿Qué acción o elección seleccionable representa «accesibilidad y controles táctiles» en el ViewModel?
- **Q01.074** ¿Qué información puede mostrarse en «accesibilidad y controles táctiles» sin revelar hechos desconocidos?
- **Q01.075** ¿Qué requisito debe revalidar el dominio al ejecutar «accesibilidad y controles táctiles»?
- **Q01.076** ¿Cómo debe verse o funcionar «accesibilidad y controles táctiles» en una pantalla Android pequeña?
- **Q01.077** ¿Qué sucede con «accesibilidad y controles táctiles» cuando cambian los recursos, la ubicación o el tiempo?
- **Q01.078** ¿Qué respuesta debe ofrecer la interfaz si el jugador cancela o no usa «accesibilidad y controles táctiles»?
- **Q01.079** ¿Qué estado de «accesibilidad y controles táctiles» conviene persistir y qué parte debe reconstruirse al cargar?
- **Q01.080** ¿Qué prueba automatizada y qué caso táctil verificarían «accesibilidad y controles táctiles»?

### Subtema 9: confirmación de decisiones irreversibles o peligrosas

- **Q01.081** ¿Qué situación de juego debería activar «confirmación de decisiones irreversibles o peligrosas»?
- **Q01.082** ¿Qué datos del mundo y del personaje necesita «confirmación de decisiones irreversibles o peligrosas»?
- **Q01.083** ¿Qué acción o elección seleccionable representa «confirmación de decisiones irreversibles o peligrosas» en el ViewModel?
- **Q01.084** ¿Qué información puede mostrarse en «confirmación de decisiones irreversibles o peligrosas» sin revelar hechos desconocidos?
- **Q01.085** ¿Qué requisito debe revalidar el dominio al ejecutar «confirmación de decisiones irreversibles o peligrosas»?
- **Q01.086** ¿Cómo debe verse o funcionar «confirmación de decisiones irreversibles o peligrosas» en una pantalla Android pequeña?
- **Q01.087** ¿Qué sucede con «confirmación de decisiones irreversibles o peligrosas» cuando cambian los recursos, la ubicación o el tiempo?
- **Q01.088** ¿Qué respuesta debe ofrecer la interfaz si el jugador cancela o no usa «confirmación de decisiones irreversibles o peligrosas»?
- **Q01.089** ¿Qué estado de «confirmación de decisiones irreversibles o peligrosas» conviene persistir y qué parte debe reconstruirse al cargar?
- **Q01.090** ¿Qué prueba automatizada y qué caso táctil verificarían «confirmación de decisiones irreversibles o peligrosas»?

### Subtema 10: actualización de opciones al cambiar el estado del mundo

- **Q01.091** ¿Qué situación de juego debería activar «actualización de opciones al cambiar el estado del mundo»?
- **Q01.092** ¿Qué datos del mundo y del personaje necesita «actualización de opciones al cambiar el estado del mundo»?
- **Q01.093** ¿Qué acción o elección seleccionable representa «actualización de opciones al cambiar el estado del mundo» en el ViewModel?
- **Q01.094** ¿Qué información puede mostrarse en «actualización de opciones al cambiar el estado del mundo» sin revelar hechos desconocidos?
- **Q01.095** ¿Qué requisito debe revalidar el dominio al ejecutar «actualización de opciones al cambiar el estado del mundo»?
- **Q01.096** ¿Cómo debe verse o funcionar «actualización de opciones al cambiar el estado del mundo» en una pantalla Android pequeña?
- **Q01.097** ¿Qué sucede con «actualización de opciones al cambiar el estado del mundo» cuando cambian los recursos, la ubicación o el tiempo?
- **Q01.098** ¿Qué respuesta debe ofrecer la interfaz si el jugador cancela o no usa «actualización de opciones al cambiar el estado del mundo»?
- **Q01.099** ¿Qué estado de «actualización de opciones al cambiar el estado del mundo» conviene persistir y qué parte debe reconstruirse al cargar?
- **Q01.100** ¿Qué prueba automatizada y qué caso táctil verificarían «actualización de opciones al cambiar el estado del mundo»?

## Q02 · P0 — Opciones que se vuelven inválidas antes de la selección

**Estado: PENDIENTE.** Gestión de opciones rechazadas o desactualizadas; las 100 preguntas siguientes son especificaciones por decidir.

### Subtema 1: opción caducada por avance de tiempo

- **Q02.001** ¿Cómo detecta el dominio que «opción caducada por avance de tiempo» invalida una opción antes ofrecida?
- **Q02.002** ¿Qué requisito concreto debe volver a evaluarse en «opción caducada por avance de tiempo» al pulsar?
- **Q02.003** ¿El rechazo por «opción caducada por avance de tiempo» debe consumir tiempo o recursos? ¿Por qué?
- **Q02.004** ¿Qué debe ocurrir si «opción caducada por avance de tiempo» se descubre antes de aplicar una consecuencia?
- **Q02.005** ¿Qué mensaje puede explicar «opción caducada por avance de tiempo» sin revelar datos ocultos?
- **Q02.006** ¿Cómo se evita que «opción caducada por avance de tiempo» cause costos o efectos duplicados?
- **Q02.007** ¿Qué cambios en las opciones visibles deben producirse después de «opción caducada por avance de tiempo»?
- **Q02.008** ¿Qué información de «opción caducada por avance de tiempo» debe registrarse para diagnosticar un fallo sin exponer secretos?
- **Q02.009** ¿Cómo deben comportarse guardar, cargar y reintentar cuando se produce «opción caducada por avance de tiempo»?
- **Q02.010** ¿Qué prueba de concurrencia o de estado obsoleto demostraría manejo correcto de «opción caducada por avance de tiempo»?

### Subtema 2: recursos insuficientes al pulsar

- **Q02.011** ¿Cómo detecta el dominio que «recursos insuficientes al pulsar» invalida una opción antes ofrecida?
- **Q02.012** ¿Qué requisito concreto debe volver a evaluarse en «recursos insuficientes al pulsar» al pulsar?
- **Q02.013** ¿El rechazo por «recursos insuficientes al pulsar» debe consumir tiempo o recursos? ¿Por qué?
- **Q02.014** ¿Qué debe ocurrir si «recursos insuficientes al pulsar» se descubre antes de aplicar una consecuencia?
- **Q02.015** ¿Qué mensaje puede explicar «recursos insuficientes al pulsar» sin revelar datos ocultos?
- **Q02.016** ¿Cómo se evita que «recursos insuficientes al pulsar» cause costos o efectos duplicados?
- **Q02.017** ¿Qué cambios en las opciones visibles deben producirse después de «recursos insuficientes al pulsar»?
- **Q02.018** ¿Qué información de «recursos insuficientes al pulsar» debe registrarse para diagnosticar un fallo sin exponer secretos?
- **Q02.019** ¿Cómo deben comportarse guardar, cargar y reintentar cuando se produce «recursos insuficientes al pulsar»?
- **Q02.020** ¿Qué prueba de concurrencia o de estado obsoleto demostraría manejo correcto de «recursos insuficientes al pulsar»?

### Subtema 3: objetivo que cambió o desapareció

- **Q02.021** ¿Cómo detecta el dominio que «objetivo que cambió o desapareció» invalida una opción antes ofrecida?
- **Q02.022** ¿Qué requisito concreto debe volver a evaluarse en «objetivo que cambió o desapareció» al pulsar?
- **Q02.023** ¿El rechazo por «objetivo que cambió o desapareció» debe consumir tiempo o recursos? ¿Por qué?
- **Q02.024** ¿Qué debe ocurrir si «objetivo que cambió o desapareció» se descubre antes de aplicar una consecuencia?
- **Q02.025** ¿Qué mensaje puede explicar «objetivo que cambió o desapareció» sin revelar datos ocultos?
- **Q02.026** ¿Cómo se evita que «objetivo que cambió o desapareció» cause costos o efectos duplicados?
- **Q02.027** ¿Qué cambios en las opciones visibles deben producirse después de «objetivo que cambió o desapareció»?
- **Q02.028** ¿Qué información de «objetivo que cambió o desapareció» debe registrarse para diagnosticar un fallo sin exponer secretos?
- **Q02.029** ¿Cómo deben comportarse guardar, cargar y reintentar cuando se produce «objetivo que cambió o desapareció»?
- **Q02.030** ¿Qué prueba de concurrencia o de estado obsoleto demostraría manejo correcto de «objetivo que cambió o desapareció»?

### Subtema 4: ubicación o acceso que ya no es válido

- **Q02.031** ¿Cómo detecta el dominio que «ubicación o acceso que ya no es válido» invalida una opción antes ofrecida?
- **Q02.032** ¿Qué requisito concreto debe volver a evaluarse en «ubicación o acceso que ya no es válido» al pulsar?
- **Q02.033** ¿El rechazo por «ubicación o acceso que ya no es válido» debe consumir tiempo o recursos? ¿Por qué?
- **Q02.034** ¿Qué debe ocurrir si «ubicación o acceso que ya no es válido» se descubre antes de aplicar una consecuencia?
- **Q02.035** ¿Qué mensaje puede explicar «ubicación o acceso que ya no es válido» sin revelar datos ocultos?
- **Q02.036** ¿Cómo se evita que «ubicación o acceso que ya no es válido» cause costos o efectos duplicados?
- **Q02.037** ¿Qué cambios en las opciones visibles deben producirse después de «ubicación o acceso que ya no es válido»?
- **Q02.038** ¿Qué información de «ubicación o acceso que ya no es válido» debe registrarse para diagnosticar un fallo sin exponer secretos?
- **Q02.039** ¿Cómo deben comportarse guardar, cargar y reintentar cuando se produce «ubicación o acceso que ya no es válido»?
- **Q02.040** ¿Qué prueba de concurrencia o de estado obsoleto demostraría manejo correcto de «ubicación o acceso que ya no es válido»?

### Subtema 5: conocimiento del jugador desactualizado

- **Q02.041** ¿Cómo detecta el dominio que «conocimiento del jugador desactualizado» invalida una opción antes ofrecida?
- **Q02.042** ¿Qué requisito concreto debe volver a evaluarse en «conocimiento del jugador desactualizado» al pulsar?
- **Q02.043** ¿El rechazo por «conocimiento del jugador desactualizado» debe consumir tiempo o recursos? ¿Por qué?
- **Q02.044** ¿Qué debe ocurrir si «conocimiento del jugador desactualizado» se descubre antes de aplicar una consecuencia?
- **Q02.045** ¿Qué mensaje puede explicar «conocimiento del jugador desactualizado» sin revelar datos ocultos?
- **Q02.046** ¿Cómo se evita que «conocimiento del jugador desactualizado» cause costos o efectos duplicados?
- **Q02.047** ¿Qué cambios en las opciones visibles deben producirse después de «conocimiento del jugador desactualizado»?
- **Q02.048** ¿Qué información de «conocimiento del jugador desactualizado» debe registrarse para diagnosticar un fallo sin exponer secretos?
- **Q02.049** ¿Cómo deben comportarse guardar, cargar y reintentar cuando se produce «conocimiento del jugador desactualizado»?
- **Q02.050** ¿Qué prueba de concurrencia o de estado obsoleto demostraría manejo correcto de «conocimiento del jugador desactualizado»?

### Subtema 6: conflicto por cambios simultáneos en el mundo

- **Q02.051** ¿Cómo detecta el dominio que «conflicto por cambios simultáneos en el mundo» invalida una opción antes ofrecida?
- **Q02.052** ¿Qué requisito concreto debe volver a evaluarse en «conflicto por cambios simultáneos en el mundo» al pulsar?
- **Q02.053** ¿El rechazo por «conflicto por cambios simultáneos en el mundo» debe consumir tiempo o recursos? ¿Por qué?
- **Q02.054** ¿Qué debe ocurrir si «conflicto por cambios simultáneos en el mundo» se descubre antes de aplicar una consecuencia?
- **Q02.055** ¿Qué mensaje puede explicar «conflicto por cambios simultáneos en el mundo» sin revelar datos ocultos?
- **Q02.056** ¿Cómo se evita que «conflicto por cambios simultáneos en el mundo» cause costos o efectos duplicados?
- **Q02.057** ¿Qué cambios en las opciones visibles deben producirse después de «conflicto por cambios simultáneos en el mundo»?
- **Q02.058** ¿Qué información de «conflicto por cambios simultáneos en el mundo» debe registrarse para diagnosticar un fallo sin exponer secretos?
- **Q02.059** ¿Cómo deben comportarse guardar, cargar y reintentar cuando se produce «conflicto por cambios simultáneos en el mundo»?
- **Q02.060** ¿Qué prueba de concurrencia o de estado obsoleto demostraría manejo correcto de «conflicto por cambios simultáneos en el mundo»?

### Subtema 7: doble pulsación y envío duplicado

- **Q02.061** ¿Cómo detecta el dominio que «doble pulsación y envío duplicado» invalida una opción antes ofrecida?
- **Q02.062** ¿Qué requisito concreto debe volver a evaluarse en «doble pulsación y envío duplicado» al pulsar?
- **Q02.063** ¿El rechazo por «doble pulsación y envío duplicado» debe consumir tiempo o recursos? ¿Por qué?
- **Q02.064** ¿Qué debe ocurrir si «doble pulsación y envío duplicado» se descubre antes de aplicar una consecuencia?
- **Q02.065** ¿Qué mensaje puede explicar «doble pulsación y envío duplicado» sin revelar datos ocultos?
- **Q02.066** ¿Cómo se evita que «doble pulsación y envío duplicado» cause costos o efectos duplicados?
- **Q02.067** ¿Qué cambios en las opciones visibles deben producirse después de «doble pulsación y envío duplicado»?
- **Q02.068** ¿Qué información de «doble pulsación y envío duplicado» debe registrarse para diagnosticar un fallo sin exponer secretos?
- **Q02.069** ¿Cómo deben comportarse guardar, cargar y reintentar cuando se produce «doble pulsación y envío duplicado»?
- **Q02.070** ¿Qué prueba de concurrencia o de estado obsoleto demostraría manejo correcto de «doble pulsación y envío duplicado»?

### Subtema 8: errores de sincronización entre UI y dominio

- **Q02.071** ¿Cómo detecta el dominio que «errores de sincronización entre UI y dominio» invalida una opción antes ofrecida?
- **Q02.072** ¿Qué requisito concreto debe volver a evaluarse en «errores de sincronización entre UI y dominio» al pulsar?
- **Q02.073** ¿El rechazo por «errores de sincronización entre UI y dominio» debe consumir tiempo o recursos? ¿Por qué?
- **Q02.074** ¿Qué debe ocurrir si «errores de sincronización entre UI y dominio» se descubre antes de aplicar una consecuencia?
- **Q02.075** ¿Qué mensaje puede explicar «errores de sincronización entre UI y dominio» sin revelar datos ocultos?
- **Q02.076** ¿Cómo se evita que «errores de sincronización entre UI y dominio» cause costos o efectos duplicados?
- **Q02.077** ¿Qué cambios en las opciones visibles deben producirse después de «errores de sincronización entre UI y dominio»?
- **Q02.078** ¿Qué información de «errores de sincronización entre UI y dominio» debe registrarse para diagnosticar un fallo sin exponer secretos?
- **Q02.079** ¿Cómo deben comportarse guardar, cargar y reintentar cuando se produce «errores de sincronización entre UI y dominio»?
- **Q02.080** ¿Qué prueba de concurrencia o de estado obsoleto demostraría manejo correcto de «errores de sincronización entre UI y dominio»?

### Subtema 9: mensaje seguro ante rechazo de la acción

- **Q02.081** ¿Cómo detecta el dominio que «mensaje seguro ante rechazo de la acción» invalida una opción antes ofrecida?
- **Q02.082** ¿Qué requisito concreto debe volver a evaluarse en «mensaje seguro ante rechazo de la acción» al pulsar?
- **Q02.083** ¿El rechazo por «mensaje seguro ante rechazo de la acción» debe consumir tiempo o recursos? ¿Por qué?
- **Q02.084** ¿Qué debe ocurrir si «mensaje seguro ante rechazo de la acción» se descubre antes de aplicar una consecuencia?
- **Q02.085** ¿Qué mensaje puede explicar «mensaje seguro ante rechazo de la acción» sin revelar datos ocultos?
- **Q02.086** ¿Cómo se evita que «mensaje seguro ante rechazo de la acción» cause costos o efectos duplicados?
- **Q02.087** ¿Qué cambios en las opciones visibles deben producirse después de «mensaje seguro ante rechazo de la acción»?
- **Q02.088** ¿Qué información de «mensaje seguro ante rechazo de la acción» debe registrarse para diagnosticar un fallo sin exponer secretos?
- **Q02.089** ¿Cómo deben comportarse guardar, cargar y reintentar cuando se produce «mensaje seguro ante rechazo de la acción»?
- **Q02.090** ¿Qué prueba de concurrencia o de estado obsoleto demostraría manejo correcto de «mensaje seguro ante rechazo de la acción»?

### Subtema 10: recuperación y nueva lista de opciones

- **Q02.091** ¿Cómo detecta el dominio que «recuperación y nueva lista de opciones» invalida una opción antes ofrecida?
- **Q02.092** ¿Qué requisito concreto debe volver a evaluarse en «recuperación y nueva lista de opciones» al pulsar?
- **Q02.093** ¿El rechazo por «recuperación y nueva lista de opciones» debe consumir tiempo o recursos? ¿Por qué?
- **Q02.094** ¿Qué debe ocurrir si «recuperación y nueva lista de opciones» se descubre antes de aplicar una consecuencia?
- **Q02.095** ¿Qué mensaje puede explicar «recuperación y nueva lista de opciones» sin revelar datos ocultos?
- **Q02.096** ¿Cómo se evita que «recuperación y nueva lista de opciones» cause costos o efectos duplicados?
- **Q02.097** ¿Qué cambios en las opciones visibles deben producirse después de «recuperación y nueva lista de opciones»?
- **Q02.098** ¿Qué información de «recuperación y nueva lista de opciones» debe registrarse para diagnosticar un fallo sin exponer secretos?
- **Q02.099** ¿Cómo deben comportarse guardar, cargar y reintentar cuando se produce «recuperación y nueva lista de opciones»?
- **Q02.100** ¿Qué prueba de concurrencia o de estado obsoleto demostraría manejo correcto de «recuperación y nueva lista de opciones»?

## Q03 · P1 — ¿Puede encadenar planes de varios pasos o debe confirmar cada acción antes de ejecutarla?

### Subtema 1: planes de varias actividades

- **Q03.001** ¿Qué experiencia concreta debe ofrecer «planes de varias actividades» al jugador durante una partida normal?
- **Q03.002** ¿Qué situación narrativa justificaría que el juego permita «planes de varias actividades»?
- **Q03.003** ¿Qué requisitos de estado deben comprobarse antes de habilitar «planes de varias actividades»?
- **Q03.004** ¿Qué información debe conocer el jugador antes de usar «planes de varias actividades»?
- **Q03.005** ¿Qué hechos ocultos no debe revelar el diseño de «planes de varias actividades»?
- **Q03.006** ¿Qué alternativas o rutas de interacción debe ofrecer «planes de varias actividades» en Android pequeño?
- **Q03.007** ¿Cómo afecta «planes de varias actividades» al reloj, los recursos o los eventos del mundo?
- **Q03.008** ¿Qué corrección o cancelación debería existir cuando «planes de varias actividades» se utiliza por error?
- **Q03.009** ¿Qué estado relacionado con «planes de varias actividades» debe sobrevivir al guardado y a la carga?
- **Q03.010** ¿Qué prueba reproducible demostraría que «planes de varias actividades» funciona y no confunde al jugador?

### Subtema 2: confirmación de cada paso

- **Q03.011** ¿Qué experiencia concreta debe ofrecer «confirmación de cada paso» al jugador durante una partida normal?
- **Q03.012** ¿Qué situación narrativa justificaría que el juego permita «confirmación de cada paso»?
- **Q03.013** ¿Qué requisitos de estado deben comprobarse antes de habilitar «confirmación de cada paso»?
- **Q03.014** ¿Qué información debe conocer el jugador antes de usar «confirmación de cada paso»?
- **Q03.015** ¿Qué hechos ocultos no debe revelar el diseño de «confirmación de cada paso»?
- **Q03.016** ¿Qué alternativas o rutas de interacción debe ofrecer «confirmación de cada paso» en Android pequeño?
- **Q03.017** ¿Cómo afecta «confirmación de cada paso» al reloj, los recursos o los eventos del mundo?
- **Q03.018** ¿Qué corrección o cancelación debería existir cuando «confirmación de cada paso» se utiliza por error?
- **Q03.019** ¿Qué estado relacionado con «confirmación de cada paso» debe sobrevivir al guardado y a la carga?
- **Q03.020** ¿Qué prueba reproducible demostraría que «confirmación de cada paso» funciona y no confunde al jugador?

### Subtema 3: interrupciones externas

- **Q03.021** ¿Qué experiencia concreta debe ofrecer «interrupciones externas» al jugador durante una partida normal?
- **Q03.022** ¿Qué situación narrativa justificaría que el juego permita «interrupciones externas»?
- **Q03.023** ¿Qué requisitos de estado deben comprobarse antes de habilitar «interrupciones externas»?
- **Q03.024** ¿Qué información debe conocer el jugador antes de usar «interrupciones externas»?
- **Q03.025** ¿Qué hechos ocultos no debe revelar el diseño de «interrupciones externas»?
- **Q03.026** ¿Qué alternativas o rutas de interacción debe ofrecer «interrupciones externas» en Android pequeño?
- **Q03.027** ¿Cómo afecta «interrupciones externas» al reloj, los recursos o los eventos del mundo?
- **Q03.028** ¿Qué corrección o cancelación debería existir cuando «interrupciones externas» se utiliza por error?
- **Q03.029** ¿Qué estado relacionado con «interrupciones externas» debe sobrevivir al guardado y a la carga?
- **Q03.030** ¿Qué prueba reproducible demostraría que «interrupciones externas» funciona y no confunde al jugador?

### Subtema 4: dependencias entre tareas

- **Q03.031** ¿Qué experiencia concreta debe ofrecer «dependencias entre tareas» al jugador durante una partida normal?
- **Q03.032** ¿Qué situación narrativa justificaría que el juego permita «dependencias entre tareas»?
- **Q03.033** ¿Qué requisitos de estado deben comprobarse antes de habilitar «dependencias entre tareas»?
- **Q03.034** ¿Qué información debe conocer el jugador antes de usar «dependencias entre tareas»?
- **Q03.035** ¿Qué hechos ocultos no debe revelar el diseño de «dependencias entre tareas»?
- **Q03.036** ¿Qué alternativas o rutas de interacción debe ofrecer «dependencias entre tareas» en Android pequeño?
- **Q03.037** ¿Cómo afecta «dependencias entre tareas» al reloj, los recursos o los eventos del mundo?
- **Q03.038** ¿Qué corrección o cancelación debería existir cuando «dependencias entre tareas» se utiliza por error?
- **Q03.039** ¿Qué estado relacionado con «dependencias entre tareas» debe sobrevivir al guardado y a la carga?
- **Q03.040** ¿Qué prueba reproducible demostraría que «dependencias entre tareas» funciona y no confunde al jugador?

### Subtema 5: reordenación de pasos

- **Q03.041** ¿Qué experiencia concreta debe ofrecer «reordenación de pasos» al jugador durante una partida normal?
- **Q03.042** ¿Qué situación narrativa justificaría que el juego permita «reordenación de pasos»?
- **Q03.043** ¿Qué requisitos de estado deben comprobarse antes de habilitar «reordenación de pasos»?
- **Q03.044** ¿Qué información debe conocer el jugador antes de usar «reordenación de pasos»?
- **Q03.045** ¿Qué hechos ocultos no debe revelar el diseño de «reordenación de pasos»?
- **Q03.046** ¿Qué alternativas o rutas de interacción debe ofrecer «reordenación de pasos» en Android pequeño?
- **Q03.047** ¿Cómo afecta «reordenación de pasos» al reloj, los recursos o los eventos del mundo?
- **Q03.048** ¿Qué corrección o cancelación debería existir cuando «reordenación de pasos» se utiliza por error?
- **Q03.049** ¿Qué estado relacionado con «reordenación de pasos» debe sobrevivir al guardado y a la carga?
- **Q03.050** ¿Qué prueba reproducible demostraría que «reordenación de pasos» funciona y no confunde al jugador?

### Subtema 6: cancelación voluntaria

- **Q03.051** ¿Qué experiencia concreta debe ofrecer «cancelación voluntaria» al jugador durante una partida normal?
- **Q03.052** ¿Qué situación narrativa justificaría que el juego permita «cancelación voluntaria»?
- **Q03.053** ¿Qué requisitos de estado deben comprobarse antes de habilitar «cancelación voluntaria»?
- **Q03.054** ¿Qué información debe conocer el jugador antes de usar «cancelación voluntaria»?
- **Q03.055** ¿Qué hechos ocultos no debe revelar el diseño de «cancelación voluntaria»?
- **Q03.056** ¿Qué alternativas o rutas de interacción debe ofrecer «cancelación voluntaria» en Android pequeño?
- **Q03.057** ¿Cómo afecta «cancelación voluntaria» al reloj, los recursos o los eventos del mundo?
- **Q03.058** ¿Qué corrección o cancelación debería existir cuando «cancelación voluntaria» se utiliza por error?
- **Q03.059** ¿Qué estado relacionado con «cancelación voluntaria» debe sobrevivir al guardado y a la carga?
- **Q03.060** ¿Qué prueba reproducible demostraría que «cancelación voluntaria» funciona y no confunde al jugador?

### Subtema 7: costos futuros previstos

- **Q03.061** ¿Qué experiencia concreta debe ofrecer «costos futuros previstos» al jugador durante una partida normal?
- **Q03.062** ¿Qué situación narrativa justificaría que el juego permita «costos futuros previstos»?
- **Q03.063** ¿Qué requisitos de estado deben comprobarse antes de habilitar «costos futuros previstos»?
- **Q03.064** ¿Qué información debe conocer el jugador antes de usar «costos futuros previstos»?
- **Q03.065** ¿Qué hechos ocultos no debe revelar el diseño de «costos futuros previstos»?
- **Q03.066** ¿Qué alternativas o rutas de interacción debe ofrecer «costos futuros previstos» en Android pequeño?
- **Q03.067** ¿Cómo afecta «costos futuros previstos» al reloj, los recursos o los eventos del mundo?
- **Q03.068** ¿Qué corrección o cancelación debería existir cuando «costos futuros previstos» se utiliza por error?
- **Q03.069** ¿Qué estado relacionado con «costos futuros previstos» debe sobrevivir al guardado y a la carga?
- **Q03.070** ¿Qué prueba reproducible demostraría que «costos futuros previstos» funciona y no confunde al jugador?

### Subtema 8: planes compartidos con NPC

- **Q03.071** ¿Qué experiencia concreta debe ofrecer «planes compartidos con NPC» al jugador durante una partida normal?
- **Q03.072** ¿Qué situación narrativa justificaría que el juego permita «planes compartidos con NPC»?
- **Q03.073** ¿Qué requisitos de estado deben comprobarse antes de habilitar «planes compartidos con NPC»?
- **Q03.074** ¿Qué información debe conocer el jugador antes de usar «planes compartidos con NPC»?
- **Q03.075** ¿Qué hechos ocultos no debe revelar el diseño de «planes compartidos con NPC»?
- **Q03.076** ¿Qué alternativas o rutas de interacción debe ofrecer «planes compartidos con NPC» en Android pequeño?
- **Q03.077** ¿Cómo afecta «planes compartidos con NPC» al reloj, los recursos o los eventos del mundo?
- **Q03.078** ¿Qué corrección o cancelación debería existir cuando «planes compartidos con NPC» se utiliza por error?
- **Q03.079** ¿Qué estado relacionado con «planes compartidos con NPC» debe sobrevivir al guardado y a la carga?
- **Q03.080** ¿Qué prueba reproducible demostraría que «planes compartidos con NPC» funciona y no confunde al jugador?

### Subtema 9: fallos a mitad del plan

- **Q03.081** ¿Qué experiencia concreta debe ofrecer «fallos a mitad del plan» al jugador durante una partida normal?
- **Q03.082** ¿Qué situación narrativa justificaría que el juego permita «fallos a mitad del plan»?
- **Q03.083** ¿Qué requisitos de estado deben comprobarse antes de habilitar «fallos a mitad del plan»?
- **Q03.084** ¿Qué información debe conocer el jugador antes de usar «fallos a mitad del plan»?
- **Q03.085** ¿Qué hechos ocultos no debe revelar el diseño de «fallos a mitad del plan»?
- **Q03.086** ¿Qué alternativas o rutas de interacción debe ofrecer «fallos a mitad del plan» en Android pequeño?
- **Q03.087** ¿Cómo afecta «fallos a mitad del plan» al reloj, los recursos o los eventos del mundo?
- **Q03.088** ¿Qué corrección o cancelación debería existir cuando «fallos a mitad del plan» se utiliza por error?
- **Q03.089** ¿Qué estado relacionado con «fallos a mitad del plan» debe sobrevivir al guardado y a la carga?
- **Q03.090** ¿Qué prueba reproducible demostraría que «fallos a mitad del plan» funciona y no confunde al jugador?

### Subtema 10: visualización del progreso

- **Q03.091** ¿Qué experiencia concreta debe ofrecer «visualización del progreso» al jugador durante una partida normal?
- **Q03.092** ¿Qué situación narrativa justificaría que el juego permita «visualización del progreso»?
- **Q03.093** ¿Qué requisitos de estado deben comprobarse antes de habilitar «visualización del progreso»?
- **Q03.094** ¿Qué información debe conocer el jugador antes de usar «visualización del progreso»?
- **Q03.095** ¿Qué hechos ocultos no debe revelar el diseño de «visualización del progreso»?
- **Q03.096** ¿Qué alternativas o rutas de interacción debe ofrecer «visualización del progreso» en Android pequeño?
- **Q03.097** ¿Cómo afecta «visualización del progreso» al reloj, los recursos o los eventos del mundo?
- **Q03.098** ¿Qué corrección o cancelación debería existir cuando «visualización del progreso» se utiliza por error?
- **Q03.099** ¿Qué estado relacionado con «visualización del progreso» debe sobrevivir al guardado y a la carga?
- **Q03.100** ¿Qué prueba reproducible demostraría que «visualización del progreso» funciona y no confunde al jugador?

## Q04 · P0 — ¿Qué tiempo de juego consumen acciones, desplazamientos, descanso y lectura de menús?

### Subtema 1: duración de actividades físicas

- **Q04.001** ¿Qué experiencia concreta debe ofrecer «duración de actividades físicas» al jugador durante una partida normal?
- **Q04.002** ¿Qué situación narrativa justificaría que el juego permita «duración de actividades físicas»?
- **Q04.003** ¿Qué requisitos de estado deben comprobarse antes de habilitar «duración de actividades físicas»?
- **Q04.004** ¿Qué información debe conocer el jugador antes de usar «duración de actividades físicas»?
- **Q04.005** ¿Qué hechos ocultos no debe revelar el diseño de «duración de actividades físicas»?
- **Q04.006** ¿Qué alternativas o rutas de interacción debe ofrecer «duración de actividades físicas» en Android pequeño?
- **Q04.007** ¿Cómo afecta «duración de actividades físicas» al reloj, los recursos o los eventos del mundo?
- **Q04.008** ¿Qué corrección o cancelación debería existir cuando «duración de actividades físicas» se utiliza por error?
- **Q04.009** ¿Qué estado relacionado con «duración de actividades físicas» debe sobrevivir al guardado y a la carga?
- **Q04.010** ¿Qué prueba reproducible demostraría que «duración de actividades físicas» funciona y no confunde al jugador?

### Subtema 2: tiempo invertido en conversaciones

- **Q04.011** ¿Qué experiencia concreta debe ofrecer «tiempo invertido en conversaciones» al jugador durante una partida normal?
- **Q04.012** ¿Qué situación narrativa justificaría que el juego permita «tiempo invertido en conversaciones»?
- **Q04.013** ¿Qué requisitos de estado deben comprobarse antes de habilitar «tiempo invertido en conversaciones»?
- **Q04.014** ¿Qué información debe conocer el jugador antes de usar «tiempo invertido en conversaciones»?
- **Q04.015** ¿Qué hechos ocultos no debe revelar el diseño de «tiempo invertido en conversaciones»?
- **Q04.016** ¿Qué alternativas o rutas de interacción debe ofrecer «tiempo invertido en conversaciones» en Android pequeño?
- **Q04.017** ¿Cómo afecta «tiempo invertido en conversaciones» al reloj, los recursos o los eventos del mundo?
- **Q04.018** ¿Qué corrección o cancelación debería existir cuando «tiempo invertido en conversaciones» se utiliza por error?
- **Q04.019** ¿Qué estado relacionado con «tiempo invertido en conversaciones» debe sobrevivir al guardado y a la carga?
- **Q04.020** ¿Qué prueba reproducible demostraría que «tiempo invertido en conversaciones» funciona y no confunde al jugador?

### Subtema 3: lectura de menús

- **Q04.021** ¿Qué experiencia concreta debe ofrecer «lectura de menús» al jugador durante una partida normal?
- **Q04.022** ¿Qué situación narrativa justificaría que el juego permita «lectura de menús»?
- **Q04.023** ¿Qué requisitos de estado deben comprobarse antes de habilitar «lectura de menús»?
- **Q04.024** ¿Qué información debe conocer el jugador antes de usar «lectura de menús»?
- **Q04.025** ¿Qué hechos ocultos no debe revelar el diseño de «lectura de menús»?
- **Q04.026** ¿Qué alternativas o rutas de interacción debe ofrecer «lectura de menús» en Android pequeño?
- **Q04.027** ¿Cómo afecta «lectura de menús» al reloj, los recursos o los eventos del mundo?
- **Q04.028** ¿Qué corrección o cancelación debería existir cuando «lectura de menús» se utiliza por error?
- **Q04.029** ¿Qué estado relacionado con «lectura de menús» debe sobrevivir al guardado y a la carga?
- **Q04.030** ¿Qué prueba reproducible demostraría que «lectura de menús» funciona y no confunde al jugador?

### Subtema 4: desplazamiento narrativo

- **Q04.031** ¿Qué experiencia concreta debe ofrecer «desplazamiento narrativo» al jugador durante una partida normal?
- **Q04.032** ¿Qué situación narrativa justificaría que el juego permita «desplazamiento narrativo»?
- **Q04.033** ¿Qué requisitos de estado deben comprobarse antes de habilitar «desplazamiento narrativo»?
- **Q04.034** ¿Qué información debe conocer el jugador antes de usar «desplazamiento narrativo»?
- **Q04.035** ¿Qué hechos ocultos no debe revelar el diseño de «desplazamiento narrativo»?
- **Q04.036** ¿Qué alternativas o rutas de interacción debe ofrecer «desplazamiento narrativo» en Android pequeño?
- **Q04.037** ¿Cómo afecta «desplazamiento narrativo» al reloj, los recursos o los eventos del mundo?
- **Q04.038** ¿Qué corrección o cancelación debería existir cuando «desplazamiento narrativo» se utiliza por error?
- **Q04.039** ¿Qué estado relacionado con «desplazamiento narrativo» debe sobrevivir al guardado y a la carga?
- **Q04.040** ¿Qué prueba reproducible demostraría que «desplazamiento narrativo» funciona y no confunde al jugador?

### Subtema 5: descanso y recuperación

- **Q04.041** ¿Qué experiencia concreta debe ofrecer «descanso y recuperación» al jugador durante una partida normal?
- **Q04.042** ¿Qué situación narrativa justificaría que el juego permita «descanso y recuperación»?
- **Q04.043** ¿Qué requisitos de estado deben comprobarse antes de habilitar «descanso y recuperación»?
- **Q04.044** ¿Qué información debe conocer el jugador antes de usar «descanso y recuperación»?
- **Q04.045** ¿Qué hechos ocultos no debe revelar el diseño de «descanso y recuperación»?
- **Q04.046** ¿Qué alternativas o rutas de interacción debe ofrecer «descanso y recuperación» en Android pequeño?
- **Q04.047** ¿Cómo afecta «descanso y recuperación» al reloj, los recursos o los eventos del mundo?
- **Q04.048** ¿Qué corrección o cancelación debería existir cuando «descanso y recuperación» se utiliza por error?
- **Q04.049** ¿Qué estado relacionado con «descanso y recuperación» debe sobrevivir al guardado y a la carga?
- **Q04.050** ¿Qué prueba reproducible demostraría que «descanso y recuperación» funciona y no confunde al jugador?

### Subtema 6: espera voluntaria

- **Q04.051** ¿Qué experiencia concreta debe ofrecer «espera voluntaria» al jugador durante una partida normal?
- **Q04.052** ¿Qué situación narrativa justificaría que el juego permita «espera voluntaria»?
- **Q04.053** ¿Qué requisitos de estado deben comprobarse antes de habilitar «espera voluntaria»?
- **Q04.054** ¿Qué información debe conocer el jugador antes de usar «espera voluntaria»?
- **Q04.055** ¿Qué hechos ocultos no debe revelar el diseño de «espera voluntaria»?
- **Q04.056** ¿Qué alternativas o rutas de interacción debe ofrecer «espera voluntaria» en Android pequeño?
- **Q04.057** ¿Cómo afecta «espera voluntaria» al reloj, los recursos o los eventos del mundo?
- **Q04.058** ¿Qué corrección o cancelación debería existir cuando «espera voluntaria» se utiliza por error?
- **Q04.059** ¿Qué estado relacionado con «espera voluntaria» debe sobrevivir al guardado y a la carga?
- **Q04.060** ¿Qué prueba reproducible demostraría que «espera voluntaria» funciona y no confunde al jugador?

### Subtema 7: acciones simultáneas

- **Q04.061** ¿Qué experiencia concreta debe ofrecer «acciones simultáneas» al jugador durante una partida normal?
- **Q04.062** ¿Qué situación narrativa justificaría que el juego permita «acciones simultáneas»?
- **Q04.063** ¿Qué requisitos de estado deben comprobarse antes de habilitar «acciones simultáneas»?
- **Q04.064** ¿Qué información debe conocer el jugador antes de usar «acciones simultáneas»?
- **Q04.065** ¿Qué hechos ocultos no debe revelar el diseño de «acciones simultáneas»?
- **Q04.066** ¿Qué alternativas o rutas de interacción debe ofrecer «acciones simultáneas» en Android pequeño?
- **Q04.067** ¿Cómo afecta «acciones simultáneas» al reloj, los recursos o los eventos del mundo?
- **Q04.068** ¿Qué corrección o cancelación debería existir cuando «acciones simultáneas» se utiliza por error?
- **Q04.069** ¿Qué estado relacionado con «acciones simultáneas» debe sobrevivir al guardado y a la carga?
- **Q04.070** ¿Qué prueba reproducible demostraría que «acciones simultáneas» funciona y no confunde al jugador?

### Subtema 8: saltos largos de tiempo

- **Q04.071** ¿Qué experiencia concreta debe ofrecer «saltos largos de tiempo» al jugador durante una partida normal?
- **Q04.072** ¿Qué situación narrativa justificaría que el juego permita «saltos largos de tiempo»?
- **Q04.073** ¿Qué requisitos de estado deben comprobarse antes de habilitar «saltos largos de tiempo»?
- **Q04.074** ¿Qué información debe conocer el jugador antes de usar «saltos largos de tiempo»?
- **Q04.075** ¿Qué hechos ocultos no debe revelar el diseño de «saltos largos de tiempo»?
- **Q04.076** ¿Qué alternativas o rutas de interacción debe ofrecer «saltos largos de tiempo» en Android pequeño?
- **Q04.077** ¿Cómo afecta «saltos largos de tiempo» al reloj, los recursos o los eventos del mundo?
- **Q04.078** ¿Qué corrección o cancelación debería existir cuando «saltos largos de tiempo» se utiliza por error?
- **Q04.079** ¿Qué estado relacionado con «saltos largos de tiempo» debe sobrevivir al guardado y a la carga?
- **Q04.080** ¿Qué prueba reproducible demostraría que «saltos largos de tiempo» funciona y no confunde al jugador?

### Subtema 9: interrupciones del mundo

- **Q04.081** ¿Qué experiencia concreta debe ofrecer «interrupciones del mundo» al jugador durante una partida normal?
- **Q04.082** ¿Qué situación narrativa justificaría que el juego permita «interrupciones del mundo»?
- **Q04.083** ¿Qué requisitos de estado deben comprobarse antes de habilitar «interrupciones del mundo»?
- **Q04.084** ¿Qué información debe conocer el jugador antes de usar «interrupciones del mundo»?
- **Q04.085** ¿Qué hechos ocultos no debe revelar el diseño de «interrupciones del mundo»?
- **Q04.086** ¿Qué alternativas o rutas de interacción debe ofrecer «interrupciones del mundo» en Android pequeño?
- **Q04.087** ¿Cómo afecta «interrupciones del mundo» al reloj, los recursos o los eventos del mundo?
- **Q04.088** ¿Qué corrección o cancelación debería existir cuando «interrupciones del mundo» se utiliza por error?
- **Q04.089** ¿Qué estado relacionado con «interrupciones del mundo» debe sobrevivir al guardado y a la carga?
- **Q04.090** ¿Qué prueba reproducible demostraría que «interrupciones del mundo» funciona y no confunde al jugador?

### Subtema 10: reloj mostrado al jugador

- **Q04.091** ¿Qué experiencia concreta debe ofrecer «reloj mostrado al jugador» al jugador durante una partida normal?
- **Q04.092** ¿Qué situación narrativa justificaría que el juego permita «reloj mostrado al jugador»?
- **Q04.093** ¿Qué requisitos de estado deben comprobarse antes de habilitar «reloj mostrado al jugador»?
- **Q04.094** ¿Qué información debe conocer el jugador antes de usar «reloj mostrado al jugador»?
- **Q04.095** ¿Qué hechos ocultos no debe revelar el diseño de «reloj mostrado al jugador»?
- **Q04.096** ¿Qué alternativas o rutas de interacción debe ofrecer «reloj mostrado al jugador» en Android pequeño?
- **Q04.097** ¿Cómo afecta «reloj mostrado al jugador» al reloj, los recursos o los eventos del mundo?
- **Q04.098** ¿Qué corrección o cancelación debería existir cuando «reloj mostrado al jugador» se utiliza por error?
- **Q04.099** ¿Qué estado relacionado con «reloj mostrado al jugador» debe sobrevivir al guardado y a la carga?
- **Q04.100** ¿Qué prueba reproducible demostraría que «reloj mostrado al jugador» funciona y no confunde al jugador?

## Q05 · P1 — ¿Qué consecuencias tiene la derrota o muerte del protagonista: heridas, pérdida de recursos, continuación, final de partida u otras?

### Subtema 1: derrota en combate

- **Q05.001** ¿Qué experiencia concreta debe ofrecer «derrota en combate» al jugador durante una partida normal?
- **Q05.002** ¿Qué situación narrativa justificaría que el juego permita «derrota en combate»?
- **Q05.003** ¿Qué requisitos de estado deben comprobarse antes de habilitar «derrota en combate»?
- **Q05.004** ¿Qué información debe conocer el jugador antes de usar «derrota en combate»?
- **Q05.005** ¿Qué hechos ocultos no debe revelar el diseño de «derrota en combate»?
- **Q05.006** ¿Qué alternativas o rutas de interacción debe ofrecer «derrota en combate» en Android pequeño?
- **Q05.007** ¿Cómo afecta «derrota en combate» al reloj, los recursos o los eventos del mundo?
- **Q05.008** ¿Qué corrección o cancelación debería existir cuando «derrota en combate» se utiliza por error?
- **Q05.009** ¿Qué estado relacionado con «derrota en combate» debe sobrevivir al guardado y a la carga?
- **Q05.010** ¿Qué prueba reproducible demostraría que «derrota en combate» funciona y no confunde al jugador?

### Subtema 2: heridas persistentes

- **Q05.011** ¿Qué experiencia concreta debe ofrecer «heridas persistentes» al jugador durante una partida normal?
- **Q05.012** ¿Qué situación narrativa justificaría que el juego permita «heridas persistentes»?
- **Q05.013** ¿Qué requisitos de estado deben comprobarse antes de habilitar «heridas persistentes»?
- **Q05.014** ¿Qué información debe conocer el jugador antes de usar «heridas persistentes»?
- **Q05.015** ¿Qué hechos ocultos no debe revelar el diseño de «heridas persistentes»?
- **Q05.016** ¿Qué alternativas o rutas de interacción debe ofrecer «heridas persistentes» en Android pequeño?
- **Q05.017** ¿Cómo afecta «heridas persistentes» al reloj, los recursos o los eventos del mundo?
- **Q05.018** ¿Qué corrección o cancelación debería existir cuando «heridas persistentes» se utiliza por error?
- **Q05.019** ¿Qué estado relacionado con «heridas persistentes» debe sobrevivir al guardado y a la carga?
- **Q05.020** ¿Qué prueba reproducible demostraría que «heridas persistentes» funciona y no confunde al jugador?

### Subtema 3: incapacidad temporal

- **Q05.021** ¿Qué experiencia concreta debe ofrecer «incapacidad temporal» al jugador durante una partida normal?
- **Q05.022** ¿Qué situación narrativa justificaría que el juego permita «incapacidad temporal»?
- **Q05.023** ¿Qué requisitos de estado deben comprobarse antes de habilitar «incapacidad temporal»?
- **Q05.024** ¿Qué información debe conocer el jugador antes de usar «incapacidad temporal»?
- **Q05.025** ¿Qué hechos ocultos no debe revelar el diseño de «incapacidad temporal»?
- **Q05.026** ¿Qué alternativas o rutas de interacción debe ofrecer «incapacidad temporal» en Android pequeño?
- **Q05.027** ¿Cómo afecta «incapacidad temporal» al reloj, los recursos o los eventos del mundo?
- **Q05.028** ¿Qué corrección o cancelación debería existir cuando «incapacidad temporal» se utiliza por error?
- **Q05.029** ¿Qué estado relacionado con «incapacidad temporal» debe sobrevivir al guardado y a la carga?
- **Q05.030** ¿Qué prueba reproducible demostraría que «incapacidad temporal» funciona y no confunde al jugador?

### Subtema 4: pérdida de inventario

- **Q05.031** ¿Qué experiencia concreta debe ofrecer «pérdida de inventario» al jugador durante una partida normal?
- **Q05.032** ¿Qué situación narrativa justificaría que el juego permita «pérdida de inventario»?
- **Q05.033** ¿Qué requisitos de estado deben comprobarse antes de habilitar «pérdida de inventario»?
- **Q05.034** ¿Qué información debe conocer el jugador antes de usar «pérdida de inventario»?
- **Q05.035** ¿Qué hechos ocultos no debe revelar el diseño de «pérdida de inventario»?
- **Q05.036** ¿Qué alternativas o rutas de interacción debe ofrecer «pérdida de inventario» en Android pequeño?
- **Q05.037** ¿Cómo afecta «pérdida de inventario» al reloj, los recursos o los eventos del mundo?
- **Q05.038** ¿Qué corrección o cancelación debería existir cuando «pérdida de inventario» se utiliza por error?
- **Q05.039** ¿Qué estado relacionado con «pérdida de inventario» debe sobrevivir al guardado y a la carga?
- **Q05.040** ¿Qué prueba reproducible demostraría que «pérdida de inventario» funciona y no confunde al jugador?

### Subtema 5: rescate por terceros

- **Q05.041** ¿Qué experiencia concreta debe ofrecer «rescate por terceros» al jugador durante una partida normal?
- **Q05.042** ¿Qué situación narrativa justificaría que el juego permita «rescate por terceros»?
- **Q05.043** ¿Qué requisitos de estado deben comprobarse antes de habilitar «rescate por terceros»?
- **Q05.044** ¿Qué información debe conocer el jugador antes de usar «rescate por terceros»?
- **Q05.045** ¿Qué hechos ocultos no debe revelar el diseño de «rescate por terceros»?
- **Q05.046** ¿Qué alternativas o rutas de interacción debe ofrecer «rescate por terceros» en Android pequeño?
- **Q05.047** ¿Cómo afecta «rescate por terceros» al reloj, los recursos o los eventos del mundo?
- **Q05.048** ¿Qué corrección o cancelación debería existir cuando «rescate por terceros» se utiliza por error?
- **Q05.049** ¿Qué estado relacionado con «rescate por terceros» debe sobrevivir al guardado y a la carga?
- **Q05.050** ¿Qué prueba reproducible demostraría que «rescate por terceros» funciona y no confunde al jugador?

### Subtema 6: muerte del protagonista

- **Q05.051** ¿Qué experiencia concreta debe ofrecer «muerte del protagonista» al jugador durante una partida normal?
- **Q05.052** ¿Qué situación narrativa justificaría que el juego permita «muerte del protagonista»?
- **Q05.053** ¿Qué requisitos de estado deben comprobarse antes de habilitar «muerte del protagonista»?
- **Q05.054** ¿Qué información debe conocer el jugador antes de usar «muerte del protagonista»?
- **Q05.055** ¿Qué hechos ocultos no debe revelar el diseño de «muerte del protagonista»?
- **Q05.056** ¿Qué alternativas o rutas de interacción debe ofrecer «muerte del protagonista» en Android pequeño?
- **Q05.057** ¿Cómo afecta «muerte del protagonista» al reloj, los recursos o los eventos del mundo?
- **Q05.058** ¿Qué corrección o cancelación debería existir cuando «muerte del protagonista» se utiliza por error?
- **Q05.059** ¿Qué estado relacionado con «muerte del protagonista» debe sobrevivir al guardado y a la carga?
- **Q05.060** ¿Qué prueba reproducible demostraría que «muerte del protagonista» funciona y no confunde al jugador?

### Subtema 7: herederos o continuación

- **Q05.061** ¿Qué experiencia concreta debe ofrecer «herederos o continuación» al jugador durante una partida normal?
- **Q05.062** ¿Qué situación narrativa justificaría que el juego permita «herederos o continuación»?
- **Q05.063** ¿Qué requisitos de estado deben comprobarse antes de habilitar «herederos o continuación»?
- **Q05.064** ¿Qué información debe conocer el jugador antes de usar «herederos o continuación»?
- **Q05.065** ¿Qué hechos ocultos no debe revelar el diseño de «herederos o continuación»?
- **Q05.066** ¿Qué alternativas o rutas de interacción debe ofrecer «herederos o continuación» en Android pequeño?
- **Q05.067** ¿Cómo afecta «herederos o continuación» al reloj, los recursos o los eventos del mundo?
- **Q05.068** ¿Qué corrección o cancelación debería existir cuando «herederos o continuación» se utiliza por error?
- **Q05.069** ¿Qué estado relacionado con «herederos o continuación» debe sobrevivir al guardado y a la carga?
- **Q05.070** ¿Qué prueba reproducible demostraría que «herederos o continuación» funciona y no confunde al jugador?

### Subtema 8: retroceso de progreso

- **Q05.071** ¿Qué experiencia concreta debe ofrecer «retroceso de progreso» al jugador durante una partida normal?
- **Q05.072** ¿Qué situación narrativa justificaría que el juego permita «retroceso de progreso»?
- **Q05.073** ¿Qué requisitos de estado deben comprobarse antes de habilitar «retroceso de progreso»?
- **Q05.074** ¿Qué información debe conocer el jugador antes de usar «retroceso de progreso»?
- **Q05.075** ¿Qué hechos ocultos no debe revelar el diseño de «retroceso de progreso»?
- **Q05.076** ¿Qué alternativas o rutas de interacción debe ofrecer «retroceso de progreso» en Android pequeño?
- **Q05.077** ¿Cómo afecta «retroceso de progreso» al reloj, los recursos o los eventos del mundo?
- **Q05.078** ¿Qué corrección o cancelación debería existir cuando «retroceso de progreso» se utiliza por error?
- **Q05.079** ¿Qué estado relacionado con «retroceso de progreso» debe sobrevivir al guardado y a la carga?
- **Q05.080** ¿Qué prueba reproducible demostraría que «retroceso de progreso» funciona y no confunde al jugador?

### Subtema 9: consecuencias sociales de perder

- **Q05.081** ¿Qué experiencia concreta debe ofrecer «consecuencias sociales de perder» al jugador durante una partida normal?
- **Q05.082** ¿Qué situación narrativa justificaría que el juego permita «consecuencias sociales de perder»?
- **Q05.083** ¿Qué requisitos de estado deben comprobarse antes de habilitar «consecuencias sociales de perder»?
- **Q05.084** ¿Qué información debe conocer el jugador antes de usar «consecuencias sociales de perder»?
- **Q05.085** ¿Qué hechos ocultos no debe revelar el diseño de «consecuencias sociales de perder»?
- **Q05.086** ¿Qué alternativas o rutas de interacción debe ofrecer «consecuencias sociales de perder» en Android pequeño?
- **Q05.087** ¿Cómo afecta «consecuencias sociales de perder» al reloj, los recursos o los eventos del mundo?
- **Q05.088** ¿Qué corrección o cancelación debería existir cuando «consecuencias sociales de perder» se utiliza por error?
- **Q05.089** ¿Qué estado relacionado con «consecuencias sociales de perder» debe sobrevivir al guardado y a la carga?
- **Q05.090** ¿Qué prueba reproducible demostraría que «consecuencias sociales de perder» funciona y no confunde al jugador?

### Subtema 10: guardado tras derrota

- **Q05.091** ¿Qué experiencia concreta debe ofrecer «guardado tras derrota» al jugador durante una partida normal?
- **Q05.092** ¿Qué situación narrativa justificaría que el juego permita «guardado tras derrota»?
- **Q05.093** ¿Qué requisitos de estado deben comprobarse antes de habilitar «guardado tras derrota»?
- **Q05.094** ¿Qué información debe conocer el jugador antes de usar «guardado tras derrota»?
- **Q05.095** ¿Qué hechos ocultos no debe revelar el diseño de «guardado tras derrota»?
- **Q05.096** ¿Qué alternativas o rutas de interacción debe ofrecer «guardado tras derrota» en Android pequeño?
- **Q05.097** ¿Cómo afecta «guardado tras derrota» al reloj, los recursos o los eventos del mundo?
- **Q05.098** ¿Qué corrección o cancelación debería existir cuando «guardado tras derrota» se utiliza por error?
- **Q05.099** ¿Qué estado relacionado con «guardado tras derrota» debe sobrevivir al guardado y a la carga?
- **Q05.100** ¿Qué prueba reproducible demostraría que «guardado tras derrota» funciona y no confunde al jugador?
