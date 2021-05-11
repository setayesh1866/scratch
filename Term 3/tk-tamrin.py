import tkinter as tk

def add():
    number = int(e1.get()) + int(e2.get())
    l1.config(text=number)

dark = {
    'bg' : '#000000',
    'fg' : '#ffffff',
    'font' : ('timed', 20)
}

root = tk.Tk()
print(root.configure().keys())
root.config(bg='#000000')
l1 = tk.Label(root, text= '', cnf=dark)
l1.pack()
print(l1.configure().keys()) 

e1 = tk.Entry(root, cnf=dark)
e1.pack()
e2 = tk.Entry(root, cnf=dark)
e2.pack()

b1 = tk.Button(root, cnf=dark)
b1.pack()
root.mainloop()