[![HACS Default][hacs_shield]][hacs]
[![GitHub Latest Release][releases_shield]][latest_release]
[![GitHub All Releases][downloads_total_shield]][releases]
[![Buy me a coffee][buy_me_a_coffee_shield]][buy_me_a_coffee]
[![PayPal.Me][paypal_me_shield]][paypal_me]

[hacs_shield]: https://img.shields.io/static/v1.svg?label=HACS&message=Default&style=popout&color=green&labelColor=41bdf5&logo=HomeAssistantCommunityStore&logoColor=white
[hacs]: https://hacs.xyz/docs/default_repositories

[latest_release]: https://github.com/PiotrMachowski/Home-Assistant-custom-components-Looko2/releases/latest
[releases_shield]: https://img.shields.io/github/release/PiotrMachowski/Home-Assistant-custom-components-Looko2.svg?style=popout

[releases]: https://github.com/PiotrMachowski/Home-Assistant-custom-components-Looko2/releases
[downloads_total_shield]: https://img.shields.io/github/downloads/PiotrMachowski/Home-Assistant-custom-components-Looko2/total

[buy_me_a_coffee_shield]: https://img.shields.io/static/v1.svg?label=%20&message=Buy%20me%20a%20coffee&color=6f4e37&logo=buy%20me%20a%20coffee&logoColor=white
[buy_me_a_coffee]: https://www.buymeacoffee.com/PiotrMachowski

[paypal_me_shield]: https://img.shields.io/static/v1.svg?label=%20&message=PayPal.Me&logo=paypal
[paypal_me]: https://paypal.me/PiMachowski

# LookO2 sensor

This sensor uses official API to get air quality data from [*LookO2*](https://looko2.com/).

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

## Installation

### Using [HACS](https://hacs.xyz/) (recommended)

This integration can be installed using HACS.
To do it search for `LookO2` in *Integrations* section.

### Manual

To install this integration manually you have to download [*looko2.zip*](https://github.com/PiotrMachowski/Home-Assistant-custom-components-Looko2/releases/latest/download/looko2.zip) and extract its contents to `config/custom_components/looko2` directory:
```bash
mkdir -p custom_components/looko2
cd custom_components/looko2
wget https://github.com/PiotrMachowski/Home-Assistant-custom-components-Looko2/releases/latest/download/looko2.zip
unzip looko2.zip
rm looko2.zip
```

## FAQ

* **How to get API key?**
  
  To get API key follow steps available at [*official project page*](https://looko2web.nazwa.pl/aktualnosci/api/).

<a href="https://www.buymeacoffee.com/PiotrMachowski" target="_blank"><img src="https://bmc-cdn.nyc3.digitaloceanspaces.com/BMC-button-images/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>
<a href="https://paypal.me/PiMachowski" target="_blank"><img src="https://www.paypalobjects.com/webstatic/mktg/logo/pp_cc_mark_37x23.jpg" border="0" alt="PayPal Logo" style="height: auto !important;width: auto !important;"></a>
