#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    #print all the moves here
    position = [0,0]
    mid = n//2
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                position = [i,j]
                break

    if position[0] > mid:
        for i in range(mid,position[0],1):
            print("RIGHT")
    else:
        for i in range(mid,position[0],-1):
            print("LEFT")

    if position[1] > mid:
        for i in range(mid,position[1],1):
            print("DOWN")
    else:
        for i in range(mid,position[1],-1):
            print("UP")

# m = int(input())
# grid = [] 
# for i in range(0, m): 
#     grid.append(input().strip())

m = 3
grid = [
    "p--",
    "-m-",
    "---"]

displayPathtoPrincess(m,grid)