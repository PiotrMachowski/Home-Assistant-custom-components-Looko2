[![HACS Default][hacs_shield]][hacs]
[![GitHub Latest Release][releases_shield]][latest_release]
[![GitHub All Releases][downloads_total_shield]][releases]<!-- piotrmachowski_support_badges_start -->
[![Ko-Fi][ko_fi_shield]][ko_fi]
[![buycoffee.to][buycoffee_to_shield]][buycoffee_to]
[![PayPal.Me][paypal_me_shield]][paypal_me]
[![Revolut.Me][revolut_me_shield]][revolut_me]
<!-- piotrmachowski_support_badges_end -->

[hacs_shield]: https://img.shields.io/static/v1.svg?label=HACS&message=Default&style=popout&color=green&labelColor=41bdf5&logo=HomeAssistantCommunityStore&logoColor=white
[hacs]: https://hacs.xyz/docs/default_repositories

[latest_release]: https://github.com/PiotrMachowski/Home-Assistant-custom-components-Looko2/releases/latest
[releases_shield]: https://img.shields.io/github/release/PiotrMachowski/Home-Assistant-custom-components-Looko2.svg?style=popout

[releases]: https://github.com/PiotrMachowski/Home-Assistant-custom-components-Looko2/releases
[downloads_total_shield]: https://img.shields.io/github/downloads/PiotrMachowski/Home-Assistant-custom-components-Looko2/total

# LookO2 integration

This sensor uses official API to get air quality data from [*LookO2*](https://looko2.com/).

## Configuration

To configure this integration search for `LookO2` on *Integrations* page.
Alternatively you can just use the button below:

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=looko2)

Available data (depending on device model):
 - PM1
 - PM2.5
 - PM10
 - Formaldehyde
 - Air Quality Index
 - Temperature
 - Humidity

For more precise information about data visit [*looko2.pl*](https://looko2.pl/).



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
  
  To get API key follow steps available at [*official project page*](https://looko2.pl/aktualnosci/api/).


<!-- piotrmachowski_support_links_start -->

## Support

If you want to support my work with a donation you can use one of the following platforms:

<table>
  <tr>
    <th>Platform</th>
    <th>Payment methods</th>
    <th>Link</th>
    <th>Comment</th>
  </tr>
  <tr>
    <td>Ko-fi</td>
    <td>
      <li>PayPal</li>
      <li>Credit card</li>
    </td>
    <td>
      <a href='https://ko-fi.com/piotrmachowski' target='_blank'><img height='35px' src='https://storage.ko-fi.com/cdn/kofi6.png?v=6' border='0' alt='Buy Me a Coffee at ko-fi.com' />
    </td>
    <td>
      <li>No fees</li>
      <li>Single or monthly payment</li>
    </td>
  </tr>
  <tr>
    <td>buycoffee.to</td>
    <td>
      <li>BLIK</li>
      <li>Bank transfer</li>
    </td>
    <td>
      <a href="https://buycoffee.to/piotrmachowski" target="_blank"><img src="https://buycoffee.to/btn/buycoffeeto-btn-primary.svg" height="35px" alt="Postaw mi kawę na buycoffee.to"></a>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>PayPal</td>
    <td>
      <li>PayPal</li>
    </td>
    <td>
      <a href="https://paypal.me/PiMachowski" target="_blank"><img src="https://www.paypalobjects.com/webstatic/mktg/logo/pp_cc_mark_37x23.jpg" border="0" alt="PayPal Logo" height="35px" style="height: auto !important;width: auto !important;"></a>
    </td>
    <td>
      <li>No fees</li>
    </td>
  </tr>
  <tr>
    <td>Revolut</td>
    <td>
      <li>Revolut</li>
      <li>Credit Card</li>
    </td>
    <td>
      <a href="https://revolut.me/314ma" target="_blank"><img src="https://assets.revolut.com/assets/favicons/favicon-32x32.png" height="32px" alt="Revolut"></a>
    </td>
    <td>
      <li>No fees</li>
    </td>
  </tr>
</table>

### Powered by
[![PyCharm logo.](https://resources.jetbrains.com/storage/products/company/brand/logos/jetbrains.svg)](https://jb.gg/OpenSourceSupport)


[ko_fi_shield]: https://img.shields.io/static/v1.svg?label=%20&message=Ko-Fi&color=F16061&logo=ko-fi&logoColor=white

[ko_fi]: https://ko-fi.com/piotrmachowski

[buycoffee_to_shield]: https://shields.io/badge/buycoffee.to-white?style=flat&labelColor=white&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABhmlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw1AUhU9TpaIVh1YQcchQnayIijhKFYtgobQVWnUweemP0KQhSXFxFFwLDv4sVh1cnHV1cBUEwR8QVxcnRRcp8b6k0CLGC4/3cd49h/fuA4R6malmxzigapaRisfEbG5FDLzChxB6MIZ+iZl6Ir2QgWd93VM31V2UZ3n3/Vm9St5kgE8knmW6YRGvE09vWjrnfeIwK0kK8TnxqEEXJH7kuuzyG+eiwwLPDBuZ1BxxmFgstrHcxqxkqMRTxBFF1ShfyLqscN7irJarrHlP/sJgXltOc53WEOJYRAJJiJBRxQbKsBClXSPFRIrOYx7+QcefJJdMrg0wcsyjAhWS4wf/g9+zNQuTE25SMAZ0vtj2xzAQ2AUaNdv+PrbtxgngfwautJa/UgdmPkmvtbTIEdC3DVxctzR5D7jcAQaedMmQHMlPSygUgPcz+qYcELoFulfduTXPcfoAZGhWSzfAwSEwUqTsNY93d7XP7d+e5vx+AIahcq//o+yoAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH5wETCy4vFNqLzwAAAVpJREFUOMvd0rFLVXEYxvHPOedKJnKJhrDLuUFREULE7YDCMYj+AydpsCWiaKu29hZxiP4Al4aWwC1EdFI4Q3hqEmkIBI8ZChWXKNLLvS0/Qcza84V3enm/7/s878t/HxGkeTaIGziP+EB918nawu7Dq1d0e1+2J2bepnk2jFEUVVF+qKV51o9neBCaugfge70keoxxUbSWjrQ+4SUyzKZ5NlnDZdzGG7w4DIh+dtZEFntDA98l8S0MYwctNGrYz9WqKJePFLq80g5Sr+EHlnATp+NA+4qLaZ7FfzMrzbMBjGEdq8GrJMZnvAvFC/8wfAwjWMQ8XmMzaW9sdevNRgd3MFhvNpbaG1u/Dk2/hOc4gadVUa7Um425qii/7Z+xH9O4jwW8Cqv24Tru4hyeVEU588cfBMgpPMI9nMFe0BkFzVOYrYqycyQgQJLwTC2cDZCPeF8V5Y7jGb8BUpRicy7OU5MAAAAASUVORK5CYII=

[buycoffee_to]: https://buycoffee.to/piotrmachowski

[buy_me_a_coffee_shield]: https://img.shields.io/static/v1.svg?label=%20&message=Buy%20me%20a%20coffee&color=6f4e37&logo=buy%20me%20a%20coffee&logoColor=white

[buy_me_a_coffee]: https://www.buymeacoffee.com/PiotrMachowski

[paypal_me_shield]: https://img.shields.io/static/v1.svg?label=%20&message=PayPal.Me&logo=paypal

[paypal_me]: https://paypal.me/PiMachowski

[revolut_me_shield]: https://img.shields.io/static/v1.svg?label=%20&message=Revolut&logo=revolut

[revolut_me]: https://revolut.me/314ma
<!-- piotrmachowski_support_links_end -->