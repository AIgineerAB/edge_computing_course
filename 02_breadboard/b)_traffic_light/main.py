from machine import Pin
import time
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico W!")

led = dict(
    red = Pin(15, Pin.OUT),
    yellow = Pin(13, Pin.OUT),
    green = Pin(10, Pin.OUT)
)

colors = ("red", "yellow", "green")

while True:
    for color in colors:
        led[color].value(1)
        # turn off the other LEDs
        remaining_colors = tuple(c for c in colors if c != color)
        led[remaining_colors[0]].value(0)
        led[remaining_colors[1]].value(0)

        time.sleep(2)
