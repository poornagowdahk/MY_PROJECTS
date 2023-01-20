from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("POORNA'S TIME")
root.geometry("400x400")
def time():
    string = strftime('%H:%M:%S: %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root , font=("ds-digital", 50), background="pink", foreground="black")
label.pack(anchor='center')
time()
mainloop()