from tkinter import *
from tkinter import messagebox


def clear_entry():
    compute.delete(0, END)


def evaluate():
    the_input = compute.get()
    try:
        the_result = eval(the_input)
    except NameError:
        messagebox.showinfo(title="Oops", message="You can input only arithmetic expressions and numbers")
    except SyntaxError:
        messagebox.showinfo(title="Oops", message="You can input only arithmetic expressions and numbers")
    else:
        compute.delete(0, END)
        compute.insert(END, the_result)
    print(type(the_input))
    print(type(the_result))


# window setup
window = Tk()
window.title("CALCULATE")
window.config(padx=50, pady=50)

compute = Entry()
compute.grid(row=1, column=1, columnspan=3, sticky="EW")
compute.focus()

label1 = Label(text="")
label1.grid(row=2, column=2)

equal_button = Button(text="=", command=evaluate)
equal_button.grid(row=3, column=1)

clear_button = Button(text="CLEAR", command=clear_entry)
clear_button.grid(row=3, column=3)

window.mainloop()