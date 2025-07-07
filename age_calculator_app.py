import tkinter as tk
from datetime import date

def calculate_age():
    try:
        name = name_entry.get()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        
        birth_date = date(year, month, day)
        today = date.today()
        
        # Calculate age
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        result_label.config(text=f"Hello {name}! You are {age} years old.", fg="green")
    except ValueError:
        result_label.config(text="Please enter valid date values!", fg="red")

# Create main window
root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")

# Name label & entry
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Date label & entry
tk.Label(root, text="Date of Birth - Day:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
day_entry = tk.Entry(root)
day_entry.grid(row=1, column=1, padx=10, pady=10)

# Month label & entry
tk.Label(root, text="Month:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
month_entry = tk.Entry(root)
month_entry.grid(row=2, column=1, padx=10, pady=10)

# Year label & entry
tk.Label(root, text="Year:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
year_entry = tk.Entry(root)
year_entry.grid(row=3, column=1, padx=10, pady=10)

# Button to calculate age
calc_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calc_button.grid(row=4, column=0, columnspan=2, pady=20)

# Label to display result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
