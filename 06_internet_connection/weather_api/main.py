import time
from wifi import connect_wifi
import requests
from machine import Pin


time.sleep(0.1)

led = Pin(15, Pin.OUT)

if connect_wifi():
    led.value(1)


url = "https://api.open-meteo.com/v1/forecast?latitude=57.7072&longitude=11.9668&current=temperature_2m&timezone=UTC"

response = requests.get(url).json()

outdoor_temperature = response.get("current").get("temperature_2m")

print(f"Outdoor temperature is {outdoor_temperature}°C")
