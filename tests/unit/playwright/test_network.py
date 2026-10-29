"""Request headers must include Chrome's extra-info event regardless of event timing."""

from __future__ import annotations

import asyncio
from types import SimpleNamespace
from typing import TYPE_CHECKING, cast

import pytest

from pydoll.playwright._network import NetworkManager  # noqa: PLC2701

if TYPE_CHECKING:
    from pydoll.playwright.async_api import Page


def _manager() -> NetworkManager:
    page = SimpleNamespace(
        _loop=asyncio.get_running_loop(),
        _navigation=SimpleNamespace(_notify=lambda: None),
        emit=lambda *_: None,
    )
    return NetworkManager(cast('Page', page))


def _request(manager: NetworkManager):
    manager.on_request_will_be_sent({
        'requestId': '1',
        'request': {'url': 'http://localhost/', 'headers': {'Accept': '*/*'}},
    })
    request = manager.request_for('1')
    assert request is not None
    return request


@pytest.mark.asyncio
async def test_request_extra_info_before_request_is_preserved():
    manager = _manager()
    manager.on_request_will_be_sent_extra_info({
        'requestId': '1', 'headers': {'Cookie': 'session=abc'}
    })
    request = _request(manager)

    assert (await request.all_headers())['cookie'] == 'session=abc'
    assert await request.header_value('Cookie') == 'session=abc'
    assert {'name': 'cookie', 'value': 'session=abc'} in await request.headers_array()


@pytest.mark.asyncio
async def test_request_all_headers_waits_for_extra_info():
    manager = _manager()
    request = _request(manager)
    headers = asyncio.create_task(request.all_headers())
    await asyncio.sleep(0)
    assert not headers.done()

    manager.on_request_will_be_sent_extra_info({
        'requestId': '1', 'headers': {'Cookie': 'session=abc'}
    })
    assert (await headers)['cookie'] == 'session=abc'


@pytest.mark.asyncio
async def test_request_all_headers_returns_when_no_extra_info_arrives():
    manager = _manager()
    request = _request(manager)
    headers = asyncio.create_task(request.all_headers())
    await asyncio.sleep(0)
    manager.on_loading_finished({'requestId': '1'})

    assert await headers == {'accept': '*/*'}
