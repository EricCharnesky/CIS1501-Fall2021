def print_board(board):
    for row in board:
        print(row)


def tie(board):
    for row in board:
        if " " in row:
            return False
    return True


def win_by_diagonal_up(board):
    for row_index in range(3, 6):
        for column_index in range(4):
            if board[row_index][column_index] != " " and \
                    board[row_index][column_index] == board[row_index - 1][column_index + 1] and \
                    board[row_index][column_index] == board[row_index - 2][column_index + 2] and \
                    board[row_index][column_index] == board[row_index - 3][column_index + 3]:
                return True
    return False


def win_by_diagonal_down(board):
    for row_index in range(0, 3):
        for column_index in range(4):
            if board[row_index][column_index] != " " and \
                    board[row_index][column_index] == board[row_index + 1][column_index + 1] and \
                    board[row_index][column_index] == board[row_index + 2][column_index + 2] and \
                    board[row_index][column_index] == board[row_index + 3][column_index + 3]:
                return True
    return False


def win_by_diagonal(board):
    return win_by_diagonal_up(board) or win_by_diagonal_down(board)


def win_by_column(board):
    for column_index in range(7):
        for row_index in range(3):
            if board[row_index][column_index] != " " \
                    and board[row_index][column_index] == board[row_index + 1][column_index] \
                    and board[row_index][column_index] == board[row_index + 2][column_index] \
                    and board[row_index][column_index] == board[row_index + 3][column_index]:
                return True
    return False


def win_by_row(board):
    for row in board:
        for column_index in range(4):
            if row[column_index] != " " and \
                    row[column_index] == row[column_index + 1] and \
                    row[column_index] == row[column_index + 2] and \
                    row[column_index] == row[column_index + 3]:
                return True
    return False


def player_won(board):
    return win_by_row(board) or win_by_column(board) or win_by_diagonal(board)


def game_over(board):
    return tie(board) or player_won(board)


def drop_piece_in_column(board, column_index, whose_turn):
    for row_index in range(5, -1, -1):
        if board[row_index][column_index] == " ":
            board[row_index][column_index] = whose_turn
            break


board = []

for row in range(6):
    board.append([])
    for column in range(7):
        board[row].append(" ")

whose_turn = "X"

while not game_over(board):
    print_board(board)

    print(f"it's {whose_turn}'s turn!")

    col = input("Enter the column to drop your piece (0-6)")
    while board[0][int(col)] != " ":
        print("You can't go there!")
        col = input("Enter the column to drop your piece (0-6)")
    drop_piece_in_column(board, int(col), whose_turn)

    whose_turn = "X" if whose_turn == 'O' else 'O'

print_board(board)
print("game over!")