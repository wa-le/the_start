from tkinter import *
from tkinter.ttk import *
from time import strftime

window = Tk()
window.title("CLOCK")


def time():
    the_time = strftime('%H:%M:%S %p')
    clock_label.config(text=the_time)
    clock_label.after(1000, time)


clock_label = Label(window, font=("ds-digital Bold", 80), background="black", foreground="cyan")
clock_label.pack(anchor='center')
time()

mainloop()