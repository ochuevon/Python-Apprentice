"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

import tkinter as tk
from tkinter import simpledialog, messagebox

window = tk.Tk()

window.withdraw()

num1 = simpledialog.askfloat("Input", "Enter the first number:")

num2 = simpledialog.askfloat("Input", "Enter the second number:")

operation = simpledialog.askstring("Input", "Enter the operation" "add, subtract, multiply, divide")

 
if operation.lower() == "add":
    result = num1 + num2
    messagebox.showinfo("Result", f"The result is: {result}")
elif operation.lower() == "subtract":
    result = num1 - num2
    messagebox.showinfo("Result", f"The result is: {result}")
elif operation.lower() == "multiply":
    result = num1 * num2
    messagebox.showinfo("Result", f"The result is: {result}")
elif operation.lower() == "divide":
    if num2 == 0:
        messagebox.showerror("Error", "Cannot divide by zero!")
    else:
        result = num1 / num2
        messagebox.showinfo("Result", f"The result is: {result}")


messagebox.showwarning("Cancelled", "One or both numbers were not entered.")

window.mainloop()  