import os
import pathlib

import cv2
import numpy as np
from PIL import Image



# def char_to_bin(c):
#     return "{:08b}".format(ord(c))
#
#
# def str_to_bin(str):
#     arr = []
#     for c in str:
#         arr.append(char_to_bin(c))
#         # arr.append(char_to_bin(c)[0:2])
#         # arr.append(char_to_bin(c)[2:4])
#         # arr.append(char_to_bin(c)[4:6])
#         # arr.append(char_to_bin(c)[6:7]+"0")
#     return arr
from PIL.Image import Image


def file_to_bin(file_name):
    inp = open(file_name, 'r')
    # lines_bin = []
    # lines_bin += str_to_bin(inp.read())
    lst = [c for c in inp.read()]
    lst.append(bin_to_char("0000000"))
    return lst


def bin_to_char(bin):
    return chr(int(bin, 2))


def num_to_bin(n):
    return "{:08b}".format(n)

def bin_to_num(bin):
    return int(bin, 2)

def bmp_to_bin(file_name):
    bmp = open(file_name, 'rb')

    # lines_bin = []
    # lines_bin += str_to_bin(inp.read())
    data = bmp.read()
    print(data)
    str = ""
    for n in data:
        # print(n)
        # print(num_to_bin(n))
        str += num_to_bin(n)
    splited = []
    for i in range(int(len(str)/7)+1):
        splited.append(str[7*i:7*(i+1)])
    while len(splited[-1]) < 7:
        splited[-1] += "0"
    # print(splited)
    chars = []
    for bin in splited:
        chars.append(bin_to_char(bin))
    return chars
    # return splited

def decoder(arr):
    str = "***\n"
    for bin in arr:
        str += bin_to_char(bin)
    return str + "\n***"

def decoder_bmp(arr):
    unite_arr = ""
    for bin in arr:
        unite_arr += bin
    # unite_arr = unite_arr[:8*16**2]
    print(unite_arr)
    splited = []
    for i in range(int(len(unite_arr)/8)):
        splited.append(unite_arr[8*i:8*(i+1)])

    print(splited)
    data = []
    for s in splited:
        data.append(bin_to_num(s))
    print(data)

    bmp_out = open("out.bmp", 'wb')
    bmp_out.write(bytes(data))


def coder():
    path = pathlib.Path().absolute()
    files = os.listdir(path)
    for f in files:
        if '.txt' in f:
            return file_to_bin(f)
        if '.bmp' in f:
            return bmp_to_bin(f)

arr = coder()
print(arr)
print(decoder_bmp(arr))