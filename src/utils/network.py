"""
Network utilities for OneShot-Extended
"""

class NetworkAddress:
    """Network address handling class."""

    def __init__(self, mac_str: str):
        """Initialize NetworkAddress with MAC string."""
        self._STR_REPR = mac_str.replace(':', '').replace('-', '').upper()
        if len(self._STR_REPR) != 12:
            raise ValueError('Invalid MAC address format')
        self._INT_REPR = self._mac2int(self._STR_REPR)

    @property
    def string(self) -> str:
        """Get MAC address as string."""
        return self._STR_REPR

    @property
    def hex(self) -> str:
        """Get MAC address as hex string."""
        return self._STR_REPR

    @property
    def integer(self) -> int:
        """Get MAC address as integer."""
        return self._INT_REPR

    def _mac2int(self, mac: str) -> int:
        """Convert MAC address to integer."""
        return int(mac, 16)

    def __str__(self):
        return self._STR_REPR

    def __repr__(self):
        return f'NetworkAddress(string={self._STR_REPR}, integer={self._INT_REPR})'
