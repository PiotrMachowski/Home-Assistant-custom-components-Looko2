import logging
from typing import Self

from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .connector import LookO2Connector, LookO2DevicesDataMap
from .connector.exceptions import LookO2Exception
from .const import DOMAIN, UPDATE_INTERVAL

_LOGGER = logging.getLogger(__name__)


class LookO2DataUpdateCoordinator(DataUpdateCoordinator[LookO2DevicesDataMap]):

    def __init__(
            self: Self,
            hass: HomeAssistant,
            look_o2_connector: LookO2Connector,
            devices: LookO2DevicesDataMap,
    ) -> None:
        self.look_o2_connector = look_o2_connector
        self.device_infos = {
            device.device_id: DeviceInfo(
                entry_type=DeviceEntryType.SERVICE,
                identifiers={(DOMAIN, device.device_id)},
                manufacturer="LookO2",
                name=f"{device.name}",
                configuration_url=f"https://looko2.com/tracker.php?lan=&search={device.device_id}",
                serial_number=device.device_id
            ) for device in devices.values()
        }
        super().__init__(hass, _LOGGER, name=DOMAIN, update_interval=UPDATE_INTERVAL, update_method=self.update_data)

    async def update_data(self: Self) -> LookO2DevicesDataMap:
        try:
            return await self.look_o2_connector.get_all_device_data()
        except LookO2Exception as err:
            raise UpdateFailed(err) from err
