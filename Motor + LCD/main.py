import serial
import sys
import time
arduino = serial.Serial('COM3', 9600, timeout=10)
string = 'hello'
arduino.write(string.encode())
arduino.close()
time.sleep(0.25)
