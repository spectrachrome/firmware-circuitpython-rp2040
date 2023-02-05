# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT
"""CircuitPython status NeoPixel rainbow example."""


import time
import board
from rainbowio import colorwheel
import neopixel
import adafruit_adxl34x
import math
import wifi

# Get WiFi details from `secrets.py`` file
try:
    from secrets import secrets

    print("Connecting to %s"%secrets["ssid"])
    wifi.radio.connect(secrets["ssid"], secrets["password"])
    print("Connected to %s!"%secrets["ssid"])
    print("My IP address is", wifi.radio.ipv4_address)
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise


led = neopixel.NeoPixel(board.IO37, 7, bpp=4, pixel_order=neopixel.GRBW)
led.brightness = 0.1

i2c = board.I2C()
accelerometer = adafruit_adxl34x.ADXL343(i2c)

def rainbow(delay):
    for color_value in range(255):
        led.fill(colorwheel(color_value))
        time.sleep(delay)

def acceleration():
    average = [0 for i in range(20)]
    index = 0

    #last = 0.0
    #current = 0.0

    has_turned_red = False

    while True:
        (x, y, z) = accelerometer.acceleration

        #last = current

        average[index] = math.sqrt(x ** 2 + y ** 2 + z ** 2)
        sum = 0.0
        for v in average:
            sum += v
        delta = sum / len(average)
        hue = abs(90 - (delta - 9.5) * 90)
        print(round(abs(delta - 9.5)))

        if hue < 0: hue = 0
        if hue > 90: hue = 90

        c = colorwheel(hue)

        #current = math.sqrt(x ** 2 + y ** 2 + (z) ** 2)
        #delta = abs(current - last)
        #hue = 90 - delta * 90

        led.fill(c)

        if index == len(average) - 1:
            index = 0
        else:
            index += 1

        time.sleep(0.05)



acceleration()

"""

import time, random
import board, neopixel, rainbowio

num_leds = 7
leds = neopixel.NeoPixel(board.IO35, num_leds, bpp=4, brightness=0.1, auto_write=False )
delta_hue = 256//num_leds
speed = 500  # higher numbers = faster rainbow spinning
i = 0

while True:
    for l in range(len(leds)):
        leds[l] = rainbowio.colorwheel( int(i*speed + l * delta_hue) % 255  )
        leds.show()  # only write to LEDs after updating them all
        i = (i+1) % 255
        time.sleep(0.05)
"""
