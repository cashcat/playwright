
from playwright import sync_playwright
 
def run(playwright):
    browser = playwright.webkit.launch(headless=False)
    context = browser.newContext()
 
    # Open new page
    page = context.newPage()
 
    # Go to https://www.baidu.com/
    page.goto("https://www.baidu.com/")
 
    # Fill input[name="wd"]
    page.fill("input[name=\"wd\"]", "AirPython")
 
    # Press Enter
    # with page.expect_navigation(url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=AirPython&fenlei=256&rsv_pq=a1739d870005eec3&rsv_t=e640wwS33ra1Koivxvy1WyTxyknRwnllWiw4JBqIYd/KUN/WKpWLtL2b2+0&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=21&rsv_sug1=18&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&inputT=6199&rsv_sug4=6199"):
    with page.expect_navigation():
        page.press("input[name=\"wd\"]", "Enter")
 
    # Close page
    page.close()
 
    # ---------------------
    context.close()
    browser.close()
 
with sync_playwright() as playwright:
    run(playwright)