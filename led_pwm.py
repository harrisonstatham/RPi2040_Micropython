# Sam's favorite!!
# Lets PWM to the MAX just for him.

import time
from machine import Pin, PWM

pwm = PWM(Pin(14))

pwm.freq(1000) # Something Sam cant see...

duty = 0
direction = 1

for _ in range(8*256):
    duty += direction

    if duty > 255:
        duty = 255
        direction = -1

    elif duty < 0:
        duty = 0
        direction = 1
    
    # duty_u16 goes from 0 to 65535 (256*256)
    pwm.duty_u16(duty*duty)
    time.sleep(0.01)
