from datetime import timedelta
from typing import Final

from homeassistant.const import Platform

NAME: Final = "LookO2"

DOMAIN: Final = "looko2"

ATTRIBUTION: Final = "Data provided by LookO2"

CONF_DEVICE_IDS: Final = "device_ids"

UPDATE_INTERVAL: Final = timedelta(minutes=30)

PLATFORMS: list[Platform] = [Platform.SENSOR]
