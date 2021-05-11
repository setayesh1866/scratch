import tkinter as tk
from tkinter.ttk import Combobox


def wart():
    print(C1.get())

root = tk.Tk()
print(root.configure().keys())
root.configure(bg='red')
root.geometry('300x300')

L1 = tk.Label(root, text='choose me !', bg='red')
L1.pack()


C1 = Combobox(root, value=['1', '2', '3'])
C1.pack()
C1.set('Choose your number: ')

B1 = tk.Button(root, text='print', command=wart)
B1.pack()


root.mainloop()