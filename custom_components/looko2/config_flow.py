from __future__ import annotations

import logging
import math
from dataclasses import dataclass
from typing import Any, Self

import voluptuous as vol
from aiohttp import ClientError
from homeassistant.config_entries import ConfigFlow, ConfigFlowResult, ConfigEntry, OptionsFlow
from homeassistant.const import CONF_API_TOKEN
from homeassistant.core import callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.selector import (
    SelectOptionDict,
    SelectSelector,
    SelectSelectorConfig,
    SelectSelectorMode,
)

from .connector import LookO2Connector
from .connector.exceptions import LookO2Exception
from .connector.model import LookO2DeviceData
from .const import CONF_DEVICE_IDS, DOMAIN, NAME
from .coordinator import LookO2DataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)


@dataclass
class LookO2RuntimeData:
    coordinator: LookO2DataUpdateCoordinator


type LookO2ConfigEntry = ConfigEntry[LookO2RuntimeData]


class LookO2FlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION = 1

    def __init__(self: Self) -> None:
        self._token = None
        self._all_devices = []

    async def async_step_user(self: Self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult:

        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        errors = {}

        if user_input is not None:
            client_session = async_get_clientsession(self.hass)
            self._token = user_input[CONF_API_TOKEN]
            look_o2_connector = LookO2Connector(client_session, self._token)

            try:
                self._all_devices = await look_o2_connector.get_all_devices()
            except (ClientError, TimeoutError, LookO2Exception) as e:
                errors["base"] = "cannot_connect"
            except Exception:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"

            is_valid = len(self._all_devices) > 0
            if is_valid:
                self._token = self._token
                return await self.async_step_device_ids()
            else:
                errors[CONF_API_TOKEN] = "invalid_token"

        schema: vol.Schema = vol.Schema({
            vol.Required(CONF_API_TOKEN): str
        })
        return self.async_show_form(step_id="user", data_schema=schema, errors=errors)

    async def async_step_device_ids(
            self: Self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}

        client_session = async_get_clientsession(self.hass)

        if user_input is not None:
            device_ids = user_input[CONF_DEVICE_IDS]

            look_o2_connector = LookO2Connector(client_session, self._token, device_ids=device_ids)

            try:
                await look_o2_connector.get_all_device_data()
            except (ClientError, TimeoutError, LookO2Exception):
                errors["base"] = "cannot_connect"
            except Exception:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
            else:
                return self.async_create_entry(title=NAME,
                                               data={CONF_API_TOKEN: self._token},
                                               options={CONF_DEVICE_IDS: device_ids},
                                               )

        def device_distance_comparator(d: LookO2DeviceData) -> float:
            return math.sqrt(
                (self.hass.config.latitude - d.latitude) ** 2
                +
                (self.hass.config.longitude - d.longitude) ** 2
            )

        sorted_devices = sorted(self._all_devices, key=device_distance_comparator)

        options: list[SelectOptionDict] = [
            SelectOptionDict(value=device_data.device_id, label=f"{device_data.name} ({device_data.device_id})")
            for device_data in sorted_devices
        ]

        schema: vol.Schema = vol.Schema(
            {
                vol.Required(CONF_DEVICE_IDS, default=[]): SelectSelector(
                    SelectSelectorConfig(
                        options=options,
                        multiple=True,
                        custom_value=False,
                        sort=False,
                        mode=SelectSelectorMode.DROPDOWN,
                    ),
                )
            }
        )

        return self.async_show_form(step_id="device_ids", data_schema=schema, errors=errors)

    @staticmethod
    @callback
    def async_get_options_flow(config_entry: LookO2ConfigEntry) -> LookO2OptionsFlowHandler:
        return LookO2OptionsFlowHandler(config_entry)


# noinspection PyTypeChecker
class LookO2OptionsFlowHandler(OptionsFlow):

    def __init__(self: Self, config_entry: LookO2ConfigEntry) -> None:
        self._config_entry = config_entry
        self.look_o2_connector = config_entry.runtime_data.coordinator.look_o2_connector
        self._all_devices = []
        self._options = dict(config_entry.options)

    async def async_step_init(
            self: Self,
            _: dict[str, Any] | None = None) -> ConfigFlowResult:  # pylint: disable=unused-argument
        """Manage the options."""
        return await self.async_step_device_ids()

    async def async_step_device_ids(
            self: Self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}

        self._all_devices = await self.look_o2_connector.get_all_devices()

        if user_input is not None:
            device_ids = user_input[CONF_DEVICE_IDS]

            client_session = async_get_clientsession(self.hass)
            look_o2_connector = LookO2Connector(client_session, self._options.get(CONF_API_TOKEN),
                                                device_ids=device_ids)

            try:
                await look_o2_connector.get_all_device_data()
            except (ClientError, TimeoutError, LookO2Exception):
                errors["base"] = "cannot_connect"
            except Exception:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
            else:
                output = await self._update_entry(device_ids)
                await self.hass.config_entries.async_reload(self.config_entry.entry_id)
                return output

        def device_distance_comparator(d: LookO2DeviceData) -> float:
            return math.sqrt(
                (self.hass.config.latitude - d.latitude) ** 2
                +
                (self.hass.config.longitude - d.longitude) ** 2
            )

        sorted_devices = sorted(self._all_devices, key=device_distance_comparator)

        options: list[SelectOptionDict] = [
            SelectOptionDict(value=device_data.device_id, label=f"{device_data.name} ({device_data.device_id})")
            for device_data in sorted_devices
        ]

        schema: vol.Schema = vol.Schema(
            {
                vol.Required(CONF_DEVICE_IDS, default=self._options[CONF_DEVICE_IDS]): SelectSelector(
                    SelectSelectorConfig(
                        options=options,
                        multiple=True,
                        custom_value=False,
                        sort=False,
                        mode=SelectSelectorMode.DROPDOWN,
                    ),
                )
            }
        )

        return self.async_show_form(step_id="device_ids", data_schema=schema, errors=errors)

    async def _update_entry(self: Self, device_ids: list[str]) -> ConfigFlowResult:
        self._options[CONF_DEVICE_IDS] = device_ids
        return self.async_create_entry(title=NAME, data=self._options)
