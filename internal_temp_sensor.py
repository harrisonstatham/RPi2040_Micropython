import machine
import utime

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / 65535

while True:
    reading = sensor_temp.read_u16() * conversion_factor

    # The temp sensor measures the internal VBE of a biased bipolar diode.
    # This temp sensor is connected to the 5th ADC channel.
    # Typical VBE = 0.706 V at 27 degrees C with a slope of -1.721 mV (0.001721) per degree.

    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    utime.sleep(2)