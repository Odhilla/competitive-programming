from valid_sudoku import is_valid_sudoku

VALID = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


def test_valid_board():
    assert is_valid_sudoku(VALID) is True


def test_duplicate_in_row():
    board = [row[:] for row in VALID]
    board[0][2] = "5"  # second 5 in row 0
    assert is_valid_sudoku(board) is False
