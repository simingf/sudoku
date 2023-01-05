solution = [[9, 5, 3, 1, 6, 7, 4, 2, 8],
            [4, 2, 8, 3, 5, 9, 7, 6, 1],
            [7, 6, 1, 8, 2, 4, 9, 5, 3],
            [5, 8, 4, 9, 3, 6, 2, 1, 7],
            [6, 3, 9, 7, 1, 2, 5, 8, 4],
            [2, 1, 7, 4, 8, 5, 6, 3, 9],
            [3, 4, 5, 6, 9, 1, 8, 7, 2],
            [8, 7, 2, 5, 4, 3, 1, 9, 6],
            [1, 9, 6, 2, 7, 8, 3, 4, 5]]

board = [[0, 0, 0, 0, 0, 0, 0, 0, 8],
         [0, 2, 0, 0, 5, 0, 7, 6, 0],
         [0, 6, 0, 0, 0, 0, 0, 0, 3],
         [5, 0, 0, 0, 0, 0, 2, 0, 7],
         [0, 3, 0, 0, 1, 0, 0, 0, 0],
         [2, 0, 0, 4, 0, 0, 0, 3, 0],
         [0, 0, 0, 6, 0, 0, 0, 0, 0],
         [8, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 2, 7, 0, 0, 4, 0]]

nums = set({})


def solve(board):
    """Solves a sudoku board"""
    pass


def check_square(board, row, column):
    """Checks if a sudoku board square is valid"""
    return check_row(board, row) and check_column(board, column) and check_square(board, row, column)


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
    nums.clear()
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
    nums.clear()
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
    nums.clear()
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


if __name__ == "__main__":
    print(check(board))
    print(check(solution))
