# 04. Sistema visual y estructura responsiva — RPG móvil
**Estado:** especificación de interfaz v0.2 (diseño; no implementación)  
**Fecha:** 2026-11-05 · **Destino:** Android en vertical, RPG narrativo independiente, sin mapas.

## 1. Autoridad de diseño
Las ocho imágenes aportadas por el propietario son **referencias visuales principales** del lenguaje negro/dorado. No son capturas de una aplicación probada ni requisitos mecánicos infalibles. Ante una inconsistencia prevalecen, en orden:
1. Decisiones explícitas del propietario y reglas confirmadas en `docs/01` y `docs/02`.
2. Este contrato de diseño y las fichas funcionales de `docs/05`.
3. Aspecto visual de las referencias, interpretado para pantallas reales.
4. Textos, cifras, clases y efectos dibujados a modo de ejemplo en las imágenes (no canon).

La experiencia es **text-first**: los íconos y líneas ornamentales sí pueden existir en la interfaz, pero no habrá mapa, minimapa, terreno, mundo 3D, retratos de personajes ni ilustraciones obligatorias de escenarios. Una pestaña denominada «World» en una imagen no autoriza un mapa.

## 2. Lenguaje visual compartido
- **Fondo** carbón casi negro; **superficies** elevadas distinguibles; **acento** oro envejecido reservado para selección, progresión y acción principal. No llenar de destellos todos los bordes.
- Paleta inicial *propuesta para prototipar* (no valores aprobados de marca): `canvas #0C0F14`, `surface #161A20`, `raised #20252C`, `border #51432D`, `accent #D9AE56`, `primaryText #F1EDE6`, `secondaryText #B9B4AA`, `disabled #8E8D8C`, `danger #DC776F`. Verificar contraste antes de fijar colores; no depender solo del color para estados.
- Tipografía: una fuente legible para cuerpo/datos; una decorativa **solo** para títulos breves si supera pruebas de lectura. Valores base propuestos: narración 16–18 sp, títulos 22–26 sp, encabezados 18–20 sp, controles 14–16 sp y metadatos 13–14 sp. Evitar 9–11 sp de las maquetas.
- Escala espacial de 4/8 dp: separación interior 12–16 dp; entre tarjetas 12–16 dp; margen lateral 16 dp (12 dp solo en anchuras estrechas); esquinas 8–12 dp; no encerrar cada palabra en otra tarjeta.
- Jerarquía recurrente: **1 título principal → 1 resumen breve → contenido primario → contenido secundario expandible → 1 acción principal**. Como máximo una acción de énfasis fuerte por pantalla o segmento.
- Iconos solo como refuerzo semántico; toda función necesita etiqueta legible; rareza y bloqueos con texto además del color. Reducir brillo, degradados y adornos en listas densas.

## 3. Shell persistente
Pantalla normal en vertical:
```text
┌──────────────────────────────────┐
│ Sistema Android / zona segura    │
├──────────────────────────────────┤
│ Encabezado: volver · Título · ⋯  │  48–56 dp objetivo
│ [Subnavegación si corresponde]   │  desplazable sin truncar
├──────────────────────────────────┤
│                                  │
│  CONTENIDO CON SCROLL VERTICAL   │  flex: ocupa lo disponible
│  (una columna principal)         │
│                                  │
│  Secciones secundarias plegables │
│                                  │
├──────────────────────────────────┤
│ Acciones contextuales (si hay)   │  se adapta al contenido
├──────────────────────────────────┤
│ Story Character Inventory More   │  56–72 dp + safe-area
└──────────────────────────────────┘
```
La barra inferior muestra pocos destinos globales. «Skills» puede ser acceso rápido a **Character → Skills** si se conserva del diseño original; no debe abrir un sistema duplicado. «Quests/Journal» puede vivir en More o como destino si pruebas justifican su frecuencia. **«World» no abre mapas**: eliminarlo o sustituirlo por una función narrativa explícitamente aprobada.

Dentro de Character, `Overview | Stats | Skills | Abilities | Class | Background` funciona como una **barra de pestañas horizontal desplazable**, no como seis mini-columnas comprimidas. La pestaña activa conserva posición al volver. Menú global y submenú no compiten visualmente.

## 4. Reglas de medidas y distribución
Utilizar **dp/sp y espacio disponible real** tras barras del sistema, teclado, accesibilidad e insets. No diseñar como una foto fija de 1024×1536.
- 320–359 dp de ancho: **una sola columna**, tarjetas apiladas; botón de acción en ancho completo; categorías como filtros horizontales o selector. Encabezado simplificado.
- 360–479 dp: una columna; solo pares de métricas muy breves si ambas mantienen lectura y toque seguro.
- 480–599 dp: mayor ancho interior con límite de línea; evitar estirar el texto de lado a lado.
- 600 dp o más: contenedor de lectura con ancho máximo aproximado de 600–720 dp; **dos columnas solo donde aporten comparación** y no oculten contenido por dependencia cruzada.
- La historia debe ocupar el **máximo espacio flexible**. Como objetivo inicial, en modo lectura narrativa ≥55% del área de contenido libre cuando las acciones se pueden plegar; no es una altura fija ni un resultado de prueba. Si el texto no cabe, scroll vertical; nunca recortar o reducir a microtipografía.
- Zona táctil mínima propuesta 48×48 dp, espaciado entre acciones 8 dp, elementos interactivos claramente diferenciados.
- No usar scroll horizontal en fichas de estadísticas ni texto narrativo. El árbol de habilidades **puede ofrecer panorámica/zoom** en su lienzo, pero siempre incluye alternativa estructurada en lista accesible.
- Cuando la altura útil es poca (teclado, modo horizontal, pantallas pequeñas), colapsar adornos, resumen y opciones secundarias antes de reducir fuente. La barra de acciones puede convertirse en hoja inferior expandible.

## 5. Prioridad de contenido por estado
- **Story:** escena, prosa legible y opciones activas; cifras, inventario y diario quedan en sus destinos.
- **Character Overview:** identidad y condición general; detalles numéricos extensos, fuera.
- **Stats:** atributos y estadísticas derivadas, agrupados; expandir para información secundaria.
- **Skills:** competencia/progreso de destrezas y acciones de mejora; categorías primero, detalle después.
- **Abilities:** habilidad y árbol de ramas dependientes de clase; desbloqueo y requisitos sin temporizadores/cooldowns.
- **Class:** clase actual, clases elegibles, requisitos, progreso. Evitar pantallas contradictorias de «sin clase» después de confirmar la inicial.
- **Background:** origen inmutable y registro cronológico descubierto; no reabrir selector de creación.
- **Nueva partida:** flujo dedicado para identidad, clase y background antes de entrar a Story.

## 6. Estados obligatorios
Cada componente interactivo debe especificar `default`, `selected`, `locked`, `unavailable`, `loading`, `empty`, `error` y `success` cuando aplique; no convertir `locked` en un botón accionable ambiguo. Explicar requisitos de bloqueo, ocultar información secreta y no prometer efectos que aún no estén implementados. Usar etiquetas y descripciones accesibles.

## 7. Validación — plan, no resultados
Revisar en 320×640, 360×780, 390×844, 412×915 y 768×1024 **como viewports de referencia**, y al menos un Android físico si se implementa. Probar fuente 100%, 150%, 200%; títulos largos; texto en español/inglés; 0, 1, 5 y 12 opciones; 0 y muchas habilidades; árbol con 20+ nodos; teclado visible; interrupción/reanudación; TalkBack; estados bloqueados; contraste y ausencia de overflow. La revisión exige capturas y comprobación funcional; todavía **no se ha ejecutado**.
