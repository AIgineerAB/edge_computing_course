from machine import Pin
import time

time.sleep(0.5)


button_state = {"pressed": False, "last_interrupt_time": 0}

buzzer = Pin(11, Pin.OUT)

# pullup keeps pin at high state (1) by default
# pin reads 1 when button NOT pressed, when button is pressed it connects to ground 0
button = Pin(13, Pin.IN, Pin.PULL_UP)
led = {"red": Pin(15, Pin.OUT), "green": Pin(14, Pin.OUT)}


def button_callback(pin):
    current_time = time.ticks_ms()
    if (current_time - button_state["last_interrupt_time"]) > 200:
        button_state["pressed"] = False if button_state["pressed"] else True
        button_state["last_interrupt_time"] = current_time


button.irq(trigger=Pin.IRQ_FALLING, handler=button_callback)

while True:
    if button_state["pressed"]:
        led["red"].value(0)
        led["green"].value(1)

        for i in range(10):
            buzzer.value(1)
            time.sleep(0.1)
            buzzer.value(0)
            time.sleep(0.3)

        for i in range(10):
            time.sleep(0.5)
            led["green"].toggle()

    button_state["pressed"] = False
    led["red"].value(1)
    led["green"].value(0)
    time.sleep(3)
