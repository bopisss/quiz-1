import tkinter

def set_tile(row, column):
    global current_player
    
    if game_over:
        return
    
    if board[row][column]["text"] != "":
        return
    
    board[row][column]["text"] = current_player
    
    if current_player ==player2:
        current_player = player1
    else:
        current_player = player2
        
    label["text"]= current_player+"'s turn"
    
    check_winner()
    
def check_winner():
    global turn, game_over
    turn += 1
    
    
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" is the winner!", foreground=p1color)
            for column in range(3):
                board[row][column].config(foreground=p1color, background=p2color)
            game_over = True
            return
        
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+" is the winner!", foreground=p1color)
            for row in range(3):
                board[row][column].config(foreground=p1color, background=p2color)
            game_over = True
            return
        
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"]+" is the winner!", foreground=p1color)
        for i in range(3):
            board[i][i].config(foreground=p1color, background=p2color)
        game_over = True
        return
    
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"]+" is the winner!", foreground=p1color)
        board[0][2].config(foreground=p1color, background=p2color)
        board[1][1].config(foreground=p1color, background=p2color)
        board[2][0].config(foreground=p1color, background=p2color)
        game_over = True
        return
    
    if (turn == 9):
        game_over = True
        label.config(text="Tie!", foreground=p1color)
    
def new_game():
    global turn, game_over

    turn = 0
    game_over = False

    label.config(text=current_player+"'s turn", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=p1color, background=bgcolor)


player1= "将"
player2= "日"
current_player= player1
board= [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
    
bgcolor= '#9C720C'
p1color= "#FFFFFF"
p2color= "#573C0E"

turn = 0
game_over = False

window = tkinter.Tk()
window.title("Tic Tac Toe ni Joachim")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=current_player+"'s turn", font=("Arial", 20), bg=bgcolor,
                      foreground="white")

label.grid(row=0, column=0, columnspan=3, sticky="nsew")
frame.pack()

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Arial", 40, "bold"),
                                            bg=bgcolor, foreground=p1color, width=6, height=2,
                                            command=lambda row=row, column=column: set_tile(row, column))

        board[row][column].grid(row=row+1, column=column)
        
button = tkinter.Button(frame, text="reset", font=("Arial", 20, "bold"), bg=bgcolor,
                        foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="nsew")


window.update()
window_width= window.winfo_width()
window_height= window.winfo_height()
screen_width= window.winfo_screenwidth()
screen_height= window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()