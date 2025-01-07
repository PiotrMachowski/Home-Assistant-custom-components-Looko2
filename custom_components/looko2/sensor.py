from __future__ import annotations

import logging
from collections.abc import Callable
from dataclasses import dataclass

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import (
    UnitOfTemperature,
    CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    PERCENTAGE,
    CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER,
    EntityCategory
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType

from . import LookO2ConfigEntry
from .connector.model import LookO2DeviceData
from .const import CONF_DEVICE_IDS
from .coordinator import LookO2DataUpdateCoordinator
from .entity import LookO2Entity

_LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True, kw_only=True)
class LookO2SensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[LookO2DeviceData], StateType]


SENSOR_TYPES: tuple[LookO2SensorEntityDescription, ...] = (
    LookO2SensorEntityDescription(
        key="pm1",
        translation_key="pm1",
        native_unit_of_measurement=CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        device_class=SensorDeviceClass.PM1,
        suggested_display_precision=0,
        value_fn=lambda data: data.pm1,
    ),
    LookO2SensorEntityDescription(
        key="pm25",
        translation_key="pm25",
        native_unit_of_measurement=CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        device_class=SensorDeviceClass.PM25,
        suggested_display_precision=0,
        value_fn=lambda data: data.pm25,
    ),
    LookO2SensorEntityDescription(
        key="pm10",
        translation_key="pm10",
        native_unit_of_measurement=CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        device_class=SensorDeviceClass.PM10,
        suggested_display_precision=0,
        value_fn=lambda data: data.pm10,
    ),
    LookO2SensorEntityDescription(
        key="hcho",
        translation_key="hcho",
        native_unit_of_measurement=CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER,
        suggested_display_precision=0,
        value_fn=lambda data: data.hcho,
    ),
    LookO2SensorEntityDescription(
        key="temperature",
        translation_key="temperature",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        value_fn=lambda data: data.temperature,
    ),
    LookO2SensorEntityDescription(
        key="humidity",
        translation_key="humidity",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=0,
        value_fn=lambda data: data.humidity,
    ),
    LookO2SensorEntityDescription(
        key="aqi",
        translation_key="aqi",
        device_class=SensorDeviceClass.AQI,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=0,
        value_fn=lambda data: data.aqi,
    ),
    LookO2SensorEntityDescription(
        key="aqi_index",
        translation_key="aqi_index",
        device_class=SensorDeviceClass.ENUM,
        options=["hazardous", "bad", "satisfactory", "moderate", "good", "very_good"],
        value_fn=lambda data: data.aqi_string_en.lower().replace(" ", "_"),
    ),
    LookO2SensorEntityDescription(
        key="aqi_index_description",
        translation_key="aqi_index_description",
        device_class=SensorDeviceClass.ENUM,
        options=["hazardous", "bad", "satisfactory", "moderate", "good", "very_good"],
        entity_registry_enabled_default=False,
        value_fn=lambda data: data.aqi_string_en.lower().replace(" ", "_"),
    ),

    LookO2SensorEntityDescription(
        key="pm1_average",
        translation_key="pm1_average",
        native_unit_of_measurement=CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        device_class=SensorDeviceClass.PM1,
        suggested_display_precision=0,
        entity_registry_enabled_default=False,
        value_fn=lambda data: data.average_pm1,
    ),
    LookO2SensorEntityDescription(
        key="pm25_average",
        translation_key="pm25_average",
        native_unit_of_measurement=CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        device_class=SensorDeviceClass.PM25,
        suggested_display_precision=0,
        entity_registry_enabled_default=False,
        value_fn=lambda data: data.average_pm25,
    ),
    LookO2SensorEntityDescription(
        key="pm10_average",
        translation_key="pm10_average",
        native_unit_of_measurement=CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        device_class=SensorDeviceClass.PM10,
        suggested_display_precision=0,
        entity_registry_enabled_default=False,
        value_fn=lambda data: data.average_pm10,
    ),
    LookO2SensorEntityDescription(
        key="hcho_average",
        translation_key="hcho_average",
        native_unit_of_measurement=CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER,
        suggested_display_precision=0,
        entity_registry_enabled_default=False,
        value_fn=lambda data: data.average_hcho,
    ),
    LookO2SensorEntityDescription(
        key="color",
        translation_key="color",
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_registry_enabled_default=False,
        value_fn=lambda data: data.color,
    ),
    LookO2SensorEntityDescription(
        key="timestamp",
        translation_key="timestamp",
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_registry_enabled_default=False,
        value_fn=lambda data: data.timestamp,
    ),
)


async def async_setup_entry(
        hass: HomeAssistant,
        entry: LookO2ConfigEntry,
        async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator = entry.runtime_data.coordinator

    async_add_entities(
        LookO2SensorEntity(device_id, coordinator, description)
        for description in SENSOR_TYPES
        for device_id in entry.options[CONF_DEVICE_IDS]
    )


class LookO2SensorEntity(LookO2Entity, SensorEntity):
    entity_description: LookO2SensorEntityDescription

    def __init__(
            self,
            device_id: str,
            coordinator: LookO2DataUpdateCoordinator,
            description: LookO2SensorEntityDescription,
    ) -> None:
        """Initialize."""
        super().__init__(device_id, coordinator)

        self._attr_unique_id = f"looko2_sensor_{self._device_id}_{description.key}"
        self.entity_description = description

    @property
    def native_value(self) -> StateType:
        """Return the value reported by the sensor."""
        return self.entity_description.value_fn(self.coordinator.data[self._device_id])
