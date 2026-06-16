from machine import PWM, Pin, ADC
import time 

time.sleep(.1)

potentiometer = ADC(Pin(26))
led_dimmer = PWM(Pin(14))
led_dimmer.freq(1000)

led_ref = Pin(15, Pin.OUT)

led_ref.value(1)

while True:
    print(potentiometer.read_u16())
    led_dimmer.duty_u16(potentiometer.read_u16())
    time.sleep(.1)