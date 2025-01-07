from typing import Final

from aiohttp import ClientTimeout

API_URL_BASE: Final = "https://api.looko2.com/?token={token}"
API_URL_ALL_DEVICES: Final = f"{API_URL_BASE}&method=GetAll"
API_URL_DEVICE_DATA: Final = f"{API_URL_BASE}&method=GetLOOKO&id={{device_id}}"

TIMEOUT = ClientTimeout(total=10)
