import serial
import time

WAIT_TIME = 0.4


def open_arduino(char_lst):
    ser = serial.Serial('COM6', 9600)  # opens communication with arduino
    time.sleep(2)

    for char in char_lst:
        ser.flush()
        ser.write(char.encode())
        time.sleep(WAIT_TIME)
    ser.close()
    exit()


if __name__ == '__main__':
    char_lst = ['a', 'b', 'c', 'd','e','f','g','h']
    open_arduino(char_lst)
