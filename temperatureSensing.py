import board
import busio
import time
import adafruit_bme280
import sys
import datetime
import digitalio

print("HelloBlinky\n")

led = digitalio.DigitalInOut(board.D4)
led.direction = digitalio.Direction.OUTPUT
led.value = True

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# OR create library object using our Bus SPI port
#spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
#bme_cs = digitalio.DigitalInOut(board.D10)
#bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25
currentDT = datetime.datetime.now()

#sys.stdout = f
# What this program is also trying to show, is that it's constantly readnig
# ....even if it's not printing anything out. 
while True:
    f = open('Humidity-Temp-Readings.txt','w')
    f.write("\nTemperature: %0.1f F" % (bme280.temperature*1.8+32))
    f.write("\nHumidity: %0.1f %%" % bme280.humidity)
    f.write("\nPressure: %0.1f hPa" % bme280.pressure)
    f.write("\nAltitude = %0.2f meters" % bme280.altitude)
    print("\nTemperature: %0.1f F" % (bme280.temperature*1.8+32))
    print("Humidity: %0.1f %%" % bme280.humidity)
    print("Pressure: %0.1f hPa" % bme280.pressure)
    print("Altitude = %0.2f meters" % bme280.altitude)
    print (str(currentDT))
    led = digitalio.DigitalInOut(board.D18)
    led.direction = digitalio.Direction.OUTPUT
    led.value = True
    time.sleep(2)
    