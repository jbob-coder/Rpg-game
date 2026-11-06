"""Regression checks for the UI layout prototype (not the RPG engine)."""
from pathlib import Path
from playwright.sync_api import sync_playwright

PROTOTYPE = Path(__file__).resolve().parents[1] / "prototypes" / "mobile-layout-v0.2.html"
VIEWPORTS = [(320, 480), (320, 640), (360, 780), (390, 844), (412, 915), (768, 1024)]

def metrics(page):
    return page.evaluate("""() => ({
        pageWidth: document.documentElement.scrollWidth,
        viewportWidth: innerWidth,
        mainHeight: document.querySelector('.body').clientHeight
    })""")

def test():
    assert PROTOTYPE.is_file(), PROTOTYPE
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            for w, h in VIEWPORTS:
                page = browser.new_page(viewport={"width": w, "height": h}, is_mobile=True, has_touch=True)
                errors = []
                page.on("pageerror", lambda e: errors.append(str(e)))
                page.set_content(PROTOTYPE.read_text(encoding="utf-8"), wait_until="load")
                expanded = metrics(page)
                page.get_by_role("button", name="Ocultar opciones").click()
                collapsed = metrics(page)
                assert collapsed["mainHeight"] > expanded["mainHeight"], (w, h)
                page.get_by_role("button", name="Mostrar opciones").click()
                assert page.get_by_role("button", name="Hablar con el herrero").count() == 1
                page.get_by_role("button", name="Character", exact=True).click()
                page.get_by_role("button", name="Skills", exact=True).click()
                page.get_by_role("button", name="Magic", exact=True).click()
                assert "Competencia de ejemplo" in page.get_by_text("Detalle seleccionado").locator("..").inner_text()
                page.get_by_role("button", name="Combat", exact=True).click()
                assert "Sword Mastery" in page.get_by_text("Detalle seleccionado").locator("..").inner_text()
                page.get_by_role("button", name="Abilities", exact=True).click()
                assert page.get_by_role("heading", name="Ability Tree").count() == 1
                page.get_by_role("button", name="Background", exact=True).click()
                assert page.get_by_role("heading", name="Background", exact=True).count() == 1
                page.get_by_role("button", name="Stats", exact=True).click()
                before_el = page.locator(".body")
                before_el.evaluate("(el) => el.scrollTop = 150")
                before = before_el.evaluate("(el) => el.scrollTop")
                page.get_by_role("button", name="Alternar guías de malla").click()
                after = page.locator(".body").evaluate("(el) => el.scrollTop")
                assert before == after, (w, h, before, after)
                page.get_by_role("button", name="Alternar texto grande").click()
                enlarged = metrics(page)
                assert enlarged["pageWidth"] <= enlarged["viewportWidth"] + 1, (w, h, enlarged)
                assert not errors, (w, h, errors)
                print(f"PASS {w}x{h}: story {expanded['mainHeight']} -> {collapsed['mainHeight']} dp; no page JS errors")
                page.close()
        finally:
            browser.close()

if __name__ == "__main__":
    test()
