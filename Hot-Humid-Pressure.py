# Author: Malik Williams
# Date: 03-08-19
# Program Description: This program triggers the red_led whenever the Temperature
#                     and Humidity cross a certain Threshold.

# Imports the Following libraries into the Program.
import board
import busio 
import time  # Time Library
import adafruit_bme280 # bme280; Temperature, Pressure, Humidity, and Altitude Sensor.
import sys
import datetime
import digitalio # I2C Controller Essentially



# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# Sets the pin and the value for the LED GREEN Pin.
led_green = digitalio.DigitalInOut(board.D18)
led_green.direction = digitalio.Direction.OUTPUT
led_green.value = True

# Sets the Pin on the T-Cobbler for the red_pin.
led_red = digitalio.DigitalInOut(board.D4)
led_red.direction = digitalio.Direction.OUTPUT
led_red.value = False

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25

# Sets the Thresholds for the Hot and Humid Triggers.
# These values can also be switched to user input too (maaaaaybe voice input later on).
hot = 74
humid = 46

# Sets the condition for the Loop below, and set's the current date & time reader.
condition = True
currentDT = datetime.datetime.now()

# While Loop that controls the led Hot/Humid Triggers.
while condition == True:
    if ((bme280.humidity) > humid or (bme280.temperature*1.8+32) > hot):
        #Sets led_green to off and prints out the values for hot/Humid.
        led_green.value = False
        print("\nHUMID: %0.1f %%" % bme280.humidity)
        print("\nTemperature: %0.1f F" % (bme280.temperature*1.8+32))
        print(str(currentDT))
        # Sets the red_led to flash for an error alarm.
        for i in range (0, 6):
            led_red.value = False
            time.sleep(0.5)
            led_red.value = True
            time.sleep(0.5)
            print("\nHUMID: %0.1f %%" % bme280.humidity)
            print("\nTemperature: %0.1f F" % (bme280.temperature*1.8+32))
        # Re-Sets the condition for when the Hot/Humid trigger shuts off.
        if ((bme280.humidity) < humid and (bme280.temperature*1.8+32) < hot):
            condition = False

# Prints out the final values for the below threshold values and resets the leds.
print("Temperature and Humidity have been restored to normal levels.")
led_red.value = False
led_green.value = True
# EXTRA NOTES:::
# What this program is also trying to show, is that it's constantly readnig
# ....even if it's not printing anything out.
# File I/O Below for later use.
#f.write("\nTemperature: %0.1f F" % (bme280.temperature*1.8+32))
#f.write("\nHumidity: %0.1f %%" % bme280.humidity)
#f.write("\nPressure: %0.1f hPa" % bme280.pressure)
#f.write("\nAltitude = %0.2f meters" % bme280.altitude)
# -----------------------------------------------------------------
# SPI CONFIGURATION
# OR create library object using our Bus SPI port
#spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
#bme_cs = digitalio.DigitalInOut(board.D10)
#bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)