<img align="right" src="docs/devKit.png" width="150">

[![Version](https://img.shields.io/badge/snips--demo--dev--kit-v0.2.0-green.svg)](https://github.com/snipsco/snips-demo-dev-kit/blob/master/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/snipsco/snips-demo-dev-kit/blob/master/LICENSE)

## snips-demo-dev-kit

Official action code for [Snips Voice Interaction Development Kit](https://www.seeedstudio.com/snips.html). 

It's composed of [snips-app-relay-switch](https://github.com/snipsco/snips-app-relay-switch/) and [snips-app-sht31](https://github.com/snipsco/snips-app-sht31/), enables you to control the connected relay module and fetch the indoor environment informations.

## Usage

#### :bulb: Controlling a connected device

***```"Hey snips, please turn on my light"```***

#### :snowman: Asking for temperature

***```"Hey snips, please tell me the current temperature?"```***

#### :bamboo: Asking for humidity

***```"Hey snips, what's the humidity in the room?"```***

## Installation

### Pre-required

Please make sure that `_snips-skills` user has permission to access `gpio` and `i2c`.

To grant this permission, run the following command **on Raspberry Pi**:

```
sudo usermod -a -G i2c,spi,gpio,audio _snips-skills
```

### With assistant (Recommend)

1. Create a Snips account **[here](https://console.snips.ai/signup)**

<p align="center">
    <img src="docs/register.png" height="350">
</p>

2. Create an assistant in **[Snips Console](https://console.snips.ai/)**

<p align="center">
    <img src="docs/createAssistant.png" height="350">
</p>

3. Add **Voice Interaction Dev Kit** App to your assistant

<p align="center">
    <img src="docs/addApp.png" height="350">
</p>

4. Deploy assistant by executing the provided command **On your laptop**

<p align="center">
    <img src="docs/deployAssistant.png" height="350">
</p>

5. Start playing **:rocket:**

### Only action code

1. Fetch action code **on your laptop**

```
sam install actions -g https://github.com/snipsco/snips-demo-dev-kit.git
```

2. Start playing **:rocket:**

## Configurations

### Connection

| Config | Description | Value | Default |
| --- | --- | --- | --- |
| `mqtt_host` | MQTT host name | `<ip address>`/`<hostname>` | `localhost` |
| `mqtt_port` | MQTT port number | `<mqtt port>` | `1883` |
| `site_id` | Snips device ID | Refering to the actual `snips.toml` | `snips-base` |

##### :bangbang: ***If this skill is installed on a satellite device, please change the `site_id` to the one set for satellite, and change `mqtt_host` connecting to master device.***

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
