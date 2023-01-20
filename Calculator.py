from tkinter import *
import tkinter.messagebox
class calculator:
    def __init__(self):
        poorna.geometry("500x500")
        title = Label(poorna, text="poorna_calculator", pady=3)
        title1 = Label(poorna, text="this is mine", pady=2)
        title.pack()
        title1.pack()
        frame = Frame(poorna, bg="pink")
        frame.pack()
        entry = Entry(frame)
        entry.grid(row=0, column=0, columnspan=60, padx=10, pady=10,ipadx=60,ipady=10)
        def myclick(number):
            entry.insert(END, number)

        def equal():
            try:
                y = str(eval(entry.get()))
                entry.delete(0, END)
                entry.insert(0,y)
            
            except:
                tkinter.messagebox.showinfo("Error", "Syntax Error")
        
        def clear():
            entry.delete(0,END)

        button_sp = Button(master=frame, text="(", padx=20, pady=20, width=4, command=lambda: myclick("("))
        button_sp.grid(row=1, column=0, padx=2,pady=2)
        button_sp = Button(master=frame, text=")", padx=20, pady=20, width=4, command=lambda: myclick(")"))
        button_sp.grid(row=1, column=1, padx=2,pady=2)
        button_sp = Button(master=frame, text="%", padx=20, pady=20, width=4, command=lambda: myclick("%"))
        button_sp.grid(row=1, column=2, padx=2,pady=2)
        button_sp = Button(master=frame, text="/", padx=20, pady=20, width=4, command=lambda: myclick("/"))
        button_sp.grid(row=1, column=3, padx=2,pady=2)
        button_sp = Button(master=frame, text="7", padx=20, pady=20, width=4, command=lambda: myclick("7"))
        button_sp.grid(row=2, column=0, padx=2,pady=2)
        button_sp = Button(master=frame, text="8", padx=20, pady=20, width=4, command=lambda: myclick("8"))
        button_sp.grid(row=2, column=1, padx=2,pady=2)
        button_sp = Button(master=frame, text="9", padx=20, pady=20, width=4, command=lambda: myclick("9"))
        button_sp.grid(row=2, column=2, padx=2,pady=2)
        button_sp = Button(master=frame, text="*", padx=20, pady=20, width=4, command=lambda: myclick("*"))
        button_sp.grid(row=2, column=3, padx=2,pady=2)
        button_sp = Button(master=frame, text="4", padx=20, pady=20, width=4, command=lambda: myclick("4"))
        button_sp.grid(row=3, column=0, padx=2,pady=2)
        button_sp = Button(master=frame, text="5", padx=20, pady=20, width=4, command=lambda: myclick("5"))
        button_sp.grid(row=3, column=1, padx=2,pady=2)
        button_sp = Button(master=frame, text="6", padx=20, pady=20, width=4, command=lambda: myclick("6"))
        button_sp.grid(row=3, column=2, padx=2,pady=2)
        button_sp = Button(master=frame, text="-", padx=20, pady=20, width=4, command=lambda: myclick("-"))
        button_sp.grid(row=3, column=3, padx=3,pady=2)
        button_sp = Button(master=frame, text="1", padx=20, pady=20, width=4, command=lambda: myclick("1"))
        button_sp.grid(row=4, column=0, padx=2,pady=2)
        button_sp = Button(master=frame, text="2", padx=20, pady=20, width=4, command=lambda: myclick("2"))
        button_sp.grid(row=4, column=1, padx=2,pady=2)
        button_sp = Button(master=frame, text="3", padx=20, pady=20, width=4, command=lambda: myclick("3"))
        button_sp.grid(row=4, column=2, padx=2,pady=2)
        button_sp = Button(master=frame, text="+", padx=20, pady=20, width=4, command=lambda: myclick("+"))
        button_sp.grid(row=4, column=3, padx=2,pady=2)
        button_sp = Button(master=frame, text="clear", padx=20, pady=20, width=4, command=clear)
        button_sp.grid(row=5, column=0, padx=2,pady=2)
        button_sp = Button(master=frame, text="0", padx=20, pady=20, width=4, command=lambda: myclick("0"))
        button_sp.grid(row=5, column=1, padx=2,pady=2)
        button_sp = Button(master=frame, text=".", padx=20, pady=20, width=4, command=lambda: myclick("."))
        button_sp.grid(row=5, column=2, padx=2,pady=2)
        button_sp = Button(master=frame, text="=", padx=20, pady=20, width=4, command=equal)
        button_sp.grid(row=5, column=3, padx=2,pady=2)
        

        
poorna=Tk()

obj = calculator()
poorna.mainloop()