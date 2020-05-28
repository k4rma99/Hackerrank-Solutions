

def next_move(posx, posy, dimx, dimy, board):
    dirty_cells = []
    pos = [0,0]
    for i in range(dimx):
        for j in range(dimy):
            if board[i][j] == 'd':
                dirty_cells.append([i,j])

    dist = float('inf')
    for a,b in dirty_cells:
        if abs(posx - a) + abs(posy - b) < dist:
            dist = abs(posx - a) + abs(posy - b)
            pos = [a,b]
    
    if pos[0] < posx:
        print('UP')
    elif pos[0] > posx:
        print('DOWN')
    elif pos[1] < posy:
        print('LEFT')
    elif pos[1]  > posy:
        print('RIGHT')
    else:
        print('CLEAN')
    
    return None


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)