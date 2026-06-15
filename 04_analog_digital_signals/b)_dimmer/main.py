import time
from machine import Pin, PWM, ADC

time.sleep(0.1) # Wait for USB to become ready

potentiometer = ADC(Pin(26))
led = PWM(Pin(15))
led.freq(1000)

while True:
    print(potentiometer.read_u16())
    led.duty_u16(potentiometer.read_u16())