import tkinter as tk
import random

window = tk.Tk()
window.title("Symulator rzutu kostką sześcienną")

def roll_dice():
  result = random.randint(1, 6)
  label.config(text=result)

button = tk.Button(text="Rzuć kostką", command=roll_dice)
button.pack()

label = tk.Label(text="")
label.pack()

w = 375
h = 50
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))
window.resizable(False, False)
window.mainloop()
