#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
    dirty_cells = []
    for i in range(5):
        for j in range(5):
            if board[j][i] == 'd':
                dirty_cells.append([j,i])

    if board[posr][posc] == "d":
        print("CLEAN")
        return None

    dist = float('inf')
    for a,b in dirty_cells:
        if abs(posr - a) + abs(posc - b) < dist:
            dist = abs(posr - a) + abs(posc - b)
            pos = [a,b]



    if pos[0] == posr:
        if pos[1] < posc:
            print("LEFT")
        else:
            print("RIGHT")
    
    else:
        if pos[0] < posr:
            print("UP")
        else:
            print("DOWN")

    return None

    # Tail starts here

if __name__ == "__main__":
    # pos = [int(i) for i in input().strip().split()]
    # board = [[j for j in input().strip()] for i in range(5)]
    pos = [0,0]
    board = [
            "b---d",
            "-d--d",
            "--dd-",
            "--d--",
            "----d"]
    next_move(pos[0], pos[1], board)