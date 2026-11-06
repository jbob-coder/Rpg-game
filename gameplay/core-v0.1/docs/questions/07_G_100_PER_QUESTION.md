# Banco de subpreguntas — G. Implementación, guardado y verificación

**Estado:** pendiente de decisión; no equivale a implementación ni pruebas superadas. **Fecha:** 2026-11-06.
**Origen:** [inventario de decisiones Q01–Q43](06_OPEN_DESIGN_QUESTIONS_BACKLOG.md).
**Rango:** Q40–Q43.

Se desglosa cada pregunta en 10 subtemas y 10 criterios; todas las preguntas quedan abiertas hasta respuesta del propietario.

## Q40 · P0 — ¿Qué plataforma/arquitectura definitiva ejecutará el núcleo JavaScript del prototipo en Android y cómo se integrará la UI?

### Subtema 1: núcleo JavaScript actual

- **Q40.001** ¿Qué responsabilidad técnica concreta debe cubrir «núcleo JavaScript actual»?
- **Q40.002** ¿Qué opciones de implementación debemos comparar para «núcleo JavaScript actual» y con qué criterio?
- **Q40.003** ¿Qué versión de plataforma, formato o API condiciona «núcleo JavaScript actual»?
- **Q40.004** ¿Qué entradas, salidas y contratos permiten aislar «núcleo JavaScript actual» del resto del juego?
- **Q40.005** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «núcleo JavaScript actual»?
- **Q40.006** ¿Cómo se comportaría «núcleo JavaScript actual» ante fallos, interrupciones y datos inesperados?
- **Q40.007** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «núcleo JavaScript actual»?
- **Q40.008** ¿Qué cambios pequeños y reversibles permitirían incorporar «núcleo JavaScript actual» sin alterar el motor actual?
- **Q40.009** ¿Qué evidencia exacta debe guardarse para verificar «núcleo JavaScript actual» en GitHub y Android?
- **Q40.010** ¿Qué criterios de aceptación y regresión permiten declarar completo «núcleo JavaScript actual»?

### Subtema 2: integración mediante WebView

- **Q40.011** ¿Qué responsabilidad técnica concreta debe cubrir «integración mediante WebView»?
- **Q40.012** ¿Qué opciones de implementación debemos comparar para «integración mediante WebView» y con qué criterio?
- **Q40.013** ¿Qué versión de plataforma, formato o API condiciona «integración mediante WebView»?
- **Q40.014** ¿Qué entradas, salidas y contratos permiten aislar «integración mediante WebView» del resto del juego?
- **Q40.015** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «integración mediante WebView»?
- **Q40.016** ¿Cómo se comportaría «integración mediante WebView» ante fallos, interrupciones y datos inesperados?
- **Q40.017** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «integración mediante WebView»?
- **Q40.018** ¿Qué cambios pequeños y reversibles permitirían incorporar «integración mediante WebView» sin alterar el motor actual?
- **Q40.019** ¿Qué evidencia exacta debe guardarse para verificar «integración mediante WebView» en GitHub y Android?
- **Q40.020** ¿Qué criterios de aceptación y regresión permiten declarar completo «integración mediante WebView»?

### Subtema 3: uso de motor nativo Android

- **Q40.021** ¿Qué responsabilidad técnica concreta debe cubrir «uso de motor nativo Android»?
- **Q40.022** ¿Qué opciones de implementación debemos comparar para «uso de motor nativo Android» y con qué criterio?
- **Q40.023** ¿Qué versión de plataforma, formato o API condiciona «uso de motor nativo Android»?
- **Q40.024** ¿Qué entradas, salidas y contratos permiten aislar «uso de motor nativo Android» del resto del juego?
- **Q40.025** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «uso de motor nativo Android»?
- **Q40.026** ¿Cómo se comportaría «uso de motor nativo Android» ante fallos, interrupciones y datos inesperados?
- **Q40.027** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «uso de motor nativo Android»?
- **Q40.028** ¿Qué cambios pequeños y reversibles permitirían incorporar «uso de motor nativo Android» sin alterar el motor actual?
- **Q40.029** ¿Qué evidencia exacta debe guardarse para verificar «uso de motor nativo Android» en GitHub y Android?
- **Q40.030** ¿Qué criterios de aceptación y regresión permiten declarar completo «uso de motor nativo Android»?

### Subtema 4: compatibilidad con frameworks híbridos

- **Q40.031** ¿Qué responsabilidad técnica concreta debe cubrir «compatibilidad con frameworks híbridos»?
- **Q40.032** ¿Qué opciones de implementación debemos comparar para «compatibilidad con frameworks híbridos» y con qué criterio?
- **Q40.033** ¿Qué versión de plataforma, formato o API condiciona «compatibilidad con frameworks híbridos»?
- **Q40.034** ¿Qué entradas, salidas y contratos permiten aislar «compatibilidad con frameworks híbridos» del resto del juego?
- **Q40.035** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «compatibilidad con frameworks híbridos»?
- **Q40.036** ¿Cómo se comportaría «compatibilidad con frameworks híbridos» ante fallos, interrupciones y datos inesperados?
- **Q40.037** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «compatibilidad con frameworks híbridos»?
- **Q40.038** ¿Qué cambios pequeños y reversibles permitirían incorporar «compatibilidad con frameworks híbridos» sin alterar el motor actual?
- **Q40.039** ¿Qué evidencia exacta debe guardarse para verificar «compatibilidad con frameworks híbridos» en GitHub y Android?
- **Q40.040** ¿Qué criterios de aceptación y regresión permiten declarar completo «compatibilidad con frameworks híbridos»?

### Subtema 5: contrato ViewModel/UI

- **Q40.041** ¿Qué responsabilidad técnica concreta debe cubrir «contrato ViewModel/UI»?
- **Q40.042** ¿Qué opciones de implementación debemos comparar para «contrato ViewModel/UI» y con qué criterio?
- **Q40.043** ¿Qué versión de plataforma, formato o API condiciona «contrato ViewModel/UI»?
- **Q40.044** ¿Qué entradas, salidas y contratos permiten aislar «contrato ViewModel/UI» del resto del juego?
- **Q40.045** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «contrato ViewModel/UI»?
- **Q40.046** ¿Cómo se comportaría «contrato ViewModel/UI» ante fallos, interrupciones y datos inesperados?
- **Q40.047** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «contrato ViewModel/UI»?
- **Q40.048** ¿Qué cambios pequeños y reversibles permitirían incorporar «contrato ViewModel/UI» sin alterar el motor actual?
- **Q40.049** ¿Qué evidencia exacta debe guardarse para verificar «contrato ViewModel/UI» en GitHub y Android?
- **Q40.050** ¿Qué criterios de aceptación y regresión permiten declarar completo «contrato ViewModel/UI»?

### Subtema 6: ejecución offline

- **Q40.051** ¿Qué responsabilidad técnica concreta debe cubrir «ejecución offline»?
- **Q40.052** ¿Qué opciones de implementación debemos comparar para «ejecución offline» y con qué criterio?
- **Q40.053** ¿Qué versión de plataforma, formato o API condiciona «ejecución offline»?
- **Q40.054** ¿Qué entradas, salidas y contratos permiten aislar «ejecución offline» del resto del juego?
- **Q40.055** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «ejecución offline»?
- **Q40.056** ¿Cómo se comportaría «ejecución offline» ante fallos, interrupciones y datos inesperados?
- **Q40.057** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «ejecución offline»?
- **Q40.058** ¿Qué cambios pequeños y reversibles permitirían incorporar «ejecución offline» sin alterar el motor actual?
- **Q40.059** ¿Qué evidencia exacta debe guardarse para verificar «ejecución offline» en GitHub y Android?
- **Q40.060** ¿Qué criterios de aceptación y regresión permiten declarar completo «ejecución offline»?

### Subtema 7: seguridad del estado

- **Q40.061** ¿Qué responsabilidad técnica concreta debe cubrir «seguridad del estado»?
- **Q40.062** ¿Qué opciones de implementación debemos comparar para «seguridad del estado» y con qué criterio?
- **Q40.063** ¿Qué versión de plataforma, formato o API condiciona «seguridad del estado»?
- **Q40.064** ¿Qué entradas, salidas y contratos permiten aislar «seguridad del estado» del resto del juego?
- **Q40.065** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «seguridad del estado»?
- **Q40.066** ¿Cómo se comportaría «seguridad del estado» ante fallos, interrupciones y datos inesperados?
- **Q40.067** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «seguridad del estado»?
- **Q40.068** ¿Qué cambios pequeños y reversibles permitirían incorporar «seguridad del estado» sin alterar el motor actual?
- **Q40.069** ¿Qué evidencia exacta debe guardarse para verificar «seguridad del estado» en GitHub y Android?
- **Q40.070** ¿Qué criterios de aceptación y regresión permiten declarar completo «seguridad del estado»?

### Subtema 8: rendimiento del evaluador

- **Q40.071** ¿Qué responsabilidad técnica concreta debe cubrir «rendimiento del evaluador»?
- **Q40.072** ¿Qué opciones de implementación debemos comparar para «rendimiento del evaluador» y con qué criterio?
- **Q40.073** ¿Qué versión de plataforma, formato o API condiciona «rendimiento del evaluador»?
- **Q40.074** ¿Qué entradas, salidas y contratos permiten aislar «rendimiento del evaluador» del resto del juego?
- **Q40.075** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «rendimiento del evaluador»?
- **Q40.076** ¿Cómo se comportaría «rendimiento del evaluador» ante fallos, interrupciones y datos inesperados?
- **Q40.077** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «rendimiento del evaluador»?
- **Q40.078** ¿Qué cambios pequeños y reversibles permitirían incorporar «rendimiento del evaluador» sin alterar el motor actual?
- **Q40.079** ¿Qué evidencia exacta debe guardarse para verificar «rendimiento del evaluador» en GitHub y Android?
- **Q40.080** ¿Qué criterios de aceptación y regresión permiten declarar completo «rendimiento del evaluador»?

### Subtema 9: pruebas de integración

- **Q40.081** ¿Qué responsabilidad técnica concreta debe cubrir «pruebas de integración»?
- **Q40.082** ¿Qué opciones de implementación debemos comparar para «pruebas de integración» y con qué criterio?
- **Q40.083** ¿Qué versión de plataforma, formato o API condiciona «pruebas de integración»?
- **Q40.084** ¿Qué entradas, salidas y contratos permiten aislar «pruebas de integración» del resto del juego?
- **Q40.085** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «pruebas de integración»?
- **Q40.086** ¿Cómo se comportaría «pruebas de integración» ante fallos, interrupciones y datos inesperados?
- **Q40.087** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «pruebas de integración»?
- **Q40.088** ¿Qué cambios pequeños y reversibles permitirían incorporar «pruebas de integración» sin alterar el motor actual?
- **Q40.089** ¿Qué evidencia exacta debe guardarse para verificar «pruebas de integración» en GitHub y Android?
- **Q40.090** ¿Qué criterios de aceptación y regresión permiten declarar completo «pruebas de integración»?

### Subtema 10: portabilidad futura de código

- **Q40.091** ¿Qué responsabilidad técnica concreta debe cubrir «portabilidad futura de código»?
- **Q40.092** ¿Qué opciones de implementación debemos comparar para «portabilidad futura de código» y con qué criterio?
- **Q40.093** ¿Qué versión de plataforma, formato o API condiciona «portabilidad futura de código»?
- **Q40.094** ¿Qué entradas, salidas y contratos permiten aislar «portabilidad futura de código» del resto del juego?
- **Q40.095** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «portabilidad futura de código»?
- **Q40.096** ¿Cómo se comportaría «portabilidad futura de código» ante fallos, interrupciones y datos inesperados?
- **Q40.097** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «portabilidad futura de código»?
- **Q40.098** ¿Qué cambios pequeños y reversibles permitirían incorporar «portabilidad futura de código» sin alterar el motor actual?
- **Q40.099** ¿Qué evidencia exacta debe guardarse para verificar «portabilidad futura de código» en GitHub y Android?
- **Q40.100** ¿Qué criterios de aceptación y regresión permiten declarar completo «portabilidad futura de código»?

## Q41 · P1 — ¿Cómo serán los slots, autoguardado, recuperación, migraciones y almacenamiento local (o eventual sincronización) de partidas?

### Subtema 1: slots manuales

- **Q41.001** ¿Qué responsabilidad técnica concreta debe cubrir «slots manuales»?
- **Q41.002** ¿Qué opciones de implementación debemos comparar para «slots manuales» y con qué criterio?
- **Q41.003** ¿Qué versión de plataforma, formato o API condiciona «slots manuales»?
- **Q41.004** ¿Qué entradas, salidas y contratos permiten aislar «slots manuales» del resto del juego?
- **Q41.005** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «slots manuales»?
- **Q41.006** ¿Cómo se comportaría «slots manuales» ante fallos, interrupciones y datos inesperados?
- **Q41.007** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «slots manuales»?
- **Q41.008** ¿Qué cambios pequeños y reversibles permitirían incorporar «slots manuales» sin alterar el motor actual?
- **Q41.009** ¿Qué evidencia exacta debe guardarse para verificar «slots manuales» en GitHub y Android?
- **Q41.010** ¿Qué criterios de aceptación y regresión permiten declarar completo «slots manuales»?

### Subtema 2: autoguardado por acción

- **Q41.011** ¿Qué responsabilidad técnica concreta debe cubrir «autoguardado por acción»?
- **Q41.012** ¿Qué opciones de implementación debemos comparar para «autoguardado por acción» y con qué criterio?
- **Q41.013** ¿Qué versión de plataforma, formato o API condiciona «autoguardado por acción»?
- **Q41.014** ¿Qué entradas, salidas y contratos permiten aislar «autoguardado por acción» del resto del juego?
- **Q41.015** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «autoguardado por acción»?
- **Q41.016** ¿Cómo se comportaría «autoguardado por acción» ante fallos, interrupciones y datos inesperados?
- **Q41.017** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «autoguardado por acción»?
- **Q41.018** ¿Qué cambios pequeños y reversibles permitirían incorporar «autoguardado por acción» sin alterar el motor actual?
- **Q41.019** ¿Qué evidencia exacta debe guardarse para verificar «autoguardado por acción» en GitHub y Android?
- **Q41.020** ¿Qué criterios de aceptación y regresión permiten declarar completo «autoguardado por acción»?

### Subtema 3: guardados durante eventos

- **Q41.021** ¿Qué responsabilidad técnica concreta debe cubrir «guardados durante eventos»?
- **Q41.022** ¿Qué opciones de implementación debemos comparar para «guardados durante eventos» y con qué criterio?
- **Q41.023** ¿Qué versión de plataforma, formato o API condiciona «guardados durante eventos»?
- **Q41.024** ¿Qué entradas, salidas y contratos permiten aislar «guardados durante eventos» del resto del juego?
- **Q41.025** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «guardados durante eventos»?
- **Q41.026** ¿Cómo se comportaría «guardados durante eventos» ante fallos, interrupciones y datos inesperados?
- **Q41.027** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «guardados durante eventos»?
- **Q41.028** ¿Qué cambios pequeños y reversibles permitirían incorporar «guardados durante eventos» sin alterar el motor actual?
- **Q41.029** ¿Qué evidencia exacta debe guardarse para verificar «guardados durante eventos» en GitHub y Android?
- **Q41.030** ¿Qué criterios de aceptación y regresión permiten declarar completo «guardados durante eventos»?

### Subtema 4: recuperación ante cierre

- **Q41.031** ¿Qué responsabilidad técnica concreta debe cubrir «recuperación ante cierre»?
- **Q41.032** ¿Qué opciones de implementación debemos comparar para «recuperación ante cierre» y con qué criterio?
- **Q41.033** ¿Qué versión de plataforma, formato o API condiciona «recuperación ante cierre»?
- **Q41.034** ¿Qué entradas, salidas y contratos permiten aislar «recuperación ante cierre» del resto del juego?
- **Q41.035** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «recuperación ante cierre»?
- **Q41.036** ¿Cómo se comportaría «recuperación ante cierre» ante fallos, interrupciones y datos inesperados?
- **Q41.037** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «recuperación ante cierre»?
- **Q41.038** ¿Qué cambios pequeños y reversibles permitirían incorporar «recuperación ante cierre» sin alterar el motor actual?
- **Q41.039** ¿Qué evidencia exacta debe guardarse para verificar «recuperación ante cierre» en GitHub y Android?
- **Q41.040** ¿Qué criterios de aceptación y regresión permiten declarar completo «recuperación ante cierre»?

### Subtema 5: versionado de esquema

- **Q41.041** ¿Qué responsabilidad técnica concreta debe cubrir «versionado de esquema»?
- **Q41.042** ¿Qué opciones de implementación debemos comparar para «versionado de esquema» y con qué criterio?
- **Q41.043** ¿Qué versión de plataforma, formato o API condiciona «versionado de esquema»?
- **Q41.044** ¿Qué entradas, salidas y contratos permiten aislar «versionado de esquema» del resto del juego?
- **Q41.045** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «versionado de esquema»?
- **Q41.046** ¿Cómo se comportaría «versionado de esquema» ante fallos, interrupciones y datos inesperados?
- **Q41.047** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «versionado de esquema»?
- **Q41.048** ¿Qué cambios pequeños y reversibles permitirían incorporar «versionado de esquema» sin alterar el motor actual?
- **Q41.049** ¿Qué evidencia exacta debe guardarse para verificar «versionado de esquema» en GitHub y Android?
- **Q41.050** ¿Qué criterios de aceptación y regresión permiten declarar completo «versionado de esquema»?

### Subtema 6: migración de partidas

- **Q41.051** ¿Qué responsabilidad técnica concreta debe cubrir «migración de partidas»?
- **Q41.052** ¿Qué opciones de implementación debemos comparar para «migración de partidas» y con qué criterio?
- **Q41.053** ¿Qué versión de plataforma, formato o API condiciona «migración de partidas»?
- **Q41.054** ¿Qué entradas, salidas y contratos permiten aislar «migración de partidas» del resto del juego?
- **Q41.055** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «migración de partidas»?
- **Q41.056** ¿Cómo se comportaría «migración de partidas» ante fallos, interrupciones y datos inesperados?
- **Q41.057** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «migración de partidas»?
- **Q41.058** ¿Qué cambios pequeños y reversibles permitirían incorporar «migración de partidas» sin alterar el motor actual?
- **Q41.059** ¿Qué evidencia exacta debe guardarse para verificar «migración de partidas» en GitHub y Android?
- **Q41.060** ¿Qué criterios de aceptación y regresión permiten declarar completo «migración de partidas»?

### Subtema 7: integridad y corrupción

- **Q41.061** ¿Qué responsabilidad técnica concreta debe cubrir «integridad y corrupción»?
- **Q41.062** ¿Qué opciones de implementación debemos comparar para «integridad y corrupción» y con qué criterio?
- **Q41.063** ¿Qué versión de plataforma, formato o API condiciona «integridad y corrupción»?
- **Q41.064** ¿Qué entradas, salidas y contratos permiten aislar «integridad y corrupción» del resto del juego?
- **Q41.065** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «integridad y corrupción»?
- **Q41.066** ¿Cómo se comportaría «integridad y corrupción» ante fallos, interrupciones y datos inesperados?
- **Q41.067** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «integridad y corrupción»?
- **Q41.068** ¿Qué cambios pequeños y reversibles permitirían incorporar «integridad y corrupción» sin alterar el motor actual?
- **Q41.069** ¿Qué evidencia exacta debe guardarse para verificar «integridad y corrupción» en GitHub y Android?
- **Q41.070** ¿Qué criterios de aceptación y regresión permiten declarar completo «integridad y corrupción»?

### Subtema 8: archivos grandes

- **Q41.071** ¿Qué responsabilidad técnica concreta debe cubrir «archivos grandes»?
- **Q41.072** ¿Qué opciones de implementación debemos comparar para «archivos grandes» y con qué criterio?
- **Q41.073** ¿Qué versión de plataforma, formato o API condiciona «archivos grandes»?
- **Q41.074** ¿Qué entradas, salidas y contratos permiten aislar «archivos grandes» del resto del juego?
- **Q41.075** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «archivos grandes»?
- **Q41.076** ¿Cómo se comportaría «archivos grandes» ante fallos, interrupciones y datos inesperados?
- **Q41.077** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «archivos grandes»?
- **Q41.078** ¿Qué cambios pequeños y reversibles permitirían incorporar «archivos grandes» sin alterar el motor actual?
- **Q41.079** ¿Qué evidencia exacta debe guardarse para verificar «archivos grandes» en GitHub y Android?
- **Q41.080** ¿Qué criterios de aceptación y regresión permiten declarar completo «archivos grandes»?

### Subtema 9: persistencia de aleatoriedad

- **Q41.081** ¿Qué responsabilidad técnica concreta debe cubrir «persistencia de aleatoriedad»?
- **Q41.082** ¿Qué opciones de implementación debemos comparar para «persistencia de aleatoriedad» y con qué criterio?
- **Q41.083** ¿Qué versión de plataforma, formato o API condiciona «persistencia de aleatoriedad»?
- **Q41.084** ¿Qué entradas, salidas y contratos permiten aislar «persistencia de aleatoriedad» del resto del juego?
- **Q41.085** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «persistencia de aleatoriedad»?
- **Q41.086** ¿Cómo se comportaría «persistencia de aleatoriedad» ante fallos, interrupciones y datos inesperados?
- **Q41.087** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «persistencia de aleatoriedad»?
- **Q41.088** ¿Qué cambios pequeños y reversibles permitirían incorporar «persistencia de aleatoriedad» sin alterar el motor actual?
- **Q41.089** ¿Qué evidencia exacta debe guardarse para verificar «persistencia de aleatoriedad» en GitHub y Android?
- **Q41.090** ¿Qué criterios de aceptación y regresión permiten declarar completo «persistencia de aleatoriedad»?

### Subtema 10: sincronización opcional entre dispositivos

- **Q41.091** ¿Qué responsabilidad técnica concreta debe cubrir «sincronización opcional entre dispositivos»?
- **Q41.092** ¿Qué opciones de implementación debemos comparar para «sincronización opcional entre dispositivos» y con qué criterio?
- **Q41.093** ¿Qué versión de plataforma, formato o API condiciona «sincronización opcional entre dispositivos»?
- **Q41.094** ¿Qué entradas, salidas y contratos permiten aislar «sincronización opcional entre dispositivos» del resto del juego?
- **Q41.095** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «sincronización opcional entre dispositivos»?
- **Q41.096** ¿Cómo se comportaría «sincronización opcional entre dispositivos» ante fallos, interrupciones y datos inesperados?
- **Q41.097** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «sincronización opcional entre dispositivos»?
- **Q41.098** ¿Qué cambios pequeños y reversibles permitirían incorporar «sincronización opcional entre dispositivos» sin alterar el motor actual?
- **Q41.099** ¿Qué evidencia exacta debe guardarse para verificar «sincronización opcional entre dispositivos» en GitHub y Android?
- **Q41.100** ¿Qué criterios de aceptación y regresión permiten declarar completo «sincronización opcional entre dispositivos»?

## Q42 · P1 — ¿Cuál es el dispositivo Android mínimo objetivo y qué presupuestos de rendimiento, memoria, accesibilidad y tamaños de texto debe cumplir?

### Subtema 1: dispositivos de gama baja

- **Q42.001** ¿Qué responsabilidad técnica concreta debe cubrir «dispositivos de gama baja»?
- **Q42.002** ¿Qué opciones de implementación debemos comparar para «dispositivos de gama baja» y con qué criterio?
- **Q42.003** ¿Qué versión de plataforma, formato o API condiciona «dispositivos de gama baja»?
- **Q42.004** ¿Qué entradas, salidas y contratos permiten aislar «dispositivos de gama baja» del resto del juego?
- **Q42.005** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «dispositivos de gama baja»?
- **Q42.006** ¿Cómo se comportaría «dispositivos de gama baja» ante fallos, interrupciones y datos inesperados?
- **Q42.007** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «dispositivos de gama baja»?
- **Q42.008** ¿Qué cambios pequeños y reversibles permitirían incorporar «dispositivos de gama baja» sin alterar el motor actual?
- **Q42.009** ¿Qué evidencia exacta debe guardarse para verificar «dispositivos de gama baja» en GitHub y Android?
- **Q42.010** ¿Qué criterios de aceptación y regresión permiten declarar completo «dispositivos de gama baja»?

### Subtema 2: memoria durante simulación

- **Q42.011** ¿Qué responsabilidad técnica concreta debe cubrir «memoria durante simulación»?
- **Q42.012** ¿Qué opciones de implementación debemos comparar para «memoria durante simulación» y con qué criterio?
- **Q42.013** ¿Qué versión de plataforma, formato o API condiciona «memoria durante simulación»?
- **Q42.014** ¿Qué entradas, salidas y contratos permiten aislar «memoria durante simulación» del resto del juego?
- **Q42.015** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «memoria durante simulación»?
- **Q42.016** ¿Cómo se comportaría «memoria durante simulación» ante fallos, interrupciones y datos inesperados?
- **Q42.017** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «memoria durante simulación»?
- **Q42.018** ¿Qué cambios pequeños y reversibles permitirían incorporar «memoria durante simulación» sin alterar el motor actual?
- **Q42.019** ¿Qué evidencia exacta debe guardarse para verificar «memoria durante simulación» en GitHub y Android?
- **Q42.020** ¿Qué criterios de aceptación y regresión permiten declarar completo «memoria durante simulación»?

### Subtema 3: tiempo de respuesta táctil

- **Q42.021** ¿Qué responsabilidad técnica concreta debe cubrir «tiempo de respuesta táctil»?
- **Q42.022** ¿Qué opciones de implementación debemos comparar para «tiempo de respuesta táctil» y con qué criterio?
- **Q42.023** ¿Qué versión de plataforma, formato o API condiciona «tiempo de respuesta táctil»?
- **Q42.024** ¿Qué entradas, salidas y contratos permiten aislar «tiempo de respuesta táctil» del resto del juego?
- **Q42.025** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «tiempo de respuesta táctil»?
- **Q42.026** ¿Cómo se comportaría «tiempo de respuesta táctil» ante fallos, interrupciones y datos inesperados?
- **Q42.027** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «tiempo de respuesta táctil»?
- **Q42.028** ¿Qué cambios pequeños y reversibles permitirían incorporar «tiempo de respuesta táctil» sin alterar el motor actual?
- **Q42.029** ¿Qué evidencia exacta debe guardarse para verificar «tiempo de respuesta táctil» en GitHub y Android?
- **Q42.030** ¿Qué criterios de aceptación y regresión permiten declarar completo «tiempo de respuesta táctil»?

### Subtema 4: consumo de batería

- **Q42.031** ¿Qué responsabilidad técnica concreta debe cubrir «consumo de batería»?
- **Q42.032** ¿Qué opciones de implementación debemos comparar para «consumo de batería» y con qué criterio?
- **Q42.033** ¿Qué versión de plataforma, formato o API condiciona «consumo de batería»?
- **Q42.034** ¿Qué entradas, salidas y contratos permiten aislar «consumo de batería» del resto del juego?
- **Q42.035** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «consumo de batería»?
- **Q42.036** ¿Cómo se comportaría «consumo de batería» ante fallos, interrupciones y datos inesperados?
- **Q42.037** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «consumo de batería»?
- **Q42.038** ¿Qué cambios pequeños y reversibles permitirían incorporar «consumo de batería» sin alterar el motor actual?
- **Q42.039** ¿Qué evidencia exacta debe guardarse para verificar «consumo de batería» en GitHub y Android?
- **Q42.040** ¿Qué criterios de aceptación y regresión permiten declarar completo «consumo de batería»?

### Subtema 5: tamaño de instalación

- **Q42.041** ¿Qué responsabilidad técnica concreta debe cubrir «tamaño de instalación»?
- **Q42.042** ¿Qué opciones de implementación debemos comparar para «tamaño de instalación» y con qué criterio?
- **Q42.043** ¿Qué versión de plataforma, formato o API condiciona «tamaño de instalación»?
- **Q42.044** ¿Qué entradas, salidas y contratos permiten aislar «tamaño de instalación» del resto del juego?
- **Q42.045** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «tamaño de instalación»?
- **Q42.046** ¿Cómo se comportaría «tamaño de instalación» ante fallos, interrupciones y datos inesperados?
- **Q42.047** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «tamaño de instalación»?
- **Q42.048** ¿Qué cambios pequeños y reversibles permitirían incorporar «tamaño de instalación» sin alterar el motor actual?
- **Q42.049** ¿Qué evidencia exacta debe guardarse para verificar «tamaño de instalación» en GitHub y Android?
- **Q42.050** ¿Qué criterios de aceptación y regresión permiten declarar completo «tamaño de instalación»?

### Subtema 6: soporte de texto ampliado

- **Q42.051** ¿Qué responsabilidad técnica concreta debe cubrir «soporte de texto ampliado»?
- **Q42.052** ¿Qué opciones de implementación debemos comparar para «soporte de texto ampliado» y con qué criterio?
- **Q42.053** ¿Qué versión de plataforma, formato o API condiciona «soporte de texto ampliado»?
- **Q42.054** ¿Qué entradas, salidas y contratos permiten aislar «soporte de texto ampliado» del resto del juego?
- **Q42.055** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «soporte de texto ampliado»?
- **Q42.056** ¿Cómo se comportaría «soporte de texto ampliado» ante fallos, interrupciones y datos inesperados?
- **Q42.057** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «soporte de texto ampliado»?
- **Q42.058** ¿Qué cambios pequeños y reversibles permitirían incorporar «soporte de texto ampliado» sin alterar el motor actual?
- **Q42.059** ¿Qué evidencia exacta debe guardarse para verificar «soporte de texto ampliado» en GitHub y Android?
- **Q42.060** ¿Qué criterios de aceptación y regresión permiten declarar completo «soporte de texto ampliado»?

### Subtema 7: lector de pantalla

- **Q42.061** ¿Qué responsabilidad técnica concreta debe cubrir «lector de pantalla»?
- **Q42.062** ¿Qué opciones de implementación debemos comparar para «lector de pantalla» y con qué criterio?
- **Q42.063** ¿Qué versión de plataforma, formato o API condiciona «lector de pantalla»?
- **Q42.064** ¿Qué entradas, salidas y contratos permiten aislar «lector de pantalla» del resto del juego?
- **Q42.065** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «lector de pantalla»?
- **Q42.066** ¿Cómo se comportaría «lector de pantalla» ante fallos, interrupciones y datos inesperados?
- **Q42.067** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «lector de pantalla»?
- **Q42.068** ¿Qué cambios pequeños y reversibles permitirían incorporar «lector de pantalla» sin alterar el motor actual?
- **Q42.069** ¿Qué evidencia exacta debe guardarse para verificar «lector de pantalla» en GitHub y Android?
- **Q42.070** ¿Qué criterios de aceptación y regresión permiten declarar completo «lector de pantalla»?

### Subtema 8: áreas táctiles accesibles

- **Q42.071** ¿Qué responsabilidad técnica concreta debe cubrir «áreas táctiles accesibles»?
- **Q42.072** ¿Qué opciones de implementación debemos comparar para «áreas táctiles accesibles» y con qué criterio?
- **Q42.073** ¿Qué versión de plataforma, formato o API condiciona «áreas táctiles accesibles»?
- **Q42.074** ¿Qué entradas, salidas y contratos permiten aislar «áreas táctiles accesibles» del resto del juego?
- **Q42.075** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «áreas táctiles accesibles»?
- **Q42.076** ¿Cómo se comportaría «áreas táctiles accesibles» ante fallos, interrupciones y datos inesperados?
- **Q42.077** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «áreas táctiles accesibles»?
- **Q42.078** ¿Qué cambios pequeños y reversibles permitirían incorporar «áreas táctiles accesibles» sin alterar el motor actual?
- **Q42.079** ¿Qué evidencia exacta debe guardarse para verificar «áreas táctiles accesibles» en GitHub y Android?
- **Q42.080** ¿Qué criterios de aceptación y regresión permiten declarar completo «áreas táctiles accesibles»?

### Subtema 9: comportamiento sin conexión

- **Q42.081** ¿Qué responsabilidad técnica concreta debe cubrir «comportamiento sin conexión»?
- **Q42.082** ¿Qué opciones de implementación debemos comparar para «comportamiento sin conexión» y con qué criterio?
- **Q42.083** ¿Qué versión de plataforma, formato o API condiciona «comportamiento sin conexión»?
- **Q42.084** ¿Qué entradas, salidas y contratos permiten aislar «comportamiento sin conexión» del resto del juego?
- **Q42.085** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «comportamiento sin conexión»?
- **Q42.086** ¿Cómo se comportaría «comportamiento sin conexión» ante fallos, interrupciones y datos inesperados?
- **Q42.087** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «comportamiento sin conexión»?
- **Q42.088** ¿Qué cambios pequeños y reversibles permitirían incorporar «comportamiento sin conexión» sin alterar el motor actual?
- **Q42.089** ¿Qué evidencia exacta debe guardarse para verificar «comportamiento sin conexión» en GitHub y Android?
- **Q42.090** ¿Qué criterios de aceptación y regresión permiten declarar completo «comportamiento sin conexión»?

### Subtema 10: pruebas de estrés de NPC

- **Q42.091** ¿Qué responsabilidad técnica concreta debe cubrir «pruebas de estrés de NPC»?
- **Q42.092** ¿Qué opciones de implementación debemos comparar para «pruebas de estrés de NPC» y con qué criterio?
- **Q42.093** ¿Qué versión de plataforma, formato o API condiciona «pruebas de estrés de NPC»?
- **Q42.094** ¿Qué entradas, salidas y contratos permiten aislar «pruebas de estrés de NPC» del resto del juego?
- **Q42.095** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «pruebas de estrés de NPC»?
- **Q42.096** ¿Cómo se comportaría «pruebas de estrés de NPC» ante fallos, interrupciones y datos inesperados?
- **Q42.097** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «pruebas de estrés de NPC»?
- **Q42.098** ¿Qué cambios pequeños y reversibles permitirían incorporar «pruebas de estrés de NPC» sin alterar el motor actual?
- **Q42.099** ¿Qué evidencia exacta debe guardarse para verificar «pruebas de estrés de NPC» en GitHub y Android?
- **Q42.100** ¿Qué criterios de aceptación y regresión permiten declarar completo «pruebas de estrés de NPC»?

## Q43 · P1 — ¿Qué pruebas y criterios de aceptación deben superar los hitos antes de integrar ramas o declarar un módulo funcional?

### Subtema 1: tests unitarios de reglas

- **Q43.001** ¿Qué responsabilidad técnica concreta debe cubrir «tests unitarios de reglas»?
- **Q43.002** ¿Qué opciones de implementación debemos comparar para «tests unitarios de reglas» y con qué criterio?
- **Q43.003** ¿Qué versión de plataforma, formato o API condiciona «tests unitarios de reglas»?
- **Q43.004** ¿Qué entradas, salidas y contratos permiten aislar «tests unitarios de reglas» del resto del juego?
- **Q43.005** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «tests unitarios de reglas»?
- **Q43.006** ¿Cómo se comportaría «tests unitarios de reglas» ante fallos, interrupciones y datos inesperados?
- **Q43.007** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «tests unitarios de reglas»?
- **Q43.008** ¿Qué cambios pequeños y reversibles permitirían incorporar «tests unitarios de reglas» sin alterar el motor actual?
- **Q43.009** ¿Qué evidencia exacta debe guardarse para verificar «tests unitarios de reglas» en GitHub y Android?
- **Q43.010** ¿Qué criterios de aceptación y regresión permiten declarar completo «tests unitarios de reglas»?

### Subtema 2: tests de integridad de guardado

- **Q43.011** ¿Qué responsabilidad técnica concreta debe cubrir «tests de integridad de guardado»?
- **Q43.012** ¿Qué opciones de implementación debemos comparar para «tests de integridad de guardado» y con qué criterio?
- **Q43.013** ¿Qué versión de plataforma, formato o API condiciona «tests de integridad de guardado»?
- **Q43.014** ¿Qué entradas, salidas y contratos permiten aislar «tests de integridad de guardado» del resto del juego?
- **Q43.015** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «tests de integridad de guardado»?
- **Q43.016** ¿Cómo se comportaría «tests de integridad de guardado» ante fallos, interrupciones y datos inesperados?
- **Q43.017** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «tests de integridad de guardado»?
- **Q43.018** ¿Qué cambios pequeños y reversibles permitirían incorporar «tests de integridad de guardado» sin alterar el motor actual?
- **Q43.019** ¿Qué evidencia exacta debe guardarse para verificar «tests de integridad de guardado» en GitHub y Android?
- **Q43.020** ¿Qué criterios de aceptación y regresión permiten declarar completo «tests de integridad de guardado»?

### Subtema 3: tests de causalidad de eventos

- **Q43.021** ¿Qué responsabilidad técnica concreta debe cubrir «tests de causalidad de eventos»?
- **Q43.022** ¿Qué opciones de implementación debemos comparar para «tests de causalidad de eventos» y con qué criterio?
- **Q43.023** ¿Qué versión de plataforma, formato o API condiciona «tests de causalidad de eventos»?
- **Q43.024** ¿Qué entradas, salidas y contratos permiten aislar «tests de causalidad de eventos» del resto del juego?
- **Q43.025** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «tests de causalidad de eventos»?
- **Q43.026** ¿Cómo se comportaría «tests de causalidad de eventos» ante fallos, interrupciones y datos inesperados?
- **Q43.027** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «tests de causalidad de eventos»?
- **Q43.028** ¿Qué cambios pequeños y reversibles permitirían incorporar «tests de causalidad de eventos» sin alterar el motor actual?
- **Q43.029** ¿Qué evidencia exacta debe guardarse para verificar «tests de causalidad de eventos» en GitHub y Android?
- **Q43.030** ¿Qué criterios de aceptación y regresión permiten declarar completo «tests de causalidad de eventos»?

### Subtema 4: tests de conocimiento secreto

- **Q43.031** ¿Qué responsabilidad técnica concreta debe cubrir «tests de conocimiento secreto»?
- **Q43.032** ¿Qué opciones de implementación debemos comparar para «tests de conocimiento secreto» y con qué criterio?
- **Q43.033** ¿Qué versión de plataforma, formato o API condiciona «tests de conocimiento secreto»?
- **Q43.034** ¿Qué entradas, salidas y contratos permiten aislar «tests de conocimiento secreto» del resto del juego?
- **Q43.035** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «tests de conocimiento secreto»?
- **Q43.036** ¿Cómo se comportaría «tests de conocimiento secreto» ante fallos, interrupciones y datos inesperados?
- **Q43.037** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «tests de conocimiento secreto»?
- **Q43.038** ¿Qué cambios pequeños y reversibles permitirían incorporar «tests de conocimiento secreto» sin alterar el motor actual?
- **Q43.039** ¿Qué evidencia exacta debe guardarse para verificar «tests de conocimiento secreto» en GitHub y Android?
- **Q43.040** ¿Qué criterios de aceptación y regresión permiten declarar completo «tests de conocimiento secreto»?

### Subtema 5: tests de consistencia NPC

- **Q43.041** ¿Qué responsabilidad técnica concreta debe cubrir «tests de consistencia NPC»?
- **Q43.042** ¿Qué opciones de implementación debemos comparar para «tests de consistencia NPC» y con qué criterio?
- **Q43.043** ¿Qué versión de plataforma, formato o API condiciona «tests de consistencia NPC»?
- **Q43.044** ¿Qué entradas, salidas y contratos permiten aislar «tests de consistencia NPC» del resto del juego?
- **Q43.045** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «tests de consistencia NPC»?
- **Q43.046** ¿Cómo se comportaría «tests de consistencia NPC» ante fallos, interrupciones y datos inesperados?
- **Q43.047** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «tests de consistencia NPC»?
- **Q43.048** ¿Qué cambios pequeños y reversibles permitirían incorporar «tests de consistencia NPC» sin alterar el motor actual?
- **Q43.049** ¿Qué evidencia exacta debe guardarse para verificar «tests de consistencia NPC» en GitHub y Android?
- **Q43.050** ¿Qué criterios de aceptación y regresión permiten declarar completo «tests de consistencia NPC»?

### Subtema 6: tests de cálculos con límites

- **Q43.051** ¿Qué responsabilidad técnica concreta debe cubrir «tests de cálculos con límites»?
- **Q43.052** ¿Qué opciones de implementación debemos comparar para «tests de cálculos con límites» y con qué criterio?
- **Q43.053** ¿Qué versión de plataforma, formato o API condiciona «tests de cálculos con límites»?
- **Q43.054** ¿Qué entradas, salidas y contratos permiten aislar «tests de cálculos con límites» del resto del juego?
- **Q43.055** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «tests de cálculos con límites»?
- **Q43.056** ¿Cómo se comportaría «tests de cálculos con límites» ante fallos, interrupciones y datos inesperados?
- **Q43.057** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «tests de cálculos con límites»?
- **Q43.058** ¿Qué cambios pequeños y reversibles permitirían incorporar «tests de cálculos con límites» sin alterar el motor actual?
- **Q43.059** ¿Qué evidencia exacta debe guardarse para verificar «tests de cálculos con límites» en GitHub y Android?
- **Q43.060** ¿Qué criterios de aceptación y regresión permiten declarar completo «tests de cálculos con límites»?

### Subtema 7: tests de interfaz responsiva

- **Q43.061** ¿Qué responsabilidad técnica concreta debe cubrir «tests de interfaz responsiva»?
- **Q43.062** ¿Qué opciones de implementación debemos comparar para «tests de interfaz responsiva» y con qué criterio?
- **Q43.063** ¿Qué versión de plataforma, formato o API condiciona «tests de interfaz responsiva»?
- **Q43.064** ¿Qué entradas, salidas y contratos permiten aislar «tests de interfaz responsiva» del resto del juego?
- **Q43.065** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «tests de interfaz responsiva»?
- **Q43.066** ¿Cómo se comportaría «tests de interfaz responsiva» ante fallos, interrupciones y datos inesperados?
- **Q43.067** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «tests de interfaz responsiva»?
- **Q43.068** ¿Qué cambios pequeños y reversibles permitirían incorporar «tests de interfaz responsiva» sin alterar el motor actual?
- **Q43.069** ¿Qué evidencia exacta debe guardarse para verificar «tests de interfaz responsiva» en GitHub y Android?
- **Q43.070** ¿Qué criterios de aceptación y regresión permiten declarar completo «tests de interfaz responsiva»?

### Subtema 8: tests de regresión entre ramas

- **Q43.071** ¿Qué responsabilidad técnica concreta debe cubrir «tests de regresión entre ramas»?
- **Q43.072** ¿Qué opciones de implementación debemos comparar para «tests de regresión entre ramas» y con qué criterio?
- **Q43.073** ¿Qué versión de plataforma, formato o API condiciona «tests de regresión entre ramas»?
- **Q43.074** ¿Qué entradas, salidas y contratos permiten aislar «tests de regresión entre ramas» del resto del juego?
- **Q43.075** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «tests de regresión entre ramas»?
- **Q43.076** ¿Cómo se comportaría «tests de regresión entre ramas» ante fallos, interrupciones y datos inesperados?
- **Q43.077** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «tests de regresión entre ramas»?
- **Q43.078** ¿Qué cambios pequeños y reversibles permitirían incorporar «tests de regresión entre ramas» sin alterar el motor actual?
- **Q43.079** ¿Qué evidencia exacta debe guardarse para verificar «tests de regresión entre ramas» en GitHub y Android?
- **Q43.080** ¿Qué criterios de aceptación y regresión permiten declarar completo «tests de regresión entre ramas»?

### Subtema 9: benchmarks Android

- **Q43.081** ¿Qué responsabilidad técnica concreta debe cubrir «benchmarks Android»?
- **Q43.082** ¿Qué opciones de implementación debemos comparar para «benchmarks Android» y con qué criterio?
- **Q43.083** ¿Qué versión de plataforma, formato o API condiciona «benchmarks Android»?
- **Q43.084** ¿Qué entradas, salidas y contratos permiten aislar «benchmarks Android» del resto del juego?
- **Q43.085** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «benchmarks Android»?
- **Q43.086** ¿Cómo se comportaría «benchmarks Android» ante fallos, interrupciones y datos inesperados?
- **Q43.087** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «benchmarks Android»?
- **Q43.088** ¿Qué cambios pequeños y reversibles permitirían incorporar «benchmarks Android» sin alterar el motor actual?
- **Q43.089** ¿Qué evidencia exacta debe guardarse para verificar «benchmarks Android» en GitHub y Android?
- **Q43.090** ¿Qué criterios de aceptación y regresión permiten declarar completo «benchmarks Android»?

### Subtema 10: criterios de aprobación de cada PR

- **Q43.091** ¿Qué responsabilidad técnica concreta debe cubrir «criterios de aprobación de cada PR»?
- **Q43.092** ¿Qué opciones de implementación debemos comparar para «criterios de aprobación de cada PR» y con qué criterio?
- **Q43.093** ¿Qué versión de plataforma, formato o API condiciona «criterios de aprobación de cada PR»?
- **Q43.094** ¿Qué entradas, salidas y contratos permiten aislar «criterios de aprobación de cada PR» del resto del juego?
- **Q43.095** ¿Qué riesgo de corrupción, pérdida de datos o incompatibilidad introduce «criterios de aprobación de cada PR»?
- **Q43.096** ¿Cómo se comportaría «criterios de aprobación de cada PR» ante fallos, interrupciones y datos inesperados?
- **Q43.097** ¿Qué límites de latencia, memoria, batería o espacio se necesitan medir para «criterios de aprobación de cada PR»?
- **Q43.098** ¿Qué cambios pequeños y reversibles permitirían incorporar «criterios de aprobación de cada PR» sin alterar el motor actual?
- **Q43.099** ¿Qué evidencia exacta debe guardarse para verificar «criterios de aprobación de cada PR» en GitHub y Android?
- **Q43.100** ¿Qué criterios de aceptación y regresión permiten declarar completo «criterios de aprobación de cada PR»?
