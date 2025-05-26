"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""
import tkinter as tk
from tkinter import simpledialog, messagebox

window = tk.Tk()

window.withdraw()

num1 = simpledialog.askfloat("Input", "Enter the first number:")

num2 = simpledialog.askfloat("Input", "Enter the second number:")

if num1 is not None and num2 is not None:
    total = num1 + num2
    messagebox.showinfo("Result", f"The sum of the two numbers is: {total}")
else:
    messagebox.showwarning("Cancelled", "One or both numbers were not entered.")

window.mainloop()