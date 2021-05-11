import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text='1', font=('times', 20), width=5)
label.grid(row=0, column=0)
label = tk.Label(root, text='2', font=('times', 20))
label.grid(row=0, column=1)
label = tk.Label(root, text='3', font=('times', 20))
label.grid(row=1, column=1)

root.mainloop()