from Tkinter import *

window = Tk()

def xStam():
    print(e1_var.get())
    t1.insert(END, e1_var.get())

b1 = Button(window, text="Execute", command=xStam)
b1.grid(row=0, column=0)

e1_var = StringVar()
e1 = Entry(window, textvariable=e1_var)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()
