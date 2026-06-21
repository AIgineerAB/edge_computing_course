import time
import requests
from wifi import connect_wifi
from machine import Pin
from gpio_lcd import GpioLcd

time.sleep(0.1)
connect_wifi()

url = "https://api.open-meteo.com/v1/forecast?latitude=57.7072&longitude=11.9668&current=temperature_2m&timezone=UTC"

response = requests.get(url).json()

current_temp = response.get("current").get("temperature_2m")
print(f"Outdoor temperature: {current_temp}°C")

lcd = GpioLcd(
    rs_pin=Pin(22),
    enable_pin=Pin(21),
    d4_pin=Pin(20),
    d5_pin=Pin(19),
    d6_pin=Pin(18),
    d7_pin=Pin(17),
    num_lines=2,
    num_columns=16,
)

lcd.clear()
lcd.putstr(f"Temp. G{chr(239)}teborg")
lcd.move_to(0,1)
lcd.putstr(f"{current_temp}{chr(223)}C hottu")