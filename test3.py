from time import sleep
 
from playwright import sync_playwright
 
# 注意：默认是无头模式
 
with sync_playwright() as p:
    # 分别对应三个浏览器驱动
    for browser_type in [p.chromium, p.firefox, p.webkit]:
 
        # 指定为有头模式，方便查看
        browser = browser_type.launch(headless=False)
        page = browser.newPage()
        page.goto('http://baidu.com')
 
        # 执行一次搜索操作
        page.fill("input[name=\"wd\"]", "AirPython")
        with page.expect_navigation():
            page.press("input[name=\"wd\"]", "Enter")
 
        # 等待页面加载完全
        page.waitForSelector("text=百度热榜")
 
        # 截图
        page.screenshot(path=f'example-{browser_type.name}.png')
 
        # 休眠5s
        sleep(5)
 
        # 关闭浏览器
        browser.close()