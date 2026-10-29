from __future__ import annotations

import logging
import platform
from typing import TYPE_CHECKING

from pydoll.browser.chromium.base import Browser
from pydoll.browser.managers import ChromiumOptionsManager
from pydoll.exceptions import UnsupportedOS
from pydoll.utils import validate_browser_paths

if TYPE_CHECKING:
    from pydoll.browser.options import ChromiumOptions

logger = logging.getLogger(__name__)


class Chrome(Browser):
    """Chrome browser implementation for CDP automation."""

    def __init__(
        self,
        options: ChromiumOptions | None = None,
        connection_port: int | None = None,
        connection_host: str | None = None,
        use_secure: bool = False,
    ):
        """
        Initialize Chrome browser instance.

        Args:
            options: Chrome configuration options (default if None).
            connection_port: CDP WebSocket port (a free port if None).
            connection_host: Debugger endpoint host (localhost by default).
            use_secure: Resolve over HTTPS and connect over WSS.
        """
        options_manager = ChromiumOptionsManager(options)
        super().__init__(
            options_manager, connection_port, connection_host=connection_host, use_secure=use_secure
        )

    @staticmethod
    def _get_default_binary_location():
        """
        Get default Chrome executable path based on OS.

        Returns:
            Path to Chrome executable.

        Raises:
            UnsupportedOS: If OS is not supported.
            ValueError: If executable not found at default location.
        """
        os_name = platform.system()
        logger.debug(f'Resolving default Chrome binary for OS: {os_name}')

        browser_paths = {
            'Windows': [
                r'C:\Program Files\Google\Chrome\Application\chrome.exe',
                r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
            ],
            'Linux': [
                '/usr/bin/google-chrome',
                '/usr/bin/google-chrome-stable',
            ],
            'Darwin': [
                '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
            ],
        }

        browser_path = browser_paths.get(os_name)

        if not browser_path:
            logger.error(f'Unsupported OS: {os_name}')
            raise UnsupportedOS(f'Unsupported OS: {os_name}')

        path = validate_browser_paths(browser_path)
        logger.debug(f'Using Chrome binary: {path}')
        return path
