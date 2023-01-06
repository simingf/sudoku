import copy 

# starting_board = [[0, 0, 0, 0, 0, 0, 0, 0, 8],
#                   [0, 2, 0, 0, 5, 0, 7, 6, 0],
#                   [0, 6, 0, 0, 0, 0, 0, 0, 3],
#                   [5, 0, 0, 0, 0, 0, 2, 0, 7],
#                   [0, 3, 0, 0, 1, 0, 0, 0, 0],
#                   [2, 0, 0, 4, 0, 0, 0, 3, 0],
#                   [0, 0, 0, 6, 0, 0, 0, 0, 0],
#                   [8, 0, 0, 0, 0, 0, 0, 0, 0],
#                   [1, 0, 0, 2, 7, 0, 0, 4, 0]]

starting_board = [[0,0,6,0,4,0,0,9,7],
                    [0,4,0,7,3,0,0,1,0],
                    [0,1,7,0,9,2,0,3,0],
                    [6,0,0,0,7,0,0,8,0],
                    [1,0,5,0,6,0,9,0,3],
                    [0,2,0,0,1,0,0,0,6],
                    [0,5,0,9,8,0,1,6,0],
                    [0,9,0,0,5,6,0,7,0],
                    [8,6,0,0,2,0,3,0,0]]

def check_board(board):
    """Checks if a sudoku board state is valid"""
    return check_rows(board) and check_columns(board) and check_squares(board)


def check_rows(board):
    """Checks if a sudoku board rows are valid"""
    for i in range(9):
        if not check_row(board, i):
            return False
    return True


def check_row(board, row):
    """Checks if a sudoku board row is valid"""
    nums = set({})
    for i in range(9):
        cur = board[row][i]
        if cur == 0:
            continue
        if cur in nums:
            return False
        else:
            nums.add(board[row][i])
    return True


def check_columns(board):
    """Checks if a sudoku board columns are valid"""
    for i in range(9):
        if not check_column(board, i):
            return False
    return True


def check_column(board, column):
    """Checks if a sudoku board column is valid"""
    nums = set({})
    for i in range(9):
        cur = board[i][column]
        if cur == 0:
            continue
        if cur in nums:
            return False
        else:
            nums.add(board[i][column])
    return True


def check_squares(board):
    """Checks if a sudoku board squares are valid"""
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not check_square(board, i, j):
                return False
    return True


def check_square(board, row, column):
    """Checks if a sudoku board square is valid"""
    nums = set({})
    row = row - row % 3
    column = column - column % 3
    for i in range(3):
        for j in range(3):
            cur = board[row + i][column + j]
            if cur == 0:
                continue
            if cur in nums:
                return False
            else:
                nums.add(board[row + i][column + j])
    return True

def solve(board):
    """Solves a sudoku board"""
    pass

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

def backtrack():
    """Backtracks a sudoku board aka the lil bit inefficient way"""
    
    working = copy.deepcopy(starting_board)
    i = 0
    j = 0
    forward = True
    
    while i < 9 and j < 9:
        print(i, j)
        if (i<0 or j<0):
            break
        if starting_board[i][j] == 0: # if the tile is editable
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
    return working
    
def print_board(board):
    """Prints a board"""
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()
    print("---------------------")

if __name__ == "__main__":
    solution = backtrack()
    print_board(solution)