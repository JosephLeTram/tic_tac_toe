# Create a game Tic Tac Toe that lets human player plays against an AI (Computer)
# Tạo một game Caro cho phép người chơi đấu với máy

# Import module random đế sử dụng hàm randint cho máy
import random

# Make necessary functions
# Tạo những hàm cần thiết


# Tạo hàm để vẽ cái bảng chơi caro
def drawboard(board):
    # This function prints out the board
    # "board" is a list of 10 strings represent the board (ignore index 0)
    # "Bảng" là tập hợp một list gồm 10 cái chuỗi để vẽ lên bảng
    # Sử dụng index dể truy cập và sử dụng vị trí của ô
    # Những hàm trong phần chơi game sẽ ghi X hoặc O bằng cách pass vô từng index của string
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# Tạo hàm hỏi người chơi chọn X hoặc O
def input_player_letter():
    # This function lets player choose which letter they want to be
    # Returns a list with the player's letter as the first item, and the computer's letter as the second
    letter = ''

    # Hàm while not sẽ liên tục hỏi đến khi nhập đúng ký tự
    while not (letter == 'X' or letter == 'O'):
        print("Do you want to be X or O?")

        # upper method sẽ viết hoa ký tự input từ player
        letter = input().upper()

    # the first element in the list is the player's letter
    # Nếu người chơi chọn X, máy tính sẽ là O và ngược lại
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first():
    # Randomly choose the player to go first.
    # Ngẫu nghiên chọn người đi trước
    if random. randint(0, 1) == 0:
        return 'computer'
    else:
        return "player"


def play_again():
    # This function returns True if the player wants to play again, otherwise
    # it returns False
    print("Do you want to play again? (Yes or No)")
    return input().lower().startswith("y")


def make_move(board, letter, move):
    board[move] = letter


def is_winner(bo, le):
    # Given a board and a player's letter, this function returns True if player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            # down the right side
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))    # diagonal


def get_board_copy(board):
    # This function is here for the times AI make some temporary modications without changing the original board.
    # Make a duplicate of the board and return it the duplicate.
    dup_board = []
    for i in board:
        dup_board.append(i)
    return dup_board


def is_space_free(board, move):
    # Return true if the passed move is free on the passed board
    return board[move] == " "


def get_player_move(board):
    # Lets the player type in their move.
    move = ""
    while move not in "1 2 3 4 5 6 7 8 9".split() or not is_space_free(board, int(move)):
        print("What is your next move? (1-9)")
        move = input()
    return int(move)


def choose_random_move_from_list(board, moves_list):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, computer_letter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computer_letter == "X":
        player_letter == "O"
    else:
        player_letter == "X"

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, 1):
            make_move(copy, player_letter, i)
            if is_winner(copy, player_letter):
                return i
    # Try to take the center, if it is free.
    if is_space_free(board, 5):
        return 5

    # Move on one of the sides.
    return choose_random_move_from_list(board, [2, 4, 6, 8])


def is_board_full(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


    # Game Code
while True:
    print("WELCOME TO JOSEPH'S TIC TAC TOE!\n")
    theBoard = [' '] * 10   #
    player_letter, computer_letter = input_player_letter()
    turn = who_goes_first()
    print("The " + turn + " will go first.")
    game_is_playing = True

    while game_is_playing:
        if turn == "player":
            # Player's turn.
            drawboard(theBoard)
            move = get_player_move(theBoard)
            make_move(theBoard, player_letter, move)

            if is_winner(theBoard, player_letter):
                drawboard(theBoard)
                print("You have won the game")
                game_is_playing = False
            else:
                if is_board_full(theBoard):
                    drawboard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    turn = "computer"
        else:
            # Computer's Turn
            move = get_computer_move(theBoard, computer_letter)
            make_move(theBoard, computer_letter, move)

            if is_winner(theBoard, computer_letter):
                drawboard(theBoard)
                print("The computer has beaten you!")
                game_is_playing = False
            else:
                if is_board_full(theBoard):
                    drawboard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    turn = "player"

    if not play_again():
        break
