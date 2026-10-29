from __future__ import annotations

from typing import TypedDict

from typing_extensions import Required


class WSAddressResolverParams(TypedDict, total=False):
    """Parameters passed to a WebSocket address resolver callback.

    All three fields are supplied when resolving a browser endpoint.

    Attributes:
        host: The hostname of the browser's debugging server.
        port: The port of the browser's debugging server.
        use_secure: Whether to use HTTPS/WSS (``True``) or HTTP/WS (``False``)
            when resolving the WebSocket address.
    """

    host: Required[str]
    port: Required[int]
    use_secure: Required[bool]
