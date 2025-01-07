import datetime
from dataclasses import dataclass
from typing import Self

type LookO2DevicesDataMap = dict[str, LookO2DeviceData]


@dataclass
class LookO2DeviceData:
    device_id: str
    pm1: float
    pm25: float
    pm10: float
    timestamp: datetime.datetime
    latitude: float
    longitude: float
    aqi: int
    aqi_string_pl: str
    aqi_string_en: str
    aqi_description_pl: str
    aqi_description_en: str
    color: str
    temperature: float
    humidity: float
    average_pm1: float
    average_pm25: float
    average_pm10: float
    name: str
    indoor: bool
    previous_aqi: int
    hcho: float
    average_hcho: float

    @classmethod
    def from_dict(cls: type[Self], data: dict[str, str]) -> Self:
        return cls(
            device_id=data["Device"],
            pm1=float(data["PM1"]),
            pm25=float(data["PM25"]),
            pm10=float(data["PM10"]),
            timestamp=datetime.datetime.fromtimestamp(int(data["Epoch"])),
            latitude=float(data["Lat"]),
            longitude=float(data["Lon"]),
            aqi=int(data["IJP"]),
            aqi_string_pl=data["IJPString"],
            aqi_string_en=data["IJPStringEN"],
            aqi_description_pl=data["IJPDescription"],
            aqi_description_en=data["IJPDescriptionEN"],
            color=data["Color"],
            temperature=float(data["Temperature"]),
            humidity=float(data["Humidity"]),
            average_pm1=float(data["AveragePM1"]),
            average_pm25=float(data["AveragePM25"]),
            average_pm10=float(data["AveragePM10"]),
            name=data["Name"],
            indoor=data["Indoor"] == '0',
            previous_aqi=int(data["PreviousIJP"]),
            hcho=float(data["HCHO"]),
            average_hcho=float(data["AverageHCHO"]),
        )
