import pyfirmata
import time

board = pyfirmata.Arduino('COM3')  # Set the connection with the Arduino board
it = pyfirmata.util.Iterator(board)  # Assigns an iterator used to read the status of the inputs
it.start()  # starts iterator, which keeps a loop running in parallel with your main code

first_analog_input = board.get_pin('a:0:i')  # Set pins as analog inputs
second_analog_input = board.get_pin('a:1:i')
third_analog_input = board.get_pin('a:2:i')

red_led = board.get_pin('d:9:p')  # Define 3 pins as a digital PWM aka 3 LEDs
blue_led = board.get_pin('d:10:p')
green_led = board.get_pin('d:11:p')

red_value = 0
blue_value = 0
green_value = 0

while True:
    first_analog_value = first_analog_input.read()
    time.sleep(5)
    second_analog_value = second_analog_input.read()
    time.sleep(5)
    third_analog_value = third_analog_input.read()
    time.sleep(5)

    # Convert the analog sensor reading from a value between 0-1023 to a value between 0-255
    try:
        red_value = first_analog_value / 4
        blue_value = second_analog_value / 4
        green_value = third_analog_value / 4
    except TypeError:
        pass

    # Call led.write() with analog_value as an argument. This is a value between 0 and 1, read from the analog input.
    red_led.write(red_value)
    blue_led.write(blue_value)
    green_led.write(green_value)
    time.sleep(0.1)
