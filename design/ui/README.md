# UI layout contract — schema v1

This directory holds a **design-only, engine-independent layout contract** for the standalone Android text RPG. It is a **blueprint**, not gameplay code or final art.

- `layout-schema.v1.json`: machine-readable shell, responsive rules, eight reference mappings, per-screen blocks, UI components, and boundaries between presentation and the RPG domain.
- `docs/04_UI_DESIGN_SYSTEM_AND_RESPONSIVE_LAYOUT.md`: dimensions, typographic and touch targets.
- `docs/05_PANEL_WIREFRAMES_AND_INTERACTION_CONTRACT.md`: individual panel wireframes.
- `docs/06_UI_REFERENCE_REGISTER_AND_INCONSISTENCIES.md`: thirteen conflicts and their resolutions.
- `docs/07_UI_LAYOUT_COMPONENTS_AND_LAYERS.md`: frontend/domain/persistence boundaries.

## Validation
Schema structure was checked for six Character tabs, eleven screen definitions, eight numbered references and the prohibition on cooldown timers. This **is not** an APK, engine integration, or a test of gameplay behavior.

The separate browser-only preview `rpg_ui_layout_blueprint.html` was tested locally at 320×640, 360×780, 390×844, 412×915, and 768×1024: navigation, ability/background views, new-game confirmation as demo, grid guides and large text worked without page-level JavaScript errors or horizontal overflow in those checks. The preview is a conversation artifact **not yet committed into this repository**. All demo values are illustrative.

## Asset policy
Keep button hit boxes, IDs, layout and click behavior independent of textures. PNG/vector/nine-slice skins and icons are a subsequent design pass. The eight original user reference images remain **not uploaded** to this repository; their metadata is recorded in `docs/06` for later verified import.

## Prototype v0.2 — responsive usability fixes

- [Open v0.2 HTML blueprint](prototypes/mobile-layout-v0.2.html) (source file; download/open locally to interact).
- [v0.2 Playwright regression test](tests/test_layout_v02.py).
- Decision dock can collapse, leaving more space for reading on short Android screens.
- Switching Skills categories resets the selected skill to a valid item; panel scroll positions survive navigation and visual toggles.
- Enlarged text mode reflows headings, values and navigation instead of forcing a wider viewport.
- **Observed locally on 2026-11-05:** automated browser checks passed at 320×480, 320×640, 360×780, 390×844, 412×915 and 768×1024. Checks covered decision collapse, Skill category coherence, Ability Tree/Background tabs, scroll preservation, enlarged-text page overflow and JavaScript errors. This is NOT a test on a physical Android phone.

To re-run from repository root: `python -m pip install playwright`, `python -m playwright install chromium`, then `python design/ui/tests/test_layout_v02.py`. Do not treat fixture actions as implemented game rules, saves or narrative simulation.
