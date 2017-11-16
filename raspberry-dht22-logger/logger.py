# LOG TO CSV

import sensor


def log(file_path='../log/log.csv', verbose=True):
    humidity, temperature = sensor.read_sensor()
    if verbose:
        print('{0:0.1f},{1:0.1f}'.format(temperature, humidity))
    # write to file
    with open(file_path, 'a') as myfile:
        myfile.write(str(humidity) + ',' + str(temperature))


if __name__ == "__main__":
    log('../log/log.csv', True)
