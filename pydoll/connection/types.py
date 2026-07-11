from __future__ import annotations

from typing import Optional, TypedDict

from typing_extensions import Required


class WSAddressResolverParams(TypedDict, total=False):
    """Parameters passed to a WebSocket address resolver callback.

    Resolver callbacks receive these as keyword arguments and only need to
    consume the ones they care about. New parameters may be added without
    breaking existing resolvers.
    """

    host: Required[Optional[str]]
    port: Required[Optional[int]]
    use_secure: Required[bool]
