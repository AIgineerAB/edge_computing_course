import rp2
import network
import json
import time


rp2.country("SE")

with open("wifi_credentials.json") as file:
    credentials = json.load(file)

def connect_wifi(waiting_time = 10):

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(credentials.get("WIFI_SSID"), credentials.get("WIFI_PASSWORD"))

    # print(wlan)
    # print(f"{wlan.ifconfig()}")

    while waiting_time > 0:
        if wlan.isconnected():
            print("Connected to wifi")
            break

        waiting_time -= 1
        print("Trying to connect to wifi")
        time.sleep(1)

    # print(f"Connected to wifi: {wlan.isconnected()}")
    return wlan.isconnected()
