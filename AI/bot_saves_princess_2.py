#

def nextMove(n,r,c,grid):

    position = []
    for i in range(0,n):
        for j in range(0,n):
            if grid[i][j] == 'p':
                position = [i,j]
                break
    
    if position[0] == r:
        if position[1] < c:
            return "LEFT"
        else:
            return "RIGHT"
    
    else:
        if position[0] < r:
            return "UP"
        else:
            return "DOWN"
    



# n = int(input())
# r,c = [int(i) for i in input().strip().split()]


n = 5
r , c = 2 , 3
X = [
    "-----",
    "-----",
    "p--m-",
    "-----",
    "-----"
    ]

grid = []
for i in range(0, n):
    grid.append(X[i])

print(nextMove(n,r,c,grid))

