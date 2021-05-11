import tkinter as tk

root = tk.Tk()
conf = {
    'width' : '5',
    'height' : '5',
}

L1 = tk.Label(root, text='L1', cnf=conf, font=('times', 20), bg='red')
L1.grid(row=0, column=0)
L2 = tk.Label(root, text='L2', cnf=conf, font=('times', 20), bg='orange')
L2.grid(row=0, column=1, columnspan=2, sticky=tk.W+tk.E)
L3 = tk.Label(root, text='L3', cnf=conf, font=('times', 20), bg='yellow')
L3.grid(row=1, column=0, rowspan=2, sticky=tk.S+tk.N)
L4 = tk.Label(root, text='L4', cnf=conf, font=('times', 20), bg='green')
L4.grid(row=1, column=1)
L5 = tk.Label(root, text='L5', cnf=conf, font=('times', 20), bg='blue')
L5.grid(row=1, column=2)
L6 = tk.Label(root, text='L6', cnf=conf, font=('times', 20), bg='purple')
L6.grid(row=2, column=1, columnspan=2, sticky=tk.E+tk.W)
root.mainloop()