# [`firmware-circuitpython-rp2040`](https://github.com/spectrachrome/firmware-circuitpython-rp2040)

This repository contains LEDswarm firmware written in CircuitPython for controllers based on the Pico W. Drivers are set up to support the [ADXL343 accelerometer](https://www.analog.com/en/products/adxl343.html), although any ADXL34x device can be used.

## Dependencies

The following dependencies are needed for the project to work correctly:

* [`adafruit_bus_device`](https://github.com/adafruit/Adafruit_CircuitPython_BusDevice)
* [`adafruit_adxl34x`](https://github.com/adafruit/Adafruit_CircuitPython_ADXL34x)

Note that these are already set up in the [`lib`](https://github.com/spectrachrome/firmware-circuitpython-esp32/tree/main/lib) folder of this repository. You may also install any desired version yourself by manually putting it into the `lib` folder of your `CIRCUITPY` drive.