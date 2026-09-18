import random
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x450")
root.configure(bg="#f0f0f0")

user_score = 0
computer_score = 0
choices = ["Rock", "Paper", "Scissors"]


def play(user_choice):
    global user_score, computer_score

    comp_choice = random.choice(choices)

    if user_choice == comp_choice:
        result_text = f"It's a Tie!\nBoth chose {user_choice}."
    elif (
        (user_choice == "Rock" and comp_choice == "Scissors")
        or (user_choice == "Paper" and comp_choice == "Rock")
        or (user_choice == "Scissors" and comp_choice == "Paper")
    ):
        user_score += 1
        result_text = f"You Win!\n{user_choice} beats {comp_choice}."
    else:
        computer_score += 1
        result_text = f"Computer Wins!\n{comp_choice} beats {user_choice}."

    result_label.config(text=result_text)
    score_label.config(
        text=f"Score - You: {user_score}  |  Computer: {computer_score}"
    )


def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="Score - You: 0  |  Computer: 0")
    result_label.config(text="Choose Rock, Paper, or Scissors to start!")


title_label = tk.Label(
    root,
    text="Rock Paper Scissors",
    font=("Helvetica", 18, "bold"),
    bg="#f0f0f0",
)
title_label.pack(pady=15)

score_label = tk.Label(
    root,
    text="Score - You: 0  |  Computer: 0",
    font=("Helvetica", 12),
    bg="#f0f0f0",
)
score_label.pack(pady=5)

result_label = tk.Label(
    root,
    text="Choose Rock, Paper, or Scissors to start!",
    font=("Helvetica", 12, "italic"),
    bg="#f0f0f0",
    fg="#333333",
)
result_label.pack(pady=20)

btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

rock_btn = tk.Button(
    btn_frame,
    text="Rock 🪨",
    font=("Helvetica", 12),
    width=10,
    command=lambda: play("Rock"),
)
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(
    btn_frame,
    text="Paper 📄",
    font=("Helvetica", 12),
    width=10,
    command=lambda: play("Paper"),
)
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(
    btn_frame,
    text="Scissors ✂️",
    font=("Helvetica", 12),
    width=10,
    command=lambda: play("Scissors"),
)
scissors_btn.grid(row=0, column=2, padx=5)

reset_btn = tk.Button(
    root,
    text="Reset Game",
    font=("Helvetica", 10),
    bg="#ff4d4d",
    fg="white",
    command=reset_game,
)
reset_btn.pack(pady=20)

root.mainloop()
