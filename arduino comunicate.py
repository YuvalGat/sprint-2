import serial
import time
import coder

WAIT_TIME = 0.1


def open_arduino(char_lst):
    if len(char_lst) % 2 == 1:
        char_lst.append('\n')

    ser = serial.Serial('COM6', 9600)  # opens communication with arduino
    time.sleep(1.6)

    for char in char_lst:
        ser.flush()
        ser.write(char.encode())
        time.sleep(WAIT_TIME)
    ser.close()
    exit()


if __name__ == '__main__':
    char_lst = coder.coder()
    open_arduino(char_lst)
