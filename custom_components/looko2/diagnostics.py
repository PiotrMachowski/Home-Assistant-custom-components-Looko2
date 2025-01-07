from __future__ import annotations

from dataclasses import asdict
from typing import Any

from homeassistant.core import HomeAssistant

from . import LookO2ConfigEntry


async def async_get_config_entry_diagnostics(
        hass: HomeAssistant, entry: LookO2ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""
    coordinator = entry.runtime_data.coordinator

    return {
        "config_entry_data": entry.as_dict(),
        "device_data": {device_id: asdict(data) for device_id, data in coordinator.data.items()},
    }
