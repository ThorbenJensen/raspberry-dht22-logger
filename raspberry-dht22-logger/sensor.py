# READ FROM SENSOR

import sys
import Adafruit_DHT


def read_sensor(sensor=22, pin=4):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return humidity, temperature


if __name__ == "__main__":
    """Read humidity and temperature from sensor, print results."""
    humidity, temperature = read_sensor()

    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature,
                                                          humidity))
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)
