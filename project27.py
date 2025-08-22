from tkinter import *
from tkinter import messagebox


def check_strength():
    password = password_entry.get()
    length = len(password)

    if length <= 5:
        strength = "Weak"
        color = "red"
    elif 6 <= length <= 8:
        strength = "Medium"
        color = "yellow"
    elif 9 <= length <= 12:
        strength = "Strong"
        color = "lightgreen"
    else:
        strength = "Very Strong"
        color = "darkgreen"

    result_label.config(text=f"Password Strength: {strength}", fg=color)


root = Tk()
root.title("Length Converter App")
root.geometry("400x400")

Label(root, text="Enter Password:").pack(pady=10)
password_entry = Entry(root, show="*")
password_entry.pack(pady=5)

Button(root, text="Check Strength", command=check_strength).pack(pady=10)

result_label = Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()
