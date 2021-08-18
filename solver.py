from settings import *
import pygame

# Solution funcion using recursion and backtracking 
def solve(board):
    print(board)
    empty = empty_pos(board)
    # Base case: Full board
    if not empty:
        return True
    # Sets row, col to empty row and column position given by empty_pos
    else: row, col = empty
    
    # Iterate from 0-9, sending paramaters to the is_valid function
    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            # If board is solved at any iteration, return True
            if solve(board):
                return True
            
            # Backtrack by setting the previous position back to an empty slot (0)
            board[row][col] = 0
    
    # Returns False if board is unsolvable
    return False

def is_valid(board, num, pos): # board = board array, num = attempted number, pos = current row and column 
    
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i]  == num and pos[1] != i:
            return False

    # Check col
    for i in range(len(board)):
        if board[i][pos[1]]  == num and pos[0] != i:
            return False

    # Check quadrants([0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,1], [2,2], [2,3])
    row_pos = pos[1] // 3
    col_pos = pos[0] // 3

    for i in range(col_pos*3, col_pos*3 + 3): # from quadrant [x,0] -> [x,2]
        for j in range(row_pos*3, row_pos*3 + 3): # from quadrant [0,x] -> [2,x]
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

def print_board(board):
    
    # nice formatting for board
    for i in range(len(board)):
        if i % 3 == 0:
            print("- - - - - - - - - - - - - - - - -")    

        for j in range(len(board[0])):
            if j == 0:
                print("| ", end="")

            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8: # last element of row, creates new line
                print(str(board[i][j]), "|")
            else:
                print(str(board[i][j]), " ", end="")
                
    print("- - - - - - - - - - - - - - - - -")


def empty_pos(board):
    for i in range(len(board)): # num of rows
        for j in range(len(board[0])): # num of cols
            if board[i][j] == 0: # check if empty
                return (i, j) # row, col
    return None # completed board

solve(board)
