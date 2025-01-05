import RPi.GPIO as GPIO
import time
import adafruit_dht
import board
import datetime

# GPIO pin definitions
DHT_PIN = 4  # DHT11 sensor GPIO pin
SOIL_SENSOR_PIN = 23  # Soil moisture sensor digital output pin
RELAY_CHANNELS = [17, 27, 22]  # Relay channels: Channel 1, 2, 3

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOIL_SENSOR_PIN, GPIO.IN)  # Soil moisture sensor as input
for pin in RELAY_CHANNELS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)  # Relay initially off (NC active)

# DHT11 sensor setup
dht_sensor = adafruit_dht.DHT11(board.D4)

def is_daytime():
    """
    Determine whether it is daytime or nighttime based on the current hour.
    Daytime: 8 AM to 8 PM
    Nighttime: 8 PM to 8 AM
    """
    current_hour = datetime.datetime.now().hour
    return 8 <= current_hour < 20

try:
    while True:
        # Read temperature and humidity from the DHT11 sensor
        try:
            temperature = dht_sensor.temperature
            humidity = dht_sensor.humidity
            print(f"Temperature: {temperature}°C, Humidity: {humidity}%")
        except RuntimeError as e:
            print(f"Error reading DHT11: {e}")
            time.sleep(2)
            continue

        # Read soil moisture sensor data
        soil_status = GPIO.input(SOIL_SENSOR_PIN)  # 0 = Dry, 1 = Wet
        print(f"Soil Status: {'Dry' if soil_status == 0 else 'Wet'}")

        # Determine the ideal temperature range based on daytime or nighttime
        if is_daytime():
            ideal_temp_min = 20
            ideal_temp_max = 30
        else:
            ideal_temp_min = 15
            ideal_temp_max = 20

        # Temperature control (Channel 1)
        if ideal_temp_min <= temperature <= ideal_temp_max:
            print("Temperature is ideal. Activating WHITE LED on Channel 1.")
            GPIO.output(RELAY_CHANNELS[0], GPIO.LOW)  # White LED on
        else:
            print("Temperature out of range. Activating RED LED on Channel 1.")
            GPIO.output(RELAY_CHANNELS[0], GPIO.HIGH)  # Red LED on

        # Humidity control (Channel 2)
        if 50 <= humidity <= 70:  # Ideal humidity
            print("Humidity is ideal. Activating WHITE LED on Channel 2.")
            GPIO.output(RELAY_CHANNELS[1], GPIO.LOW)  # White LED on
        else:
            print("Humidity out of range. Activating RED LED on Channel 2.")
            GPIO.output(RELAY_CHANNELS[1], GPIO.HIGH)  # Red LED on

        # Soil moisture control (Channel 3)
        if soil_status == 1:  # Wet soil
            print("Soil is wet. Activating WHITE LED on Channel 3.")
            GPIO.output(RELAY_CHANNELS[2], GPIO.LOW)  # White LED on
        else:  # Dry soil
            print("Soil is dry. Activating RED LED on Channel 3.")
            GPIO.output(RELAY_CHANNELS[2], GPIO.HIGH)  # Red LED on

        time.sleep(2)  # Wait before the next measurement

except KeyboardInterrupt:
    print("Program interrupted by user.")
finally:
    GPIO.cleanup()  # Clean up GPIO pins
