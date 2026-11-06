# 06. Registro de referencias visuales, inconsistencias y decisiones
**Estado:** auditoría de diseño v0.2 · **Fecha:** 2026-11-05

## Inventario de las **últimas ocho** referencias principales
Los nombres corresponden a imágenes proporcionadas en la conversación. **El inventario de nombre/huella no afirma que los binarios estén subidos a GitHub**. Carpeta prevista: \`assets/ui-references/\`; conservar originales fuera de producción y crear versiones optimizadas para el repositorio cuando el transporte de archivos lo permita. No copiar textos o números como valores finales.

| ID | Nombre de origen | Pantalla observada | Autoridad de uso |
|---|---|---|---|
| R01 | \`A147F328-E162-4F6E-A9D1-51358CD08725.jpeg\` | «Origin Selection (Pre-Game)», Noble Heir/Epic, Background Log | Base estética de creación; separar selección de registro posterior |
| R02 | \`90A6E593-BEBA-4BFA-924E-848F416E6717.jpeg\` | Character → Class y «Class Ability Tree» | Jerarquía de clase, no árbol mecánico duplicado |
| R03 | \`14D05893-C3A1-4801-A7D7-17919927BA1D(1).jpeg\` | Abilities: «Ability Proficiency» y «Combat Ability Tree» | Estructura de ramas complejas; renombrar árbol a «Ability Tree» |
| R04 | \`B383EA14-99DD-4647-8F70-3827E82D4E1F(1).jpeg\` | Abilities: «Ability Sets» y panel bloqueado | **Legada** para nomenclatura; útil solo para estados vacíos/bloqueados |
| R05 | \`BC3E0150-9FA2-4BD8-B564-93C13A1CE9F0.jpeg\` | Skills: categorías, árbol y Sword Mastery | Inspiración de jerarquía; apilar en móviles |
| R06 | \`68FE604C-513E-45C8-B517-22B726FA05D3.jpeg\` | Stats: atributos, combate, resistencia, crecimiento | Taxonomía; reemplazar columnas comprimidas |
| R07 | \`4B860E68-3A0B-45F4-9648-283F6FD9CB29.jpeg\` | Character → Overview | Resumen compacto; reducir duplicaciones |
| R08 | \`IMG_6607.jpeg\` | Story: The Market Square y opciones | Referencia principal de lectura y opciones |

Referencia adicional anterior **X01** (NO parte de las últimas ocho): \`EAE02F15-800E-46F3-92E8-FCC8CE4BAFB9.jpeg\`, variante Skills con varias columnas. Se conserva como evidencia del proceso, pero no debe prevalecer sobre la versión de Skills más reciente.

### Integridad de las ocho imágenes de origen (SHA-256)
\`\`\`
R01 3a20f8bc77ff4230b8d34569e9d014f7292e2d45a4a0e196cf856d210554b0a9
R02 d6ee5df3e2b8d1c4960575d51bda7bc4612f8ba09d0720046ecc40505f5bd1da
R03 7a73d5c1c8c20fa77acffbeb5d413d2e1ef57993eb20e26c40302df85e73f8de
R04 2fa468eb6175fbafeda6c321d25bd75b4908cf5ecbd81918bd9cdd65683ba3e2
R05 79361e62b260578131a0c73bacb0489a76c7081062e0d1ed4508e98c154ac4b5
R06 afeacaa7631e82c03d28f1a488d4445fa7d1f0f65539c026ebdbb22b12d505eb
R07 3796b889aed9312c05dbf88a279ac34d4f03696f0616eb688b7ec2aa28e666e1
R08 b4f4c3fa26753b19964d31f75c09ef98e76646a74fa130465d1042242ff9f138
\`\`\`

## Registro de inconsistencias y resolución
| ID | Conflicto en referencias | Regla de resolución | Estado |
|---|---|---|---|
| C01 | R04 «Ability Sets» vs R03 «Ability Proficiency» | Adoptar **Ability Proficiency** | Confirmado por propietario |
| C02 | «Combat Ability Tree» / «Class Ability Tree» vs árbol único | Usar **Ability Tree**; filtro por clase | Confirmado nombre; integración propuesta |
| C03 | Cooldowns/temporizadores en habilidades antiguas | **Eliminar todos los cooldowns de abilities** | Confirmado |
| C04 | Árbol accesible vs ramas cerradas | Las ramas se muestran bloqueadas cuando faltan clase/requisitos | Confirmado |
| C05 | Pantalla R01 dice pregame, pero Background debe permanecer | Crear selector inicial independiente; Character → Background muestra historial sin editar origen | Confirmado |
| C06 | R02 muestra «No Class Selected» mientras se elige clase antes del juego | Solo puede mostrarse **durante creación** o en guardados excepcionales; en partida usar clase confirmada | Regla de coherencia |
| C07 | R05/R06/R03 comprimen 2–3 columnas densas en retrato | Un solo flujo apilado <600 dp; categorías/filtros y detalles progresivos | Corrección de usabilidad |
| C08 | Barras inferiores varían y algunas incluyen «World» | Shell compartido; no crear mapa ni destino cartográfico | Sin mapa confirmado |
| C09 | Tamaño de fuente y botones diminutos en varios mockups | Fuente escalable y toques ≥48 dp; texto visible sin zoom | Corrección de accesibilidad |
| C10 | Rareza «Noble» vs «Epic» | R01 muestra trasfondo Noble Heir con rareza **Epic** | Confirmado |
| C11 | Skills y Abilities parecen árboles intercambiables | Skills = competencias/dominio; Abilities = árbol dependiente de clase | Separación funcional recomendada |
| C12 | Opciones y escenas parecen historia completamente accionada por jugador | Motor de eventos autónomos también altera el mundo, con conocimiento diferido | Confirmado |
| C13 | Números, nombres, barras y SP de las imágenes son demostrativos | No adoptar valores ni reglas sin decisión y pruebas | Pendiente de balance |

## Política de implementación
- **No reproducir exactamente** una captura con defectos: reconstruir la **intención** y dejar una nota de desviación.
- Mantener equivalencia funcional entre títulos, tabs, estados, desbloqueos y navegación en todas las pantallas.
- No agregar mapas, geografías visuales ni contenido de otros proyectos.
- Bloqueos tienen explicación; cambios narrativos afectan registros pertinentes sin sobrescribir origen.
- Revisión visual se hace **contra capturas de la implementación** en varios tamaños y contra la matriz C01–C13.

## Pendientes no resueltos (no inventar)
Lista final de clases y backgrounds; condiciones de desbloqueo; costos y puntos; taxonomía final de Stats/Skills; iconografía definitiva; compatibilidad de las clases de inicio con las avanzadas; comportamiento del tiempo sin sesión; navegación global definitiva; motor/engine final; nombres y lore canon; eventual fuente decorativa; accesibilidad auditada.

## Entregables y verificación
- \`docs/04\`: diseño maestro y reglas responsivas.
- \`docs/05\`: esquemas funcionales W0–W8 y aceptación.
- \`docs/06\`: registro de imágenes R01–R08 y decisiones C01–C13.
- **Pendiente:** subir originales/derivados de R01–R08 como archivos de imagen a \`assets/ui-references/\` y comparar sus hashes.
- **Pendiente:** maquetas de baja fidelidad, prototipo ejecutable, pruebas Android, screenshots y APK.

La existencia de documentación **no es implementación ni validación del juego**.
