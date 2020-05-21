#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = 6
    names = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        print (emailID[-10::])
        if emailID[-10::] == "@gmail.com":
            names.append(firstName)
        print(names)

    
    for x in sorted(names):
        print(x)