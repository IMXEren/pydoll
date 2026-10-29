<p align="center">
    <img src="/docs/resources/images/logo.png" alt="Pydoll Logo" /> <br><br>
</p>

# Pydoll

Pydoll 通过 Chrome DevTools Protocol 自动化 Chromium 浏览器，无需 webdriver，也无需手动等待。用它来抓取数据、测试 Web 应用，以及用 Python 自动化真实的浏览器工作流，同步或异步 API 任你选择。

## 安装

<div class="termy">
```bash
$ pip install pydoll-python

---> 100%
```
</div>

Pydoll 驱动你机器上已安装的 Chrome 或 Edge。你无需下载 webdriver，也无需让 driver 版本与浏览器保持同步。

第一次使用 Pydoll？跟随 [快速开始](getting-started.md) 完成一次完整的上手演练。

## 快速上手

打开一个页面，用你向别人描述元素的方式来查找它们，并以拟人化的节奏进行交互：

=== "Sync"

    ```python
    import time
    from pydoll.sync import Chrome

    def main():
        with Chrome() as browser:
            tab = browser.start()
            tab.go_to('https://github.com/IMXEren/pydoll')

            star_button = tab.find(
                tag_name='button',
                timeout=5,
                raise_exc=False
            )
            if not star_button:
                print('Button not found.')
                return

            star_button.click()
            time.sleep(3)

    main()
    ```

=== "Async"

    ```python
    import asyncio

    from pydoll import Chrome


    async def main():
        async with Chrome() as browser:
            tab = await browser.start()
            await tab.go_to('https://github.com/IMXEren/pydoll')

            star_button = await tab.find(
                tag_name='button',
                timeout=5,
                raise_exc=False
            )
            if not star_button:
                print('Button not found.')
                return

            await star_button.click()
            await asyncio.sleep(3)

    asyncio.run(main())
    ```

当目标是数据而非交互时，定义一个模型，让 Pydoll 提取它，并完成类型标注与校验：

=== "Sync"

    ```python
    from pydoll.sync import Chrome, ExtractionModel, Field

    class Quote(ExtractionModel):
        text: str = Field(selector='.text')
        author: str = Field(selector='.author')
        tags: list[str] = Field(selector='.tag')

    def main():
        with Chrome() as browser:
            tab = browser.start()
            tab.go_to('https://quotes.toscrape.com')

            quotes = tab.extract_all(Quote, scope='.quote', timeout=5)
            for quote in quotes:
                print(f'{quote.author}: {quote.text}')

    main()
    ```

=== "Async"

    ```python
    import asyncio

    from pydoll import Chrome, ExtractionModel, Field


    class Quote(ExtractionModel):
        text: str = Field(selector='.text')
        author: str = Field(selector='.author')
        tags: list[str] = Field(selector='.tag')


    async def main():
        async with Chrome() as browser:
            tab = await browser.start()
            await tab.go_to('https://quotes.toscrape.com')

            quotes = await tab.extract_all(Quote, scope='.quote', timeout=5)
            for quote in quotes:
                print(f'{quote.author}: {quote.text}')

    asyncio.run(main())
    ```

模型支持 CSS 和 XPath 选择器、HTML 属性定位、自定义转换以及嵌套模型。更多内容见 [结构化提取](guides/structured-extraction.md)。

已经有 Playwright 脚本？留着它。改一行导入就能跑在 Pydoll 上：

=== "Sync"

    ```python
    from pydoll.playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://quotes.toscrape.com')
        print(page.locator('.quote .text').first.inner_text())
        browser.close()
    ```

=== "Async"

    ```python
    import asyncio

    from pydoll.playwright.async_api import async_playwright


    async def main():
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto('https://quotes.toscrape.com')
            print(await page.locator('.quote .text').first.inner_text())
            await browser.close()

    asyncio.run(main())
    ```

定位器、`get_by_role`、自动等待、路由、对话框和下载都保留 Playwright 的语义；`expect()` 和测试运行器不在范围内。参见[带上你的 Playwright 脚本](playwright.md)。

## 为什么选择 Pydoll

- **无需 webdriver**：Pydoll 通过 Chrome DevTools Protocol 直接连接浏览器。没有需要下载的东西，也没有版本不匹配需要排查。
- **拟人化交互**：点击沿着弯曲的鼠标轨迹移动，打字带有可变的节奏并偶尔出现随即被修正的拼写错误，因此你的自动化表现得像一个真人在键盘前操作。
- **同步或异步**：同一套 API 既可以从 `pydoll.sync` 逐个调用阻塞执行，也可以运行在 `asyncio` 上，让一个进程并发驱动多个标签页和浏览器。
- **兼容 Playwright**：保留已有的 Playwright 脚本，改一行导入；它通过 Pydoll 的 CDP 连接运行，没有驱动进程。
- **Cloudflare Turnstile 处理**：Pydoll 检测 Turnstile 组件并原生点击它。无需付费或集成外部 captcha 服务。
- **网络控制**：在页面发起请求时监控、拦截并修改它们。
- **类型化提取**：声明一个 Pydantic 模型，得到经过校验、对 IDE 友好的对象，而不是原始元素。

## 下一步

- [快速开始](getting-started.md)：安装 Pydoll 并运行你的第一个脚本。
- [你的第一个自动化](first-automation.md)：登录站点并提取类型化数据。
- [带上你的 Playwright 脚本](playwright.md)：改一行导入，你的 Playwright 代码就跑在 Pydoll 上。
- [从 Selenium 和 Playwright 迁移](migrating.md)：把你已经掌握的操作对应到 Pydoll。
- [保持不被检测](stealth/index.md)：避开明显机器人信号的最小配置。
- [指南](guides/index.md)：每种能力一篇指南，从元素查找到请求拦截。
- [API 参考](api/index.md)：每一个公开类和方法。

## 许可证

Pydoll 以 [MIT License](https://github.com/IMXEren/pydoll/blob/main/LICENSE) 发布，因此你可以在个人和商业项目中自由使用它。
