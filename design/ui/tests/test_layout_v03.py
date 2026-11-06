"""Regression test: proportions, 48px CSS touch targets and panel layout.

Only tests a browser UI fixture, not gameplay or a physical Android device.
Requirements: pip install playwright; python -m playwright install chromium.
"""
import os
import shutil
from pathlib import Path
from playwright.sync_api import sync_playwright

HTML = Path(__file__).resolve().parents[1] / "prototypes" / "mobile-layout-v0.3.html"
SIZES = [(320,480),(320,640),(360,780),(390,844),(412,915),(768,1024)]
TABS = ["Overview","Stats","Skills","Abilities","Class","Background"]
SCREENS = ["Story",*TABS,"Inventory","More","Journal","New Game"]

def audit(page):
    return page.evaluate("""() => {
      const rect = e => e.getBoundingClientRect();
      const visible = b => {const r=rect(b),s=getComputedStyle(b);return r.width>0&&r.height>0&&s.visibility!=='hidden'&&s.display!=='none'};
      const tooSmall=[...document.querySelectorAll('button')].filter(visible).filter(b=>rect(b).width<47.9||rect(b).height<47.9).map(b=>[b.innerText,rect(b).width,rect(b).height]);
      const body=document.querySelector('.body'),header=document.querySelector('.header .app-symbol'),tab=document.querySelector('.subtabs button'),content=document.querySelector('.body > .stack');
      return {width:innerWidth,scrollWidth:document.documentElement.scrollWidth,small:tooSmall,
       main:body.clientHeight,contentLeft:content?rect(content).left:null,
       headerLeft:rect(header).left,tabLeft:tab?rect(tab).left:null};
    }""")

def navigate(page,screen):
    if screen in TABS:
        page.get_by_role("button",name="Character",exact=True).click()
        page.get_by_role("button",name=screen,exact=True).click()
    elif screen in ("Story","Inventory","More"):
        page.get_by_role("button",name=screen,exact=True).click()
    else:
        page.get_by_role("button",name="More",exact=True).click()
        page.get_by_role("button",name="Journal · blueprint" if screen=="Journal" else "Nueva partida · blueprint").click()

def test_all():
    html=HTML.read_text(encoding="utf-8")
    assert "v0.3" in html
    with sync_playwright() as p:
        binary=os.environ.get("CHROME_PATH") or shutil.which("chromium") or shutil.which("google-chrome")
        args=dict(headless=True)
        if binary: args.update(executable_path=binary,args=["--no-sandbox"])
        browser=p.chromium.launch(**args)
        try:
            for width,height in SIZES:
                page=browser.new_page(viewport={"width":width,"height":height},is_mobile=True,has_touch=True)
                errors=[]
                page.on("pageerror",lambda e: errors.append(str(e)))
                page.set_content(html,wait_until="load")
                expanded=audit(page)
                page.get_by_role("button",name="Ocultar opciones").click()
                collapsed=audit(page)
                assert collapsed["main"]>expanded["main"]+30,(width,height,expanded,collapsed)
                page.get_by_role("button",name="Mostrar opciones").click()
                for zoom in (False,True):
                    for screen in SCREENS:
                        navigate(page,screen)
                        if zoom and screen=="Story":
                            page.get_by_role("button",name="Alternar texto grande").click()
                        a=audit(page)
                        assert a["scrollWidth"]<=a["width"]+1,(width,height,zoom,screen,"overflow",a)
                        assert not a["small"],(width,height,zoom,screen,"small touch targets",a["small"])
                        assert abs(a["headerLeft"]-a["contentLeft"])<1.5,(width,height,zoom,screen,"header margin",a)
                        if a["tabLeft"] is not None:
                            assert abs(a["tabLeft"]-a["contentLeft"])<1.5,(width,height,zoom,screen,"tabs margin",a)
                        assert a["main"]>0,(width,height,zoom,screen,"reading area")
                navigate(page,"Skills")
                page.get_by_role("button",name="Magic",exact=True).click()
                assert "Competencia de ejemplo" in page.get_by_text("Detalle seleccionado").locator("..").inner_text()
                page.get_by_role("button",name="Combat",exact=True).click()
                assert "Sword Mastery" in page.get_by_text("Detalle seleccionado").locator("..").inner_text()
                assert not errors,(width,height,errors)
                print(f"PASS {width}x{height}: 22 layout states, >=48px controls, aligned margins, reading +{collapsed['main']-expanded['main']}px")
                page.close()
        finally:
            browser.close()

if __name__=="__main__":
    test_all()
