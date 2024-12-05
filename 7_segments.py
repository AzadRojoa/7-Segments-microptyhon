from machine import Pin,PWM
import time
tab = [13,12,14,27,26,25,33,32]

for i in tab:
    pin = Pin(i, mode=Pin.OUT)
    pin.value(1)