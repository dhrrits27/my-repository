import tkinter as tk

def check_strength():
    password = entry.get()
    length = len(password)
    if length <= 5:
        strength = "Weak"
        color = "red"
    elif 6 <= length <= 8:
        strength = "Medium"
        color = "yellow"
    elif 9 <= length <= 12:
        strength = "Strong"
        color = "light green"
    else:
        strength = "Very Strong"
        color = "dark green"
    result_label.config(text=strength, fg=color)

# Create main window
root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")

# Password entry
entry_label = tk.Label(root, text="Enter Password:")
entry_label.pack(pady=10)

entry = tk.Entry(root, show="*")
entry.pack(pady=10)

# Button to check password strength
check_button = tk.Button(root, text="Check Strength", command=check_strength)
check_button.pack(pady=10)

# Label to display the strength
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()
