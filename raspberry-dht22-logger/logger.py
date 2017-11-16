# LOG TO CSV

import sensor


def log():
    humidity, temperature = sensor.read_sensor()

    if humidity is not None and temperature is not None:
        print('{0:0.1f},{1:0.1f}'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')
        print('Humidity: ' + str(humidity))
        print('Temperature: ' + str(temperature))


if __name__ == "__main__":
    for i in range(10):
        log()
