#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    max_v = 0
    min_v = sum(arr)
    for _ in range(len(arr)):
        x = arr.pop(0)
        max_v = max(max_v,sum(arr))
        min_v = min(min_v,sum(arr))
        arr.append(x)
    
    print("{:d} {:d}".format(min_v,max_v))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
