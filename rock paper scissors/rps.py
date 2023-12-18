from tkinter import *
import random

player_score = 0
computer_score = 0
computer_moves = ["rock", "paper", "scissors"]
outcomes = {
    "rock": {"rock": 1, "paper": 0, "scissors": 2},
    "paper": {"rock": 2, "paper": 1, "scissors": 0},
    "scissors": {"rock": 0, "paper": 2, "scissors": 1}
}

#get random computer move
def get_computer_move():
    return computer_moves[random.randint(0, 2)]

#define the winner
def calculate_result(player_move):
    global computer_score
    global player_score
    computer_move = get_computer_move()
    player_move_label.config(text=f"You played: {player_move}")
    computer_move_label.config(text=f"Computer played: {computer_move}")

    winner = outcomes[player_move][computer_move]
    if winner == 0:
        computer_score += 2
        computer_score_label.config(text=f"Computer: {computer_score}")
        result_label.config(fg="red", text=f"You lost. Computer wins {2} points")
    elif winner == 1:
        result_label.config(fg="blue", text="It's a draw")
    else:
        player_score += 2
        player_score_label.config(text=f"You: {player_score}")
        result_label.config(fg="green", text=f"You won {2} points")

# Main UI
GUI = Tk()
GUI.title("Rock Paper Scissors")
rock_img=PhotoImage(file='rock paper scissors\\rock.PNG')
paper_img=PhotoImage(file='rock paper scissors\\papers.PNG')
scissors_img=PhotoImage(file='rock paper scissors\\scissors.PNG')

# Labels
Label(GUI, text="Rock Paper Scissors", font=("Velvetica", 22)).grid(row=0, sticky=N, padx=200, pady=20)
Label(GUI, text="Make your move", font=("Calibri", 20)).grid(row=2, sticky=N)
player_score_label = Label(GUI, text="You: 0", font=("Calibri", 15))
player_score_label.grid(row=5, sticky=W)
computer_score_label = Label(GUI, text="Computer: 0", font=("Calibri", 15))
computer_score_label.grid(row=5, sticky=E)
player_move_label = Label(GUI, font=("Calibri", 14))
player_move_label.grid(row=4, sticky=W)
computer_move_label = Label(GUI, font=("Calibri", 14))
computer_move_label.grid(row=4, sticky=E)
result_label = Label(GUI, font=("Calibri", 14))
result_label.grid(row=4, sticky=N)

# Buttons
Button(GUI, text="Rock",image=rock_img, width=200,height=180, command=lambda: calculate_result("rock"),cursor="hand2").grid(row=3, sticky=W, padx=5, pady=5)
Button(GUI, text="Paper",image=paper_img, width=200,height=180, command=lambda: calculate_result("paper"),cursor="hand2").grid(row=3, sticky=N, pady=5)
Button(GUI, text="Scissors",image=scissors_img,width=200, height=180,command=lambda: calculate_result("scissors"),cursor="hand2").grid(row=3, sticky=E, padx=5, pady=5)
Label(GUI).grid(row=6)

if __name__ == '__main__':
    GUI.mainloop()
