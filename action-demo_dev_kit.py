#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from snipsTools import SnipsConfigParser
from RelaySwitch import RelaySwitch
from SHT31 import SHT31
from SnipsClients import SnipsMPU

CONFIG_INI = 'config.ini'

config = SnipsConfigParser.read_configuration_file(CONFIG_INI).get('global')

MQTT_ADDR_HOST = str(config.get('mqtt_host'))
MQTT_ADDR_PORT = str(config.get('mqtt_port'))
MQTT_ADDR = "{}:{}".format(MQTT_ADDR_HOST, MQTT_ADDR_PORT)

RELAY_GPIO = int(config.get('relay_gpio'))
TEMP_UNIT = str(config.get('temperature_unit'))

relay = RelaySwitch.RelaySwitch('screen', RELAY_GPIO)
sht31 = SHT31.SHT31(TEMP_UNIT)

client = SnipsMPU.SnipsMPU(MQTT_ADDR, relay, sht31)

if __name__ == "__main__":
    try:
        client.start_block()

    except KeyboardInterrupt:
        relay.clear()