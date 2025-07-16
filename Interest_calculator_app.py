import tkinter as tk

def calculate_interest():
    # Get values from entries
    try:
        p = float(principal_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())

        # Calculate interests
        si = (p * r * t) / 100
        ci = p * ((1 + r / 100) ** t - 1)

        # Display results
        result_label.config(text=f"Simple Interest: ₹{si:.2f}\nCompound Interest: ₹{ci:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# Create window
window = tk.Tk()
window.geometry("400x400")
window.title("Interest Calculator App")
window.configure(bg="#f0f0f0")  # Light background

# Labels and entry fields
tk.Label(window, text="Principal (₹):", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10, sticky="e")
principal_entry = tk.Entry(window)
principal_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Time (years):", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky="e")
time_entry = tk.Entry(window)
time_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(window, text="Rate (%):", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10, sticky="e")
rate_entry = tk.Entry(window)
rate_entry.grid(row=2, column=1, padx=10, pady=10)

# Button to calculate
calc_button = tk.Button(window, text="Calculate Interest", command=calculate_interest, bg="#4CAF50", fg="white")
calc_button.grid(row=3, columnspan=2, pady=20)

# Result label
result_label = tk.Label(window, text="", bg="#f0f0f0", font=("Arial", 12))
result_label.grid(row=4, columnspan=2)

# Run the application
window.mainloop()
