#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    return (sum(j * 2 ** i for (i,j) in enumerate(sorted(calorie , reverse = True),start = 0)))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())

    calorie = [1,3,2]

    
    #list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
