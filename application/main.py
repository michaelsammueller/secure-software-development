from sensors.geigercounter import GeigerCounter
from sensors.thermometer import Thermometer

if __name__ == '__main__':
    t = Thermometer()
    g = GeigerCounter()
    print(t)
    print(g)

