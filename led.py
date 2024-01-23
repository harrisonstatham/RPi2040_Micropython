from machine import Pin
from utime import sleep

internal_led_pin = Pin("LED", Pin.OUT)


red_led_pin = Pin(13, Pin.OUT)
green_led_pin = Pin(14, Pin.OUT)
blue_led_pin = Pin(15, Pin.OUT)

print("LED starts flashing...")

red_led_pin.off()
green_led_pin.off()
blue_led_pin.off()

while True:
    try:
        red_led_pin.toggle()
        sleep(0.25) # sleep 1sec
        green_led_pin.toggle()
        sleep(0.25) # sleep 1sec
        blue_led_pin.toggle()

    except KeyboardInterrupt:
        break
red_led_pin.off()
green_led_pin.off()
blue_led_pin.off()
print("Finished.")