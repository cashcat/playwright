import asyncio
 
from playwright import async_playwright
 
# 异步执行
async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            # 指定为有头模式，方便查看
            browser = await browser_type.launch(headless=False)
            page = await browser.newPage()
 
            await page.goto('http://baidu.com')
 
            # 执行一次搜索操作
            await page.fill("input[name=\"wd\"]", "AirPython")
            await page.press("input[name=\"wd\"]", "Enter")
 
            # 等待页面加载完全
            await page.waitForSelector("text=百度热榜")
 
            # 截图
            await page.screenshot(path=f'example-{browser_type.name}.png')
 
            await browser.close()
 
 
asyncio.get_event_loop().run_until_complete(main())