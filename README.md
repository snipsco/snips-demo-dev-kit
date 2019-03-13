# snips-demo-dev-kit

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/snipsco/snips-demo-dev-kit/blob/master/LICENSE)

Official action code for [Snips Voice Interaction Development Kit](https://www.seeedstudio.com/snips.html).

This action code is composed of [snips-app-relay-switch](https://github.com/snipsco/snips-app-relay-switch/) and [snips-app-sht31](https://github.com/snipsco/snips-app-sht31/), enables you to control the connected relay module and fetch the indoor environment informations.

## Usage

#### :bulb: Controlling a connected device

***```"Hey snips, please turn on my light"```***

***```"Relay has been turned on"```***

#### :snowman: Asking for temperature

***```"Hey snips, please tell me the current temperature?"```***

***```"The current temperature is 24.4 degree."```***

#### :bamboo: Asking for humidity

***```"Hey snips, what's the humidity in the room?"```***

***```"The current humidity is 53.25% "```***

# Installation

### With assistant (Recommend)

1. Create a Snips account **[here](https://console.snips.ai/signup)**

<p align="center">
    <img src="docs/register.png" height="350">
</p>

2. Create an assistant in **[Snips console](https://console.snips.ai/)**

<p align="center">
    <img src="docs/createAssistant.png" height="350">
</p>

3. Add `Voice Interaction Dev Kit` APP **Snips - Dev Kit** to your assistant

<p align="center">
    <img src="docs/addApp.png" height="350">
</p>

4. Deploy assistant by **[Sam](https://snips.gitbook.io/documentation/console/deploy-your-assistant)**

<p align="center">
    <img src="docs/deployAssistant.png" height="350">
</p>

5. Grant `_snips-skill` user permission to access `GPIO` and `I2C` **(On Raspberry Pi)**

```
sudo usermod -a -G i2c,spi,gpio,audio _snips-skills
```

6. Restart `snips-skill-server` **(On Raspberry Pi)**

```
sudo systemctl restart snips-skill-server
```

7. Start playing **:rocket:**

### Only action code

1. Fetch action code **(On your laptop)**

```
sam install actions -g https://github.com/snipsco/snips-demo-dev-kit.git
```

2. Grant `i2c` and `gpio` accessing to `_snips-skill` **(On Raspberry Pi)**

```
sudo usermod -a -G i2c,spi,gpio,audio _snips-skills
```

## Configurations

### Connection

| Config | Description | Value | Default |
| --- | --- | --- | --- |
| `mqtt_host` | MQTT host name | `<ip address>`/`<hostname>` | `localhost` |
| `mqtt_port` | MQTT port number | `<mqtt port>` | `1883` |
| `site_id` | Snips device ID | Refering to the actual `snips.toml` | `snips-base` |

 ##### :bangbang: ***To make satellite work correctly, please change here***

### Relay GPIO pin

| Config | Description | Value | Default |
| --- | --- | --- | --- |
| `relay_gpio_bcm` | The BCM GPIO number | [Available BCM pin number](https://www.raspberrypi.org/documentation/usage/gpio/README.md) | `12` |

### Temperature Unit

| Config | Description | Value | Default |
| --- | --- | --- | --- |
| `temperature_unit` | The unit applied to temperature | `celsius`, `fahrenheit` | `celsius` |

## Contributing

Please see the [Contribution Guidelines](https://github.com/snipsco/snips-demo-dev-kit/blob/master/CONTRIBUTING.md).

## Copyright

This library is provided by [Snips](https://www.snips.ai) as Open Source software. See [LICENSE](https://github.com/snipsco/snips-demo-dev-kit/blob/master/LICENSE) for more information.