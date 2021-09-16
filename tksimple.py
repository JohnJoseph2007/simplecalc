import tkinter as tk
from tkinter import *
from tkinter import ttk

ans = 0

dum = tk.Tk()
dum.title("Calculator")

def evaluate():
    global ans
    if op.get() == '+':
        ans = int(n1.get()) + int(n2.get())
        Label(dum, text=ans).grid(row=4, column=0)
    elif op.get() == '-':
        ans = int(n1.get()) - int(n2.get())
        Label(dum, text=ans).grid(row=4, column=0)
    elif op.get() == '*':
        ans = int(n1.get()) * int(n2.get())
        Label(dum, text=ans).grid(row=4, column=0)
    elif op.get() == '/':
        ans = int(n1.get()) / int(n2.get())
        Label(dum, text=ans).grid(row=4, column=0)
    elif op.get() == '%':
        ans = int(n1.get()) % int(n2.get())
        Label(dum, text=ans).grid(row=4, column=0)
    else:
        ans = "Invalid input detected"
        Label(dum, text=ans).grid(row=4, column=0)

Label(dum, text="First Number").grid(row=0)
Label(dum, text="Second Number").grid(row=1)
Label(dum, text="Operator").grid(row=2)
n1 = Entry(dum)
n2 = Entry(dum)
op = Entry(dum)
n1.grid(row=0, column=1)
n2.grid(row=1, column=1)
op.grid(row=2, column=1)
Label(dum, text=" ").grid(row=3)
button = tk.Button(dum, text="Submit", width=10, command=evaluate).grid(row=4, column=1)

dum.mainloop()
