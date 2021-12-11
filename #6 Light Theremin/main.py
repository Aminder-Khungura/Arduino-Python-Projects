import pyfirmata
import time

board = pyfirmata.Arduino('COM3')  # Set the connection with the Arduino board
it = pyfirmata.util.Iterator(board)  # Assigns an iterator used to read the status of the inputs
it.start()  # starts iterator, which keeps a loop running in parallel with your main code

analog_input = board.get_pin('a:0:i')  # Set pins as analog inputs

pwm_output = board.get_pin('d:9:p')  # Define pin as a digital pwm


while True:
    analog_value = analog_input.read()
    print(analog_value)
    pwm_output.write(analog_value)
    time.sleep(0.5)
