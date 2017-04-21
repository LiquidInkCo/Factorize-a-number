#!/usr/bin/env python
# coding=utf-8
import os
import re
import math
import shutil
import subprocess
import sys


def factors_of_number(start):
    var = float(float(start) / 2)
    h = int(round(var)) + 1

    for x in range(1,h):
       if (x == 1):
           a = 2

       q = float(start) / a
       a = a + 1

       i, d = divmod(q, 1)

       if d == 0:
           print(int(q))

    user_input()


def user_input():
   a = "Hello"
   try:
       a = int(input("Enter a number to be factorized (press enter to exit): "))
   except NameError:
        print("Not an integer value...")
        user_input()
   except:
    print("Have a nice day!")
    sys.exit()

   factors_of_number(a)


user_input()