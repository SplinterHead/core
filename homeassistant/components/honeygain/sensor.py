"""Sensors for HoneyGain data."""
from homeassistant.components.sensor import (
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Sensor set up for HoneyGain config entry."""
    entities: list[SensorEntity] = []

    entities.append(HoneyGainBalanceSensor())

    async_add_entities(entities)


class HoneyGainBalanceSensor(SensorEntity):
    """Sensor to track account balance."""

    def __init__(self):
        """Initialise the sensor for the account balance."""
        self.entity_description = SensorEntityDescription(
            key="account_balance",
            name="Account Balance",
            icon="mdi:hand-coin",
            state_class=SensorStateClass.TOTAL,
        )

    @property
    def native_value(self) -> int:
        """Return the account balance."""
        return 123
