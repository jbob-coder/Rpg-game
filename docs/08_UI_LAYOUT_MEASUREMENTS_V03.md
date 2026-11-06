# 08. Auditoría de márgenes y ratios — UI blueprint v0.3

**Fecha:** 2026-11-05 · **Estado:** observaciones de pruebas locales de navegador Chromium, **no prueba de APK/Android físico**.

## Correcciones incorporadas

1. Unificar el inset lateral del header, subtabs, cuerpo y dock usando `--pad` (12 CSS px en <360; 16 CSS px entre 360 y 599; 24 CSS px desde 600 dentro del contenedor centrado).
2. Unificar `--touch:48px` como mínimo visual para controles de header, pestañas, filtros y selección; details de estadísticas reciben área de activación de 48 px.
3. Evitar deformación de números largos con `overflow-wrap:anywhere`.
4. Reducir adornos del header en pantallas muy bajas con texto ampliado, sin alterar la lógica RPG.
5. Mantener tamaño de lectura adaptable y la posibilidad de plegar decisiones.

## Medidas observadas en Chromium

Viewport CSS | lectura con opciones | lectura plegada | ganancia | margen de contenido/encabezado/pestañas
---|---:|---:|---:|---
320×480 | 203 | 288 | +85 | 12 / 12 / 12
320×640 | 307 | 448 | +141 | 12 / 12 / 12
360×780 | 427 | 591 | +164 | 16 / 16 / 16
390×844 | 491 | 655 | +164 | 16 / 16 / 16
412×915 | 562 | 726 | +164 | 16 / 16 / 16
768×1024 | 671 | 835 | +164 | 49 / 49 / 49

Unidades en **CSS px**, no píxeles de hardware ni dp de una implementación nativa. A 768 px el app se centra hasta 720 px de ancho, por eso el inset visto desde el viewport es 49 px. Las medidas se obtuvieron con barras del sistema simuladas a cero; la implementación final debe respetar insets Android.

## Alcance y resultado de pruebas

- Se ejecutó una prueba de Playwright con **11 pantallas/estados funcionales de presentación × dos modos tipográficos × seis viewports = 132 estados**.
- Ningún control visible medido quedó por debajo de 48×48 CSS px; no se detectó desbordamiento horizontal del documento ni errores de JS.
- El margen izquierdo de contenido, header y primera subpestaña coincidió dentro de 1.5 px en todos los estados.
- Cambiar categorías Skills sincroniza detalle; se puede volver a mostrar el dock de decisiones.
- La prueba reproducible está en `design/ui/tests/test_layout_v03.py`.

## Qué NO se ha verificado

No existe QA de un APK, dispositivo Android físico, barras seguras reales, TalkBack, localización completa, composición nativa ni motor RPG. Mínimos táctiles en CSS px son aproximaciones de diseño, no prueba de cumplimiento en dp. Las ocho imágenes originales siguen pendientes de incorporarse como binarios.
