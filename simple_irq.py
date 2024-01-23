
from machine import Pin
from utime import sleep

p2 = Pin(2, Pin.IN, Pin.PULL_UP)
led_pin = Pin("LED", Pin.OUT)

p2.irq(lambda p: print("IRQ with flags:", p.irq().flags()), Pin.IRQ_FALLING)

while True:
    led_pin.toggle()
    sleep(0.25)