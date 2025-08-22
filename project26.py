from tkinter import *
from tkinter import messagebox

def calculate_interest():
    try:
        p = float(principal_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())

        si = (p * t * r) / 100
        ci = p * ((1 + r/100) ** t) - p


        Label(root, text="Simple Interest:").pack(pady=5)
        si_entry = Entry(root)
        si_entry.pack()
        si_entry.insert(0, f"{si:.2f}")

        Label(root, text="Compound Interest:").pack(pady=5)
        ci_entry = Entry(root)
        ci_entry.pack()
        ci_entry.insert(0, f"{ci:.2f}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values")

root = Tk()
root.title("Interest Calculator")
root.geometry("400x400")


Label(root, text="Principal Amount:").pack(pady=5)
principal_entry = Entry(root)
principal_entry.pack()

Label(root, text="Time Period (years):").pack(pady=5)
time_entry = Entry(root)
time_entry.pack()

Label(root, text="Rate of Interest (%):").pack(pady=5)
rate_entry = Entry(root)
rate_entry.pack()

Button(root, text="Calculate", command=calculate_interest).pack(pady=10)

root.mainloop()
