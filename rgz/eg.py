import PySimpleGUI as sg
import random

# Initialize the game board
def initialize_board():
    return [["" for _ in range(3)] for _ in range(3)]

# Check for a winner or a draw
def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    # Check for draw
    if all(cell != "" for row in board for cell in row):
        return "Draw"
    return None

# Update results file
def append_result(result):
    with open("tic_tac_toe_results.txt", "a") as file:
        file.write(result + "\n")

# Get all available moves
def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]

# Minimax algorithm for optimal AI move
def minimax(board, is_maximizing): # true if current turn is AI's, false if turn is player's
    # base case - function immediately returns a score based on the outcome
    winner = check_winner(board)
    if winner == "X":  # Player wins
        return -1
    elif winner == "O":  # AI wins
        return 1
    elif winner == "Draw":  # Draw
        return 0

    # if check_winner returns None
    if is_maximizing:
        best_score = float("-inf") # The AI starts with the worst possible score, -∞.
        # simulate all possible moves for AI using recursion, choose the move that has the highest chance of winning
        for move in get_available_moves(board): 
            board[move[0]][move[1]] = "O" # place "O" in an empty cell
            score = minimax(board, False) # recursively call minimax for opponent's turn (passing False)
            board[move[0]][move[1]] = ""
            best_score = max(best_score, score) # best score out of all recursive scores
        return best_score
    else: # player's turn
        best_score = float("inf") # starts with best possible score
        # choose the move that minimizes the player's chances of losing (chances of AI winning)
        for move in get_available_moves(board):
            board[move[0]][move[1]] = "X" 
            score = minimax(board, True) # rec call, next turn is AI's
            board[move[0]][move[1]] = ""
            best_score = min(best_score, score) # chooses the least possible score out of all the moves
        return best_score

# Get the best move for AI
def get_best_move(board):
    best_score = float("-inf")
    best_move = None
    # calculate highest "score" out of each move with minimax
    for move in get_available_moves(board):
        board[move[0]][move[1]] = "O"
        score = minimax(board, False)
        board[move[0]][move[1]] = ""
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

# Create PySimpleGUI layout
def create_layout():
    layout = [
        [sg.Button("", size=(6, 3), key=(i, j), pad=(5, 5)) for j in range(3)]
        for i in range(3)
    ]
    layout.append([sg.Text("", size=(30, 1), key="-STATUS-", justification="center")])
    layout.append([sg.Button("Restart", size=(10, 1)), sg.Button("Exit", size=(10, 1))])
    return layout

# Main game loop
def main():
    sg.theme("LightBlue")
    board = initialize_board()
    layout = create_layout()
    window = sg.Window("Tic Tac Toe", layout)

    current_player = "X"  # Player always starts as "X"

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break
        if event == "Restart":
            # Reset the board and GUI
            board = initialize_board()
            current_player = "X"
            for i in range(3):
                for j in range(3):
                    window[(i, j)].update("", disabled=False)
            window["-STATUS-"].update("Player X's turn")
            continue
        if isinstance(event, tuple) and board[event[0]][event[1]] == "" and current_player == "X":
            # Player move
            board[event[0]][event[1]] = "X"
            window[event].update("X")
            # Check if player wins or game ends
            winner = check_winner(board)
            if winner:
                if winner == "Draw":
                    window["-STATUS-"].update("It's a draw!")
                    append_result("Draw")
                else:
                    window["-STATUS-"].update(f"Player {winner} wins!")
                    append_result(f"Player {winner} wins")
                # Disable all buttons after game ends
                for i in range(3):
                    for j in range(3):
                        window[(i, j)].update(disabled=True)
                continue
            # AI move
            ai_move = get_best_move(board)
            if ai_move:
                board[ai_move[0]][ai_move[1]] = "O"
                window[ai_move].update("O")
            # Check if AI wins or game ends
            winner = check_winner(board)
            if winner:
                if winner == "Draw":
                    window["-STATUS-"].update("It's a draw!")
                    append_result("Draw")
                else:
                    window["-STATUS-"].update(f"Player {winner} wins!")
                    append_result(f"Player {winner} wins")
                # Disable all buttons after game ends
                for i in range(3):
                    for j in range(3):
                        window[(i, j)].update(disabled=True)
                continue
            # Switch turn back to player
            window["-STATUS-"].update("Player X's turn")
    window.close()

if __name__ == "__main__":
    main()
