from playwright import sync_playwright

def run(playwright):
    browser = playwright.webkit.launch(headless=False)
    context = browser.newContext()

    # Open new page
    page = context.newPage()

    # Go to https://www.baidu.com/
    page.goto("https://www.baidu.com/")

    # Click input[name="wd"]
    page.click("input[name=\"wd\"]")

    # Fill input[name="wd"]
    # with page.expect_navigation(url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=test&fenlei=256&rsv_pq=90d2c7a300106485&rsv_t=f7cd53khCaFHt%2BZSJt3rWV2u6D5NVK87%2FVGedj7%2BL93HZPzPMQfsvVMmHQ8&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=5&rsv_sug2=0&rsv_btype=i&inputT=1433&rsv_sug4=2202"):
    with page.expect_navigation():
        page.fill("input[name=\"wd\"]", "test")

    # Press Enter
    # with page.expect_navigation(url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=test&fenlei=256&rsv_pq=90d2c7a300106485&rsv_t=f7cd53khCaFHt%2BZSJt3rWV2u6D5NVK87%2FVGedj7%2BL93HZPzPMQfsvVMmHQ8&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_btype=t&inputT=16&rsv_sug2=0&rsv_sug4=16"):
    with page.expect_navigation():
        page.press("input[name=\"wd\"]", "Enter")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)