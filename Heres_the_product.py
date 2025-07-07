import tkinter as tk

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_text.delete("1.0", tk.END)  # Clear previous result
        result_text.insert(tk.END, f"Product: {product:.2f}")
    except ValueError:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Please enter valid numbers!")

# Create main window
root = tk.Tk()
root.title("Getting Started with Widgets")
root.geometry("400x300")

# Label describing the functionality
desc_label = tk.Label(root, text="This app calculates the product of two numbers you enter.", font=("Arial", 10))
desc_label.pack(pady=10)

# Labels and entries for number inputs
label1 = tk.Label(root, text="Enter first number:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter second number:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

# Button to calculate product
calc_button = tk.Button(root, text="Calculate Product", command=calculate_product)
calc_button.pack(pady=10)

# Text box to display the result
result_text = tk.Text(root, height=2, width=30)
result_text.pack(pady=10)

root.mainloop()
