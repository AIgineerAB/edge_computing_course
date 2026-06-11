from machine import ADC, Pin
import time 

time.sleep(.5)

temp_sensor = ADC(ADC.CORE_TEMP)
warning_lamp = Pin(15, Pin.OUT)


# analog -> digital -> voltage -> temp C

VOLTAGE_FACTOR = 3.3/65536
THRESHOLD = 27

with open("temps.txt", "w") as file:
    while True:
        adc_voltage = temp_sensor.read_u16() * VOLTAGE_FACTOR
        temp_celcius = 27 - (adc_voltage-0.706)/0.001721

        temp_log = f"\nTemperature °C: {temp_celcius}. "

        if temp_celcius > THRESHOLD:
            temp_log += "CRITICALLY HIGH."
            warning_lamp.value(1)
        else:
            temp_log += "GOOD TEMP."
            warning_lamp.value(0)

        file.write(temp_log)
        file.flush()
        print(temp_log)
        time.sleep(5)
    