import tkinter as tk
from datetime import date

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        today = date.today()
        age = today.year - year - ((today.month, today.day) < (month, day))

        result_label.config(text=f"Your Age: {age} years")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")


root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x250")

tk.Label(root, text="Enter Date of Birth", font=("Arial", 14)).pack(pady=10)

tk.Label(root, text="Day:").pack()
day_entry = tk.Entry(root)
day_entry.pack()

tk.Label(root, text="Month:").pack()
month_entry = tk.Entry(root)
month_entry.pack()

tk.Label(root, text="Year:").pack()
year_entry = tk.Entry(root)
year_entry.pack()


tk.Button(root, text="Calculate Age", command=calculate_age).pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
