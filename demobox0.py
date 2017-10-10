#!/usr/bin/env python

from time import sleep
from libacquavisual import thermometer, hygrometer, glassofwater
from libardurep import datastore, datareporter, serialreader

if __name__ == '__main__':

    temp = thermometer.Thermometer()
    hum = hygrometer.Hygrometer()
    glass = glassofwater.GlassOfWater()

    store = datastore.DataStore()
    reader = serialreader.SerialReader('/dev/ttyACM0', 9600, store, 0)
    reader.start()

    sleep(8)

    glass.calibrate(zero=38, value=float(store.data["water_distance"]["value"]))

    while True:
        sleep(1)
        try:
            print "T" + str(store.data["env_temperature"]["value"])
            temp.display_value(float(store.data["env_temperature"]["value"]))
            print "H" + str(store.data["env_humidity"]["value"])
            hum.display_value(float(store.data["env_humidity"]["value"]))
            print "W" + str(store.data["water_distance"]["value"])
            glass.display_value(float(store.data["water_distance"]["value"]))
        except KeyError as e:
            # Wait for next iter
            print e

    reader.halt()

