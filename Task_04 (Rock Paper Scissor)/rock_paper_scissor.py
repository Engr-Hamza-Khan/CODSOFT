import tkinter as tk
from tkinter import ttk
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.comp_score = 0

        # Labels
        self.result_var = tk.StringVar()
        self.result_label = ttk.Label(master, textvariable=self.result_var)
        self.result_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.user_score_label = ttk.Label(master, text="Your Score: 0", font=('Arial', 12))
        self.user_score_label.grid(row=1, column=0, pady=5)

        self.comp_score_label = ttk.Label(master, text="Computer Score: 0", font=('Arial', 12))
        self.comp_score_label.grid(row=1, column=2, pady=5)

        # Buttons
        self.rock_button = ttk.Button(master, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.grid(row=2, column=0, padx=10, pady=10)

        self.paper_button = ttk.Button(master, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.grid(row=2, column=1, padx=10, pady=10)

        self.scissors_button = ttk.Button(master, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.grid(row=2, column=2, padx=10, pady=10)

        self.reset_button = ttk.Button(master, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=3, column=1, pady=10)

    def play(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        comp_choice = random.choice(choices)

        result = self.determine_winner(user_choice, comp_choice)

        self.result_var.set(f"Your choice: {user_choice.capitalize()}\nComputer's choice: {comp_choice.capitalize()}\nResult: {result}")

        if result == "You Win!":
            self.user_score += 1
        elif result == "You Lose!":
            self.comp_score += 1

        self.user_score_label.config(text=f"Your Score: {self.user_score}")
        self.comp_score_label.config(text=f"Computer Score: {self.comp_score}")

    def determine_winner(self, user_choice, comp_choice):
        if user_choice == comp_choice:
            return "It's a Tie!"
        elif (
            (user_choice == "rock" and comp_choice == "scissors") or
            (user_choice == "paper" and comp_choice == "rock") or
            (user_choice == "scissors" and comp_choice == "paper")
        ):
            return "You Win!"
        else:
            return "You Lose!"

    def reset_game(self):
        self.user_score = 0
        self.comp_score = 0
        self.user_score_label.config(text="Your Score: 0")
        self.comp_score_label.config(text="Computer Score: 0")
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
