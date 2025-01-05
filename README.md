# Project Description
This project was developed to monitor the temperature and soil moisture levels of a plant cultivation environment using Raspberry Pi 4B and create a light panel to evaluate the environment based on these values. The project visualizes the condition of the environment with red, yellow, and white lights to ensure optimal plant growth conditions.

---

## Features
- **Temperature Monitoring**: Measures the ambient temperature using a DHT11 sensor.
- **Soil Moisture Monitoring**: Detects dry/wet conditions with a digital soil moisture sensor.
- **Visual Status Indicator**:
  - **Red Light**: Critical condition
  - **White Light**: Optimal conditions
- **Relay Control**: Controls the lights via a 4-channel relay module.

---

## Requirements

### Hardware
- Raspberry Pi 4B
- DHT11 temperature sensor
- Digital soil moisture sensor
- 4-channel relay module
- 5V lights (red, yellow, white)
- Breadboard and connecting wires

### Software
- Python 3
- Required Python libraries: `RPi.GPIO`, `Adafruit_DHT`

---

## Setup

### Connect the Hardware:
1. Connect the DHT11 sensor to the GPIO pins.
2. Attach the soil moisture sensor using digital output.
3. Connect the lights via the relay module for control.

### Install the Software:
1. Install the necessary Python libraries on Raspberry Pi:
   ```bash
   pip install Adafruit_DHT RPi.GPIO
2. Create your project folder and save your code under the name "raspberrypi_code.py".

### Usage
Run the Python file:
python3 project/raspberrypi_code.py

   
   
