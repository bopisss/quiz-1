import tkinter

player1 = ":)"
player2 = ":("
current_player = player1

bgcolor = "#e4f1eb"

window = tkinter.Tk()
window.title("Tic Tac Toe ni Joachim")
window.resizable(False, False)
window.configure(bg=bgcolor)

frame = tkinter.Frame(window, bg=bgcolor)
frame.pack()

label = tkinter.Label(
    frame,
    text=current_player + "'s turn",
    font=("Arial", 20),
    bg=bgcolor,
    fg="black"
)

label.pack()

window.mainloop()
