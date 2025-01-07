import json
import logging
from typing import Any, Self

from aiohttp import ClientSession

from .const import API_URL_ALL_DEVICES, API_URL_DEVICE_DATA, TIMEOUT
from .exceptions import (
    LookO2UnauthorizedException,
    LookO2ApiException,
    LookO2MissingDataException,
    LookO2InvalidDeviceIdException
)
from .model import LookO2DeviceData, LookO2DevicesDataMap

_LOGGER = logging.getLogger(__name__)


class LookO2Connector:
    def __init__(self: Self, session: ClientSession, token: str, device_ids: list[str] | None = None) -> None:
        self._session = session
        self._token = token
        self._device_ids = device_ids

    async def _get_data(self: Self, url: str) -> Any:
        response = await self._session.get(url, timeout=TIMEOUT)

        response_text = await response.text()

        if response.status in [401, 403]:
            raise LookO2UnauthorizedException(response.status, response_text)

        if response.status != 200:
            raise LookO2ApiException(response.status, response_text)

        return json.loads(response_text)

    async def get_all_devices(self: Self) -> list[LookO2DeviceData]:
        url = API_URL_ALL_DEVICES.format(token=self._token)
        data = await self._get_data(url)
        devices = [LookO2DeviceData.from_dict(device_data) for device_data in data]
        return devices

    async def get_all_device_data(self: Self) -> LookO2DevicesDataMap:
        if self._device_ids is None:
            raise LookO2MissingDataException("device_ids")

        all_device_data = {device_id: await self.get_device_data(device_id) for device_id in self._device_ids}
        return all_device_data

    async def get_device_data(self: Self, device_id: str) -> LookO2DeviceData:
        url = API_URL_DEVICE_DATA.format(token=self._token, device_id=device_id)
        data = await self._get_data(url)

        if len(data) != 25:
            raise LookO2InvalidDeviceIdException(device_id)

        device_data = LookO2DeviceData.from_dict(data)
        return device_data
