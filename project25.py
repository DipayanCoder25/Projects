from tkinter import *

def convert():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{inches} inches = {cm:.2f} cm")
    except ValueError:
        result_label.config(text="Please enter a valid number")


root = Tk()
root.title("Inches to Centimeters Converter")
root.geometry("400x400")
# Input field
Label(root, text="Enter length in inches:").pack(padx=10,pady=5)
entry = Entry(root)
entry.pack(pady=5)

# Convert button
convert_btn = Button(root, text="Convert", command=convert)
convert_btn.pack(pady=5)

# Result label
result_label = Label(root, text="")
result_label.pack(pady=5)


root.mainloop()
