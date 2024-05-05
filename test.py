import tkinter as tk
import re

def limit_input(*args):
    value = entry.get()
    if len(value) > 2:
        entry.set(value[:2])
    elif not re.match("^[0-9]*$", value):
        entry.set(value[:-1])

root = tk.Tk()

entry = tk.StringVar()
entry.trace('w', limit_input)

entry_box = tk.Entry(root, textvariable=entry)
entry_box.pack()

root.mainloop()
