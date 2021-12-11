import pyfirmata
import time

board = pyfirmata.Arduino('COM3')  # Set the connection with the Arduino board
it = pyfirmata.util.Iterator(board)  # Assigns an iterator used to read the status of the inputs
it.start()  # starts iterator, which keeps a loop running in parallel with your main code

analog_input = board.get_pin('a:0:i')  # Set pin as analog inputs

board.digital[9].mode = pyfirmata.SERVO  # Define component connected as SERVO


# def scale_analog_value(analog_value):
#     try:
#         angle = (179 - 0) * ((analog_value - 0) / (1023 - 0)) + 0
#     except TypeError:
#         angle = 0
#     return angle


while True:
    # analog_value = analog_input.read()
    # angle = scale_analog_value(analog_value)
    # print(analog_value, " ", angle)
    # try:
    #     board.digital[9].write(analog_value)
    # except TypeError:
    #     pass
    x = input("Enter: ")
    board.digital[9].write(x)
    time.sleep(15)