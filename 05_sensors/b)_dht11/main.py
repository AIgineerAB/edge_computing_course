from dht import DHT11
from machine import Pin
import time 

time.sleep(.5)

sensor = DHT11(Pin(16))

while True:
    sensor.measure()
    print(f"Temperature: {sensor.temperature()}°C")
    print(f"Humidity: {sensor.humidity()}%")
    time.sleep(1)