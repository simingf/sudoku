def check_starting_board(board):
    """Checks if a starting sudoku board state is valid"""
    return check_rows(board) and check_columns(board) and check_squares(board)


def check_solved_board(board):
    """Checks if a solved sudoku board state is valid"""
    return check_rows(board, True) and check_columns(board, True) and check_squares(board, True)


def check_rows(board, complete=False):
    """Checks if a sudoku board rows are valid"""
    for i in range(9):
        if not check_row(board, i, complete):
            return False
    return True


def check_row(board, row, complete=False):
    """Checks if a sudoku board row is valid"""
    nums = set({})
    for i in range(9):
        cur = board[row][i]
        if cur == 0 and complete:
            return False
        if cur == 0 and not complete:
            continue
        if cur in nums:
            return False
        nums.add(board[row][i])
    return True


def check_columns(board, complete=False):
    """Checks if a sudoku board columns are valid"""
    for i in range(9):
        if not check_column(board, i, complete):
            return False
    return True


def check_column(board, column, complete=False):
    """Checks if a sudoku board column is valid"""
    nums = set({})
    for i in range(9):
        cur = board[i][column]
        if cur == 0 and complete:
            return False
        if cur == 0 and not complete:
            continue
        if cur in nums:
            return False
        nums.add(board[i][column])
    return True


def check_squares(board, complete=False):
    """Checks if a sudoku board squares are valid"""
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not check_square(board, i, j, complete):
                return False
    return True


def check_square(board, row, column, complete=False):
    """Checks if a sudoku board square is valid"""
    nums = set({})
    row = row - row % 3
    column = column - column % 3
    for i in range(3):
        for j in range(3):
            cur = board[row + i][column + j]
            if cur == 0 and complete:
                return False
            if cur == 0 and not complete:
                continue
            if cur in nums:
                return False
            nums.add(board[row + i][column + j])
    return True