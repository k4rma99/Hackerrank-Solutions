#!/bin/python3

import math
import os
import random
import re
import sys


def bitwise(n,k):
    max_val = 0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            val = i & j
            if max_val < val < k:
                max_val = val
                if max_val == k-1:
                    return max_val
    return max_val

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        print(bitwise(n,k))
