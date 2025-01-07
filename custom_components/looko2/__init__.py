from __future__ import annotations

import logging

from aiohttp import ClientError
from homeassistant.const import CONF_API_TOKEN
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.device_registry import DeviceRegistry

from .config_flow import LookO2ConfigEntry, LookO2RuntimeData
from .connector import LookO2Connector
from .connector.exceptions import LookO2Exception
from .const import CONF_DEVICE_IDS, PLATFORMS, DOMAIN
from .coordinator import LookO2DataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: LookO2ConfigEntry) -> bool:
    device_ids: list[str] = entry.options[CONF_DEVICE_IDS]
    token: str = entry.data[CONF_API_TOKEN]

    client_session = async_get_clientsession(hass)
    look_o2_connector = LookO2Connector(client_session, token, device_ids)

    try:
        device_data = await look_o2_connector.get_all_device_data()
    except (ClientError, TimeoutError, LookO2Exception) as err:
        raise ConfigEntryNotReady from err

    look_o2_update_coordinator = LookO2DataUpdateCoordinator(hass, look_o2_connector, device_data)
    await look_o2_update_coordinator.async_config_entry_first_refresh()
    entry.runtime_data = LookO2RuntimeData(look_o2_update_coordinator)
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    entry.async_on_unload(entry.add_update_listener(async_reload_entry))
    return True


async def async_unload_entry(hass: HomeAssistant, entry: LookO2ConfigEntry) -> bool:
    _remove_old_devices(hass, entry)
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)


async def async_reload_entry(hass: HomeAssistant, entry: LookO2ConfigEntry) -> None:
    await hass.config_entries.async_reload(entry.entry_id)


def _remove_old_devices(hass: HomeAssistant, entry: LookO2ConfigEntry) -> None:
    device_registry = dr.async_get(hass)
    existing_entries = dr.async_entries_for_config_entry(
        device_registry, entry.entry_id
    )
    existing_ids = set(map(lambda ee: list(ee.identifiers)[0][1], existing_entries))
    new_ids = set(entry.options[CONF_DEVICE_IDS])
    _remove_devices(device_registry, set(existing_ids) - set(new_ids))


def _remove_devices(device_registry: DeviceRegistry, device_ids_to_remove: set[str]) -> None:
    for device_id in device_ids_to_remove:
        device = device_registry.async_get_device(identifiers={(DOMAIN, device_id)})
        if device is not None:
            device_registry.async_remove_device(device.id)
