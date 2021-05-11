import tkinter as tk

def press():
    print(el.get())

#widget
root = tk.Tk()
l1 = tk.Label(root, text='Rebka is here')
l1.pack()
el = tk.Entry(root)
el.pack()
bl = tk.Button(root, command=press, text='Ok!')
bl.pack()
root.mainloop()
