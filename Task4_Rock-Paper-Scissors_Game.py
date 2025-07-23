import tkinter as tk
import random

# Initialize scores
player_score = 0
computer_score = 0

# Choices list
choices = ["Rock", "Paper", "Scissors"]

# Determine winner
def get_winner(player, computer):
    if player == computer:
        return "Draw"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "Player"
    else:
        return "Computer"

# Handle user move
def play(player_choice):
    global player_score, computer_score

    computer_choice = random.choice(choices)
    winner = get_winner(player_choice, computer_choice)

    if winner == "Player":
        player_score += 1
        result_text = "✅ You win!"
    elif winner == "Computer":
        computer_score += 1
        result_text = "❌ Computer wins!"
    else:
        result_text = "😐 It's a draw!"

    # Update labels
    player_label.config(text=f"You: {player_choice}")
    computer_label.config(text=f"Computer: {computer_choice}")
    result_label.config(text=result_text)
    score_label.config(text=f"The Score's - 🧑‍💼Your: {player_score} | 💻Computer: {computer_score}")

# Reset scores
def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    player_label.config(text="You:")
    computer_label.config(text="Computer:")
    result_label.config(text="")
    score_label.config(text="The Score's - 🧑‍💼Your: 0 | 💻Computer: 0")

# Create GUI window
window = tk.Tk()
window.title("Rock Paper Scissors - By Tanmay")
window.geometry("450x400")
window.config(bg="#fcf810")

# Heading
title = tk.Label(window, text="Rock Paper Scissors", font=("Arial", 25, "bold"), bg="#d74c4c")
title.pack(pady=10)

# Labels
player_label = tk.Label(window, text="You:", font=("Arial", 16), bg="#3491dc")
player_label.pack()

computer_label = tk.Label(window, text="Computer:", font=("Arial", 16), bg="#27bfda")
computer_label.pack()

result_label = tk.Label(window, text="", font=("Arial", 20, "bold"), fg="green", bg="#fbff13")
result_label.pack(pady=10)

score_label = tk.Label(window, text="The Score's - 🧑‍💼Your: 0 | 💻Computer: 0", font=("Arial", 16), bg="#f07a47")
score_label.pack(pady=5)

# Buttons
button_frame = tk.Frame(window, bg="#3a7a2d")
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="🪨 Rock", width=14, command=lambda: play("Rock"))
paper_button = tk.Button(button_frame, text="📄 Paper", width=14, command=lambda: play("Paper"))
scissors_button = tk.Button(button_frame, text="✂️ Scissors", width=14, command=lambda: play("Scissors"))

rock_button.grid(row=0, column=0, padx=10, pady=5)
paper_button.grid(row=0, column=1, padx=10, pady=5)
scissors_button.grid(row=0, column=2, padx=10, pady=5)

# Reset button
reset_button = tk.Button(window, text="🔄 Reset Game", command=reset_game)
reset_button.pack(pady=10)

# Start the GUI loop
window.mainloop()
