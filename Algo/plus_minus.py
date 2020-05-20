#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    s = [0,0,0]

    s[0] = float(sum([1 for i in arr if i > 0])/len(arr))
    s[1] = float(sum([1 for i in arr if i < 0])/len(arr))
    s[2] = float(sum([1 for i in arr if i == 0])/len(arr))

    print("{:.6f}\n{:.6f}\n{:.6f}".format(s[0] , s[1] ,s[2]))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)