import time
import machine

time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")


led_external = machine.Pin(15, machine.Pin.OUT)

print(led_external)

while True:
  led_external.toggle()
  time.sleep(3)