import pyfirmata
import time

board = pyfirmata.Arduino('COM3')  # Set the connection with the Arduino board
it = pyfirmata.util.Iterator(board)  # Assigns an iterator used to read the status of the inputs
it.start()  # starts iterator, which keeps a loop running in parallel with your main code

digital_input = board.get_pin('d:2:i')  # Set pin 2 as a digital input, the default is to use digital pins as outputs
digital_output = board.get_pin('d:9:o')  # Define pin 9 as a digital output

while True:
    switchState = digital_input.read()

    if switchState is True:
        digital_output.write(1)  # Digital pin 3 is turned on
    else:
        digital_output.write(0)  # Digital pin 3 is turned off
        time.sleep(0.25)