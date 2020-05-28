#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    x = set(ar)
    count = 0
    for i in x:
        s = ar.count(i)
        if s == 2:
            count += 1
        elif s%2 == 0:
            count += s//2
        else:
            if (s-1) == 2:
                count += 1
            elif (s-1)%2 == 0 and s!=1:
                count += s//2
    
    return (count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
