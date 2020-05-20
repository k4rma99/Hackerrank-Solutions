#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid):
    n = len(grid)
    
    x = [map(lambda x : ord(x[0]) <= ord(x) <= ord(x[-1]) , i[j]) for j in range(n) for i in grid]
    y = [list(map(lambda x : ord(x[0]) <= ord(x) <= ord(x[-1]), grid[j])) for j in range(n)]
    
    if all(x) and all(y):
        return "YES"
    else:
        return "NO"
    #print(grid[0])

    return y

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input())

    # for t_itr in range(t):
    #     n = int(input())

        grid = [
            ['e','b','a','c','d'],
            ['f','g','h','i','j'],
            ['o','l','m','k','n'],
            ['t','r','p','q','s'],
            ['x','y','w','u','v']
        ]

        # for _ in range(n):
        #     grid_item = input()
        #     grid.append(grid_item)

        result = gridChallenge(grid)
        print(result)
    #     fptr.write(result + '\n')

    # fptr.close()
