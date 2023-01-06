import copy
from boards import *
from checks import check_starting_board, check_solved_board

def get_possible_nums(board, row, column):
    """Gets the possible numbers for a tile"""
    valid = []
    for num in range(1,10):
        flag = 1

        # check row
        for i in range(9):
            if (board[i][column]) == num:
                flag = 0
                break

        # check column
        for i in range(9):
            if (board[row][i]) == num:
                flag = 0
                break

        # check square
        base_row = row - row % 3
        base_column = column - column % 3
        for i in range(3):
            for j in range(3):
                if (board[base_row + i][base_column + j]) == num:
                    flag = 0
                    break

        # add to list
        if flag:
            valid.append(num)

    return valid

def backtrack(board):
    """Backtracks a sudoku board aka the lil bit inefficient way"""
    
    if (check_starting_board(board)):
        print("starting board is valid")
    else:
        print("starting board is invalid")
        raise Exception("starting board is invalid")

    working = copy.deepcopy(board)
    i = 0
    j = 0
    forward = True
    
    while 0 <= i <= 8 and 0 <= j <= 8:
        if board[i][j] == 0: # if the tile is editable
            cur = working[i][j]
            nums = [n for n in get_possible_nums(working, i, j) if n > cur]
            if len(nums) == 0: # something went wrong, so backtrack
                forward = False
                working[i][j] = 0
            else:
                working[i][j] = nums[0]
                forward = True
        if forward:
            if j == 8:
                i += 1
                j = 0
            else:
                j += 1
        else:
            if j == 0:
                i -= 1
                j = 8
            else:
                j -= 1
    
    if (check_solved_board(working)):
        print("solution found")
        return working
    else:
        print("no solution found")
        raise Exception("no solution found")
    
def print_board(board):
    """Prints a board"""
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()
    print("---------------------")

if __name__ == "__main__":
    backtrack(board_easy)