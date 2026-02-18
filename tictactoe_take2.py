import tkinter as tk
from tkinter import messagebox

# Create main window
window = tk.Tk()
window.title("Tic-Tac-Toe")
window.resizable(False, False)

current_player = "X"
buttons = [""] * 9

# Check for winner
def check_winner():
    win_combinations = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in win_combinations:
        if buttons[a] == buttons[b] == buttons[c] != "":
            return buttons[a]

    if "" not in buttons:
        return "Draw"

    return None


# Button click function
def button_click(index):
    global current_player

    if buttons[index] == "":
        buttons[index] = current_player
        btn_list[index].config(text=current_player)

        winner = check_winner()
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            else:
                messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Reset game
def reset_game():
    global current_player, buttons
    current_player = "X"
    buttons = [""] * 9
    for btn in btn_list:
        btn.config(text="")

# Create buttons
btn_list = []

for i in range(9):
    btn = tk.Button(
        window,
        text="",
        font=("Arial", 24),
        width=6,
        height=2,
        command=lambda i=i: button_click(i)
    )
    btn.grid(row=i//3, column=i%3)
    btn_list.append(btn)

# Restart button
restart_button = tk.Button(
    window,
    text="Restart",
    font=("Arial", 12),
    command=reset_game
)
restart_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

window.update()
window_width= window.winfo_width()
window_height= window.winfo_height()
screen_width= window.winfo_screenwidth()
screen_height= window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()