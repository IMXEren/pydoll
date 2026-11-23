"""Authentication headers reach both browser and page CDP sockets."""

import json

import pytest
from websockets.asyncio.server import serve

from pydoll.browser.chromium import Chrome
from pydoll.commands.runtime_commands import RuntimeCommands


@pytest.mark.asyncio
async def test_authenticated_connection_opens_normal_page_socket():
    paths = []
    headers_seen = []

    async def handle(socket):
        paths.append(socket.request.path)
        headers_seen.append(socket.request.headers.get('Authorization'))
        async for raw in socket:
            command = json.loads(raw)
            if command['method'] == 'Target.getTargets':
                result = {
                    'targetInfos': [{'targetId': 'tab-a', 'type': 'page', 'url': 'about:blank'}]
                }
            else:
                result = {'result': {'type': 'string', 'value': 'page-socket'}}
            await socket.send(json.dumps({'id': command['id'], 'result': result}))

    async with serve(handle, '127.0.0.1', 0) as server:
        port = server.sockets[0].getsockname()[1]
        browser = Chrome()
        headers = {'Authorization': 'Bearer synthetic'}
        try:
            tab = await browser.connect(
                f'ws://127.0.0.1:{port}/devtools/browser/test?reservation=tab-1',
                headers=headers,
            )
            response = await tab._connection_handler.execute_command(RuntimeCommands.evaluate('1'))
            assert response['result']['result']['value'] == 'page-socket'
            assert paths == [
                '/devtools/browser/test?reservation=tab-1',
                '/devtools/page/tab-a?reservation=tab-1',
            ]
            assert headers_seen == ['Bearer synthetic'] * len(paths)
            headers['Authorization'] = 'Bearer changed'
            later = browser._get_tab_kwargs('tab-later')['connection_handler']
            assert later._headers == {'Authorization': 'Bearer synthetic'}
        finally:
            await browser.close()
