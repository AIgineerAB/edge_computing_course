from wifi import connect_wifi
import time 
from dht import DHT11
from machine import Pin
from umqtt.simple import MQTTClient
import json


time.sleep(.5)

sensor = DHT11(Pin(16))
led = Pin(15, Pin.OUT)

led.value(0)

MQTT_BORKER = "192.168.1.141"
TOPIC = b"home/pico/dht11"

if connect_wifi():
    led.value(1)

def connect_mqtt():
    client = MQTTClient(client_id="pico", server=MQTT_BORKER, port = 1883)
    client.connect()
    print("Connected to MQTT")
    return client

client = connect_mqtt()

while True:
    sensor.measure()
    temp = sensor.temperature()
    humidity = sensor.humidity()

    data = {"temperature": temp, "humidity": humidity}
    payload = json.dumps(data)
    client.publish(TOPIC, payload)
    
    print(f"sent: {payload} to mosquitto" )
    time.sleep(3)