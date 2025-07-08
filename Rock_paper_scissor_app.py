import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice):
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    
    result = ""
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = "You Win!"
    else:
        result = "Computer Wins!"
    
    result_label.config(text=f"Your Choice: {user_choice}\nComputer's Choice: {computer_choice}\n{result}")

# Individual functions for each button
def choose_rock():
    determine_winner('rock')

def choose_paper():
    determine_winner('paper')

def choose_scissors():
    determine_winner('scissors')

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissor App")
root.geometry("400x400")

# Heading
heading = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16))
heading.pack(pady=10)

# Buttons for user choice
rock_btn = tk.Button(root, text="Rock", width=20, command=choose_rock)
rock_btn.pack(pady=5)

paper_btn = tk.Button(root, text="Paper", width=20, command=choose_paper)
paper_btn.pack(pady=5)

scissors_btn = tk.Button(root, text="Scissors", width=20, command=choose_scissors)
scissors_btn.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=20)

# Start the GUI event loop
root.mainloop()

