import pyfirmata
import time

board = pyfirmata.Arduino('COM3')  # Set the connection with the Arduino board
it = pyfirmata.util.Iterator(board)  # Assigns an iterator used to read the status of the inputs
it.start()  # starts iterator, which keeps a loop running in parallel with your main code

analog_input = board.get_pin('a:0:i')  # Set pin 0 as a analog input
first_led = board.get_pin('d:2:o')  # Define 3 pins as a digital output aka 3 LEDs
second_led = board.get_pin('d:3:o')
third_led = board.get_pin('d:4:o')

baseline_temp = 17

while True:
    try:
        analog_value = analog_input.read()
        voltage = analog_value * 5
        temperature = (voltage - 0.5) * 100
        print('analog_value/Voltage/Temperature: ', analog_value, '/', voltage, '/', temperature)
    except TypeError:
        temperature = baseline_temp

    if temperature >= baseline_temp + 3:
        first_led.write(1)
        second_led.write(1)
        third_led.write(1)
    elif temperature >= baseline_temp + 2:
        first_led.write(1)
        second_led.write(1)
        third_led.write(0)
    elif temperature >= baseline_temp + 1:
        first_led.write(1)
        second_led.write(0)
        third_led.write(0)
    else:
        first_led.write(0)
        second_led.write(0)
        third_led.write(0)
    time.sleep(0.1)
