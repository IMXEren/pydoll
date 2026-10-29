<p align="center">
    <img src="/docs/resources/images/logo.png" alt="Pydoll Logo" /> <br><br>
</p>

# Pydoll

O Pydoll automatiza navegadores Chromium pelo Chrome DevTools Protocol, sem webdriver e sem esperas manuais. Use para extrair dados, testar aplicações web e automatizar fluxos reais de navegador em Python, com uma API síncrona ou assíncrona.

## Instalação

<div class="termy">
```bash
$ pip install pydoll-python

---> 100%
```
</div>

O Pydoll controla o Chrome ou o Edge que já estão instalados na sua máquina. Você não precisa baixar um webdriver nem manter as versões do driver em sincronia com o navegador.

Novo no Pydoll? Siga o [Primeiros passos](getting-started.md) para um passo a passo completo.

## Início rápido

Abra uma página, encontre elementos pela forma como você os descreveria para uma pessoa e interaja com timing humanizado:

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

Quando o objetivo é dado, e não interação, defina um modelo e deixe o Pydoll extraí-lo, tipado e validado:

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

Os modelos suportam seletores CSS e XPath, mira em atributos HTML, transformações personalizadas e modelos aninhados. Saiba mais em [Extração estruturada](guides/structured-extraction.md).

Já tem um script Playwright? Mantenha ele. Um import o coloca no Pydoll:

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

Locators, `get_by_role`, espera automática, rotas, diálogos e downloads mantêm a semântica do Playwright; `expect()` e o test runner ficam fora do escopo. Veja [Traga seu script Playwright](playwright.md).

## Por que Pydoll

- **Sem webdriver**: o Pydoll se conecta direto ao navegador pelo Chrome DevTools Protocol. Nada para baixar, nenhuma incompatibilidade de versão para depurar.
- **Interações humanizadas**: os cliques seguem trajetórias curvas do mouse e a digitação tem ritmo variável, com erros de digitação corrigidos de vez em quando, então sua automação se comporta como uma pessoa no teclado.
- **Síncrono ou assíncrono**: a mesma API bloqueia chamada a chamada a partir de `pydoll.sync`, ou roda sobre `asyncio` para que um único processo controle muitas abas e navegadores ao mesmo tempo.
- **Compatível com o Playwright**: mantenha um script Playwright existente e troque um import; ele roda pela conexão CDP do Pydoll, sem processo driver.
- **Tratamento do Cloudflare Turnstile**: o Pydoll detecta o widget Turnstile e clica nele nativamente. Nenhum serviço externo de captcha para pagar ou integrar.
- **Controle de rede**: monitore, intercepte e modifique requisições conforme a página as faz.
- **Extração tipada**: declare um modelo Pydantic e receba objetos validados e amigáveis à IDE, em vez de elementos crus.

## Próximos passos

- [Primeiros passos](getting-started.md): instale o Pydoll e rode seu primeiro script.
- [Sua primeira automação](first-automation.md): faça login em um site e extraia dados tipados.
- [Traga seu script Playwright](playwright.md): um import, e seu código Playwright roda no Pydoll.
- [Migrando do Selenium e do Playwright](migrating.md): mapeie os comandos que você conhece para o Pydoll.
- [Passando despercebido](stealth/index.md): a configuração mínima para evitar os sinais óbvios de bot.
- [Guias](guides/index.md): um guia por funcionalidade, do encontro de elementos à interceptação de requisições.
- [Referência da API](api/index.md): cada classe e método público.

## Licença

O Pydoll é distribuído sob a [Licença MIT](https://github.com/IMXEren/pydoll/blob/main/LICENSE), então você pode usá-lo livremente em projetos pessoais e comerciais.
