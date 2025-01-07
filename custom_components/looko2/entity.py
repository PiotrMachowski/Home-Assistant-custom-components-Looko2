from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import ATTRIBUTION
from .coordinator import LookO2DataUpdateCoordinator


class LookO2Entity(CoordinatorEntity[LookO2DataUpdateCoordinator]):
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name = True

    def __init__(
            self,
            device_id: str,
            coordinator: LookO2DataUpdateCoordinator,
    ) -> None:
        """Initialize."""
        super().__init__(coordinator)
        self._device_id = device_id
        self._attr_device_info = coordinator.device_infos[device_id]
