import time
from machine import Pin, PWM

time.sleep(.5)

MAX_U16 = 2**16 

ref_led = Pin(14, Pin.OUT)
ref_led.value(1)

pwm_led = PWM(Pin(15))
pwm_led.freq(1000)

i = 1

while True:
    i *= 2
    pwm_led.duty_u16(int(MAX_U16/i))

    print(f"duty cycle {100/i}%")
    if i > 16:
        i = 1

    time.sleep(3)