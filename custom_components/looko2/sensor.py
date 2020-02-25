from datetime import timedelta
import logging
import requests

import voluptuous as vol

from homeassistant.util import Throttle
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (CONF_MONITORED_CONDITIONS, CONF_NAME, TEMP_CELSIUS, CONF_API_KEY, CONF_SCAN_INTERVAL)
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

CONF_STATION_ID = 'station_id'

DEFAULT_NAME = 'LookO2'
DEFAULT_SCAN_INTERVAL = timedelta(minutes=20)

SENSOR_TYPES = {
    'AverageHCHO': ['Średni formaldehyd', 'µg/m³'],
    'AveragePM1': ['Średnie PM1', 'µg/m³'],
    'AveragePM10': ['Średnie PM10', 'µg/m³'],
    'AveragePM25': ['Średnie PM2.5', 'µg/m³'],
    'Color': ['Kolor', None],
    'HCHO': ['Formaldehyd', 'µg/m³'],
    'Humidity': ['Wilgotność', '%'],
    'IJP': ['IJP', ' '],
    'IJPDescription': ['IJP Opis', None],
    'IJPDescriptionEN': ['IJP Opis EN', None],
    'IJPString': ['IJP Nazwa', None],
    'IJPStringEN': ['IJP Nazwa EN', None],
    'Indoor': ['Wewnętrzny', None],
    'PM1': ['PM1', 'µg/m³'],
    'PM10': ['PM10', 'µg/m³'],
    'PM25': ['PM2.5', 'µg/m³'],
    'PreviousIJP': ['Poprzednie IJP', ' '],
    'Temperature': ['Temperatura', TEMP_CELSIUS]
}

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_STATION_ID): cv.string,
    vol.Required(CONF_API_KEY): cv.string,
    vol.Optional(CONF_MONITORED_CONDITIONS, default=[]):
        vol.All(cv.ensure_list, [vol.In(SENSOR_TYPES)]),
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    vol.Optional(CONF_SCAN_INTERVAL, default=DEFAULT_SCAN_INTERVAL): cv.time_period
})


def setup_platform(hass, config, add_entities, discovery_info=None):
    name = config.get(CONF_NAME)
    token = config.get(CONF_API_KEY)
    station_id = config.get(CONF_STATION_ID)
    scan_interval = config.get(CONF_SCAN_INTERVAL)
    updater = LookO2Updater(station_id, token, scan_interval)
    updater.update()
    if updater.data is None:
        raise Exception('Invalid configuration for LookO2 platform')
    dev = []
    for variable in config[CONF_MONITORED_CONDITIONS]:
        dev.append(LookO2Sensor(name, variable, updater))
    add_entities(dev, True)


class LookO2Sensor(Entity):
    def __init__(self, name, sensor_type, updater):
        self._client_name = name
        self._type = sensor_type
        self._updater = updater
        self._data = None
        self._state = None
        self._unit_of_measurement = SENSOR_TYPES[sensor_type][1]

    @property
    def name(self):
        return '{} {}'.format(self._client_name, self._type)

    @property
    def state(self):
        if self._updater.data is not None:
            self._state = self._updater.data[self._type]
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit_of_measurement

    def update(self):
        self._updater.update()


class LookO2Updater:
    def __init__(self, station_id, token, scan_interval):
        self._station_id = station_id
        self._token = token
        self.update = Throttle(scan_interval)(self._update)
        self.data = None

    def _update(self):
        address = 'http://api.looko2.com/?method=GetLOOKO&id={}&token={}'.format(self._station_id, self._token)
        request = requests.get(address)
        if request.status_code == 200 and request.content.__len__() > 0:
            self.data = request.json()
