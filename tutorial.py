import tkinter as tk
from tkinter import ttk


def button_func():
    print("a button was pressed")


# create  a window
window = tk.Tk()
window.title("Window and Widgets")
window.geometry("800x500")  # width x height for start

# ttk widgets / ttk label
label = ttk.Label(master=window, text="This is a Test")
label.pack()  # pack() placed widgets in below each other

# create widgets / tk.text
text = tk.Text(master=window)
text.pack()  # important split for widget with variable

# ttk entry
entry = ttk.Entry(master=window)
entry.pack()

label_2 = ttk.Label(master=window, text="my label")
label_2.pack()

button_2 = ttk.Button(master=window, text="say hi", command=lambda: print("hello"))
button_2.pack()

# ttk button
button = ttk.Button(master=window, text="A button", command=button_func)
button.pack()

# exercise
# add one more text label and a button with a function that prints "hello"
# the label should say "my label" and be between the entry widget and the button
# run
window.mainloop()  # updates, checks for events, nothing after it is executed while window is open
