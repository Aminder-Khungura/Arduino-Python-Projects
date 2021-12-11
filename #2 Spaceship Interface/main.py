import pyfirmata
import time

board = pyfirmata.Arduino('COM3')  # Set the connection with the Arduino board
it = pyfirmata.util.Iterator(board)  # Assigns an iterator used to read the status of the inputs
it.start()  # starts iterator, which keeps a loop running in parallel with your main code

digital_input = board.get_pin('d:2:i')  # Set pin 2 as a digital input, the default is to use digital pins as outputs
green_led = board.get_pin('d:3:o')  # Define pin 3 as a digital output aka green led
first_red_led = board.get_pin('d:4:o')  # Define pin 4 as a digital output aka red led
second_red_led = board.get_pin('d:5:o')  # Define pin 5 as a digital output aka red led

# you use board.get_pin()
# The type of the pin (a for analog or d for digital)
# The number of the pin
# The mode of the pin (i for input or o for output)

while True:
    switchState = digital_input.read()

    if switchState is True:
        green_led.write(0)  # Digital pin 3 is turned off
        first_red_led.write(1)  # Digital pin 4 is turned on
        second_red_led.write(1)  # Digital pin 5 is turned on
    else:
        green_led.write(1)  # Digital pin 3 is turned on
        first_red_led.write(0)  # Digital pin 4 is turned off
        second_red_led.write(0)  # Digital pin 5 is turned off
        time.sleep(0.25)