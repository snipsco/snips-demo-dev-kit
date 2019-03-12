# snips-demo-dev-kit

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/snipsco/snips-demo-dev-kit/blob/master/LICENSE)

Official action code for [Snips Voice Interaction Development Kit](https://www.seeedstudio.com/snips.html). 

## Usage

#### :bulb: Controlling a connected device

***```"Hey snips, please turn on my light"```***

***```"Sure, it's done"```***

#### :snowman: Asking for temperature

***```"Hey snips, please tell me the current temperature?"```***

***```"The current temperature is 24.4 degree."```***

#### :bamboo: Asking for humidity

***```"Hey snips, what's the humidity in the room?"```***

***```"The current humidity is 53.25% "```***

# Installation

1. Create a Snips account ***[here](https://console.snips.ai/?ref=Qr4Gq17mkPk)***
2. Create an assistant in ***[Snips console](https://console.snips.ai/)***
3. Add APP ***Snips - Dev Kit*** to your assistant
4. Deploy assistant by ***[Sam](https://snips.gitbook.io/documentation/console/deploy-your-assistant)***
5. (On Pi) Add permission to `_snips-skill` user to access gpio: `sudo usermod -a -G i2c,spi,gpio,audio _snips-skills`
6. (On Pi) Restart snips-skill-server: `sudo systemctl restart snips-skill-server`
7. Have fun ***;-)***

## Contributing

Please see the [Contribution Guidelines](https://github.com/snipsco/snips-demo-dev-kit/blob/master/CONTRIBUTING.md).

## Copyright

This library is provided by [Snips](https://www.snips.ai) as Open Source software. See [LICENSE](https://github.com/snipsco/snips-demo-dev-kit/blob/master/LICENSE) for more information.