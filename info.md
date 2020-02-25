## Configuration options

| Key | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `name` | `string` | `False` | `LookO2` | Name of sensor |
| `api_key` | `string` | `True` | - | API key for Look02 |
| `station_id` | `string` | `True` | - | ID of monitored station |
| `monitored_conditions` | `list` | `True` | - | List of conditions to monitor |
| `scan_interval` | `time period` | `False` | `00:20:00` | Interval between sensor updates |

### Possible monitored conditions

| Key | Description |
| --- | --- | 
| `AverageHCHO` | Average value of HCHO |
| `AveragePM1` | Average value of PM1 |
| `AveragePM10` | Average value of PM10 |
| `AveragePM25` | Average value of PM2.5 |
| `Color` | Color of sensor, indicating quality of air |
| `HCHO` | Current value of HCHO |
| `Humidity` | Current value of humidity |
| `IJP` | Current value of air quality index |
| `IJPDescription` | Description of current air quality |
| `IJPDescriptionEN` | English description of current air quality |
| `IJPString` | Name of current air quality value |
| `IJPStringEN` | English name of current air quality value |
| `Indoor` | Indicates that sensor is mounted indoor |
| `PM1` | Current value of PM1 |
| `PM10` | Current value of PM10 |
| `PM25` | Current value of PM2.5 |
| `PreviousIJP` | Previous value of air quality index |
| `Temperature` | Current value of temperature |

## Example usage

```
sensor:
  - platform: looko2
    api_key: !secret looko2.api_key
    name: LookO2
    station_id: '5CCF7F0C2E8B'
    monitored_conditions:
      - 'AverageHCHO'
      - 'AveragePM1'
      - 'AveragePM10'
      - 'AveragePM25'
      - 'Color'
      - 'HCHO'
      - 'Humidity'
      - 'IJP'
      - 'IJPDescription'
      - 'IJPDescriptionEN'
      - 'IJPString'
      - 'IJPStringEN'
      - 'Indoor'
      - 'PM1'
      - 'PM10'
      - 'PM25'
      - 'PreviousIJP'
      - 'Temperature'
    scan_interval:
      hours: 1
      minutes: 2
      seconds: 3
```

## FAQ

* **How to get API key?**
  
  To get API key follow steps available at [*official project page*](https://burze.dzis.net/?page=api_interfejs).
