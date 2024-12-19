import PySimpleGUI as sg

def initialize_board():
    return [["" for _ in range(3)] for _ in range(3)]


def check_winner(board):
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


def append_result(result):
    with open("tic_tac_toe_results.txt", "a") as file:
        file.write(result + "\n")


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
    board = initialize_board()
    current_player = "X"
    layout = create_layout()
    window = sg.Window("Tic Tac Toe", layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Exit":
            break
        if event == "Restart":
            board = initialize_board()
            current_player = "X"
            for i in range(3):
                for j in range(3):
                    window[(i, j)].update("", disabled=False)
            window["-STATUS-"].update("")
            continue
        else:
            # if cell is empty
            if board[event[0]][event[1]] == "":
                # Update board and button
                board[event[0]][event[1]] = current_player
                window[event].update(current_player)

                # Check game state
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
                else:
                    # Switch player
                    current_player = "O" if current_player == "X" else "X"
                    window["-STATUS-"].update(f"Player {current_player}'s turn")
    window.close()

if __name__ == "__main__":
    main()
