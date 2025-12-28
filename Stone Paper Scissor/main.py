#!/usr/bin/env python3

"""Tic Tac Toe Game
A simple command-line tic tac toe game for two players.
"""
def print_board(board):
    """Display the current game board."""
    print("\n")
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i + 1]} | {board[i + 2]} ")
        if i < 6:
            print("-----------")
    print("\n")
def check_winner(board, player):
    """Check if the given player has won."""
    # Winning combinations
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]

    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False


def is_board_full(board):
    """Check if the board is full (tie game)."""
    return all(cell in ['X', 'O'] for cell in board)


def get_player_move(board, player):
    """Get a valid move from the current player."""
    while True:
        try:
            move = input(f"Player {player}, enter your move (1-9): ")
            move = int(move) - 1

            if move < 0 or move > 8:
                print("Invalid input! Please enter a number between 1 and 9.")
                continue

            if board[move] in ['X', 'O']:
                print("That position is already taken! Choose another.")
                continue

            return move
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")
        except (KeyboardInterrupt, EOFError):
            print("\nGame interrupted. Exiting...")
            exit(0)


def play_game():
    """Main game loop."""
    # Initialize board with position numbers
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    current_player = 'X'

    print("=" * 40)
    print("Welcome to Tic Tac Toe!")
    print("=" * 40)
    print("Positions are numbered 1-9:")
    print_board(board)

    while True:
        # Get player move
        move = get_player_move(board, current_player)
        board[move] = current_player

        # Display updated board
        print_board(board)

        # Check for winner
        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins! 🎉")
            break

        # Check for tie
        if is_board_full(board):
            print("It's a tie! Well played both!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

    # Ask to play again
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again == 'y':
        play_game()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    play_game()
