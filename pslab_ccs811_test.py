#!/usr/bin/python3
# pslab_cs811_test.py

import time

from pslab.external.ccs811 import CCS811
dev = CCS811()
time.sleep(0.05)


print('dev.appStart()')
dev.appStart()
time.sleep(15)


# time.sleep(1)
print("dev.setMeasureMode(CCS811.MODE_CONTINUOUS)")
dev.setMeasureMode(CCS811.MODE_CONTINUOUS)


while (1):
    time.sleep(1.3)

    print('\ndev.getStatus()')
    status = dev.getStatus()
    dev.decodeStatus(status)

    # time.sleep(1)
    print("dev.measure()")

    dev.measure()
    # time.sleep(0.1)
