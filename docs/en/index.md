<p align="center">
    <img src="/docs/resources/images/logo.png" alt="Pydoll Logo" /> <br><br>
</p>

# Pydoll

Pydoll automates Chromium browsers over the Chrome DevTools Protocol, with no webdriver and no manual waits. Use it to scrape data, test web applications, and automate real browser workflows in Python, with a synchronous or an asynchronous API.

## Installation

<div class="termy">
```bash
$ pip install pydoll-python

---> 100%
```
</div>

Pydoll drives the Chrome or Edge already installed on your machine. You don't need to download a webdriver or keep driver versions in sync with your browser.

New to Pydoll? Follow [Getting started](getting-started.md) for a complete walkthrough.

## Quick start

Open a page, find elements by how you'd describe them to a person, and interact with humanized timing:

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

When the goal is data rather than interaction, define a model and let Pydoll extract it, typed and validated:

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

Models support CSS and XPath selectors, HTML attribute targeting, custom transforms, and nested models. Learn more in [Structured extraction](guides/structured-extraction.md).

Already have a Playwright script? Keep it. One import moves it onto Pydoll:

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

Locators, `get_by_role`, auto-waiting, routes, dialogs and downloads keep their Playwright semantics; `expect()` and the test runner are out of scope. See [Bring your Playwright script](playwright.md).

## Why Pydoll

- **No webdriver**: Pydoll connects straight to the browser over the Chrome DevTools Protocol. Nothing to download, no version mismatches to debug.
- **Humanized interactions**: clicks follow curved mouse paths and typing has variable rhythm with occasional corrected typos, so your automation behaves like a person at the keyboard.
- **Sync or async**: the same API blocks call by call from `pydoll.sync`, or runs on `asyncio` so one process can drive many tabs and browsers concurrently.
- **Playwright-compatible**: keep an existing Playwright script and change one import; it runs over Pydoll's CDP connection with no driver process.
- **Cloudflare Turnstile handling**: Pydoll detects the Turnstile widget and clicks it natively. No external captcha service to pay for or integrate.
- **Network control**: monitor, intercept, and modify requests as the page makes them.
- **Typed extraction**: declare a Pydantic model and get validated, IDE-friendly objects instead of raw elements.

## What's next

- [Getting started](getting-started.md): install Pydoll and run your first script.
- [Your first automation](first-automation.md): log in to a site and extract typed data.
- [Bring your Playwright script](playwright.md): one import, and your Playwright code runs on Pydoll.
- [Migrating from Selenium and Playwright](migrating.md): map the moves you know to Pydoll.
- [Staying undetected](stealth/index.md): the minimum setup to avoid the obvious bot signals.
- [Guides](guides/index.md): one guide per capability, from element finding to request interception.
- [API Reference](api/index.md): every public class and method.

## License

Pydoll is released under the [MIT License](https://github.com/IMXEren/pydoll/blob/main/LICENSE), so you can use it freely in personal and commercial projects.
