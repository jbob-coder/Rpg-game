# 07. Blueprint de UI y separación de responsabilidades

**Estado:** arquitectura propuesta para futura implementación; no se ha programado ni probado el juego.  
**Proyecto:** RPG narrativo independiente, Android, sin mapa. **Fecha:** 2026-11-05.

## Propósito

Las ocho imágenes principales son **referencias de apariencia**, no código ni archivos listos para usarse como texturas o sprites. Se debe construir primero un layout medible y adaptable; después se diseñan sus íconos, bordes y texturas; finalmente se implementa el comportamiento.

**«Mesh» aquí significa malla de distribución de UI, no una malla 3D.** No se pretende recortar cada screenshot en botones funcionales: eso fijaría tamaños incorrectos, texto obsoleto y defectos de alineación.

La separación técnica protege el motor del RPG frente a cambios visuales y permite reemplazar una textura sin rehacer los controles.

## Capas independientes (lógicas, no necesariamente procesos separados)

| Capa | Responsabilidad | No debe hacer |
|---|---|---|
| 1. **Design tokens y skins** | Colores, tipografía, marcos, íconos, texturas, estados visuales; recursos mediante IDs estables | Decidir requisitos de clase o modificar vida/XP |
| 2. **Componentes UI reutilizables** | Botones, tarjetas, tabs, indicadores, árboles/listas y acceso táctil; usan tokens y estilos | Conocer reglas narrativas, acceso directo a guardados |
| 3. **Layout y pantallas** | Composición responsive de Story, Overview, Stats, Skills, Abilities, Class, Background, creación | Aplicar XP, desbloquear habilidades o avanzar eventos por su cuenta |
| 4. **Adaptadores / ViewModels** | Convertir estado del juego en datos presentables; despachar acciones tipadas y representar loading/locked/error | Duplicar cálculos del dominio, inventar hechos ocultos |
| 5. **Dominio y simulación (backend lógico)** | Creación, validación, clases, atributos, skills, ability tree, mundo autónomo, decisiones, reloj y cadenas de eventos | Conocer tamaños dp, colores, PNG, botones o pestañas |
| 6. **Persistencia** | Guardar/cargar estado versionado, snapshots, eventos, migraciones y recuperación | Elegir diseño visual; sobrescribir hechos históricos por estética |

En Android estas capas **pueden ejecutarse dentro de una sola aplicación, incluso sin internet**. «Frontend/backend» describe responsabilidades y límites; **no exige servidores ni una arquitectura en red**.

## Esquema de dependencias

```text
[Design Tokens]       [Texture/Icon Catalog]
       \                    /
        → [Reusable UI Components] 
                   ↓
          [Screens + Layout]
                   ↓
           [ViewModels/Adapters]
                   ↓   typed commands / immutable read models
             [Game Domain]
                   ↓
         [Save + Event Storage]

[World Simulation] → [Game Domain / Event Queue]
(advances independently of which screen is open)
```

Regla principal: **las capas superiores dependen de contratos estables de las inferiores; el dominio no importa componentes, pantallas ni texturas**. La simulación puede continuar aunque el jugador esté en Inventory o Character.

## Blueprint geométrico, no coordenadas pegadas a las fotos

El viewport útil se obtiene después de áreas seguras, barras del sistema y teclado. Usar restricciones y contenido flexible, no recortes con posición absoluta:

```text
┌────────────────────────────────────┐
│ ANDROID SAFE AREA                  │
│ HEADER compacto / título           │
│ SUBTABS (solo cuando corresponde)  │
├────────────────────────────────────┤
│ CONTENIDO DE LA PANTALLA           │
│ - panel prioritario                │
│ - secciones y recuadros apilados   │
│ - detalles secundarios plegables   │
│ - scroll vertical según necesidad  │
├────────────────────────────────────┤
│ ACCIÓN CONTEXTUAL (si corresponde) │
│ NAVEGACIÓN GLOBAL CONSISTENTE      │
│ ANDROID SAFE AREA                  │
└────────────────────────────────────┘
```

Reglas iniciales propuestas (se validarán, no son pruebas realizadas): márgenes 12 dp en teléfonos muy estrechos y 16 dp en el resto; espacios base de 8/12/16 dp; objetivos táctiles mínimo 48×48 dp; body 16–18 sp; una columna principal bajo 600 dp; el contenido central crece y desplaza, mientras las zonas persistentes ocupan su altura necesaria. Las proporciones cambian con el texto, tamaño de fuente y pantalla: no se fija un «40% exacto» de historia universal.

Cada pantalla utiliza el **mismo Shell**, sin copiar y pegar navegación, márgenes ni widgets. Las fichas por panel W0–W8 ya están en [05. Wireframes](05_PANEL_WIREFRAMES_AND_INTERACTION_CONTRACT.md). Los tokens y tamaños iniciales están en [04. Sistema visual](04_UI_DESIGN_SYSTEM_AND_RESPONSIVE_LAYOUT.md).

## Componentes que conviene definir antes de programar

- **ShellScreen**: safe areas, header, subtabs opcionales, scroll y barra global.
- **RpgButton**: label, iconId opcional, estado, acción y skinId; área táctil separada del arte.
- **RpgCard**: título, contenido, estado expandido, variante de densidad y borde.
- **StatRow**: etiqueta, valor, unidad, fuente/modificadores; no asigna puntos por sí mismo.
- **ProgressMeter**: valor/máximo del ViewModel, texto alternativo y apariencia intercambiable.
- **SkillEntry**: competencia, progreso, requisito, acción validada por dominio.
- **AbilityNode / AbilityTreeView**: ID estable, conexiones, requisito, estado, detalle; alternativa en lista accesible; **sin cooldown**.
- **HistoryEntry**: fecha, hecho conocido, fuente, consecuencia; origen fijado al crear personaje.
- **NarrativeChoice**: ID de elección, descripción, estado, requisitos conocidos; acción no altera el mundo directamente.

Estos nombres son **propuestas de contrato**, no clases implementadas ni decisiones de framework.

## Interfaz de datos entre UI y dominio (contrato de ejemplo)

Los ViewModels reciben **read models** inmutables, con IDs y versión. No se transmite una captura renderizada como estado del juego.

```json
{
  "view_model_version": 1,
  "panel": "abilities",
  "character_id": "character-001",
  "class": { "id": "class-001", "display_name": "Ejemplo", "unlocked": true },
  "nodes": [
    {
      "id": "ability-001",
      "label": "Ejemplo",
      "state": "locked",
      "known_requirements": ["class-002"]
    }
  ]
}
```

Ejemplo ilustrativo **no canon**. La UI puede mostrar la condición y un candado. Para desbloquear, envía un comando con `character_id` y `ability_id`; el dominio valida elegibilidad **en ese momento**. No se otorga la habilidad porque el usuario pulse un botón. No exponer al ViewModel los hechos del mundo que el personaje aún desconoce.

Versionar contratos, distinguir campos opcionales y desconocidos, tolerar datos faltantes y mantener identificadores estables incluso si se traduce o cambia el nombre visible.

## Capas de arte sobre un botón

```text
[Hit area accesible: ≥48 dp]
  ├─ background / nine-slice / vector frame
  ├─ skin tint / estado normal, pressed, disabled, selected
  ├─ icon layer (assetId, tamaño y padding)
  ├─ label + contenido dinámico
  └─ focus / feedback / accessibility label
```

El botón y su lógica **no dependen del PNG**. La textura puede reemplazarse mediante `skinId` o `assetId` y un manifest central, con alternativas si falta un recurso. Evitar incrustar imágenes de los screenshots con texto renderizado: texto, valores e íconos se dibujan como capas separadas. Si se utiliza **nine-slice** para marcos, definir esquinas protegidas y zona central estirable, sin deformar bordes. Probar resoluciones y densidades. El formato definitivo (PNG, vector, atlas, etc.) depende del engine elegido; no fijar APIs hasta verificarlo.

En el catálogo de íconos se usarán nombres semánticos (por ejemplo `nav.story`, `nav.character`, `state.locked`, `action.confirm`), no rutas de archivo codificadas en cada pantalla. Un ícono obsoleto se sustituye una sola vez.

## Matriz de cambios sin romper otras capas

| Si se modifica… | Debe cambiar | No debería cambiar |
|---|---|---|
| Color, borde, textura o ícono | Tokens/skins/asset catalog | Lógica de XP, evento, guardado |
| Márgenes, ratio, tamaño de tarjetas | Layout y quizá sus pruebas visuales | Reglas de clase y narración |
| Nombre visible de pestaña/habilidad | Datos de presentación/localización | ID estable, progreso guardado |
| Orden y estructura de un panel | Composición UI y tests de navegación | Cálculos de personaje |
| Requisitos de Ability Tree | Dominio, datos y tests funcionales; UI recibe nuevo estado | Apariencia global del botón |
| Nuevos eventos narrativos | Datos/reglas de eventos y tests de simulación | Componentes globales del shell |
| Cambios al formato de guardado | Esquema/migraciones + tests de compatibilidad | Recursos gráficos |

No se garantizan cambios «sin tocar nada»: hay modificaciones de contratos que requieren actualización coordinada y pruebas. La meta es **confinar el impacto**, no ocultar dependencias reales.

## Reglas de persistencia y coherencia

- La selección inicial de Class y Background se confirma en creación; la pantalla Character → Background sigue siendo un registro, no un selector que reescribe el pasado.
- **Skills** y **Abilities** son sistemas distintos; Ability Proficiency y Ability Tree conservan nombres y requisitos ya acordados. Ramas bloqueadas sin cooldowns.
- Los eventos del mundo nacen de la simulación y las cadenas causales, no del montaje de una pantalla; cada UI recibe solo el conocimiento revelado al jugador.
- Serialización y migración deben permitir cargar partidas anteriores después de añadir íconos, reordenar paneles o evolucionar el motor.

## Verificación obligatoria cuando exista implementación

1. Probar navegación y estados de cada panel de forma aislada, con datos falsos y sin backend real.
2. Probar el dominio sin interfaz (creación, habilidades bloqueadas, eventos por tiempo, elecciones y guardados).
3. Prueba de contrato ViewModel ↔ dominio: IDs estables, condiciones, opciones y errores; sin filtración de secretos.
4. Pruebas visuales de 320×640, 360×780, 390×844, 412×915 y tablet; también 150% y 200% de fuente; no overflow ni controles cortados.
5. Sustituir skin/icono por otro sin modificar código de dominio; añadir/remover una sección sin romper navegación.
6. Guardar/cargar durante eventos; tras reiniciar, origen, clase, habilidad y cola de consecuencias persisten.
7. Verificación final en hardware Android real y con lector de pantalla.

**Estado real:** este documento es una especificación; no hay componentes ni tests ejecutables creados por este cambio, y todavía faltan los binarios de las ocho referencias en el repositorio.
