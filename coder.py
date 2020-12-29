import os
import pathlib
import sys


def char_to_bin(c):
    return "{:08b}".format(ord(c))


def str_to_bin(str):
    arr = []
    for c in str:
        arr.append(char_to_bin(c))
    return arr


def file_to_bin(file_name):
    inp = open(file_name, 'r')
    lines_bin = []
    # for line in inp:
    #     lines_bin += str_to_bin(line)
    lines_bin += str_to_bin(inp.read())
    return lines_bin


def bin_to_char(bin):
    return chr(int(bin, 2))


def decoder(arr):
    str = "***\n"
    for bin in arr:
        str += bin_to_char(bin)
    return str + "\n***"


def coder():
    path = pathlib.Path().absolute()
    files = os.listdir(path)
    for f in files:
        if '.txt' in f:
            return file_to_bin(f)

arr = coder()
print(arr)
print(decoder(arr))
