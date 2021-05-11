import tkinter as tk

root = tk.Tk()
###################################
B1 = tk.Button(root, text='+')
B1.grid(row=0, column=2)
L1 = tk.Label(root, text='TEMPRATURE:')
L1.grid(row=1, column=1)
L2 = tk.Label(root, text='')
L2.grid(row=1, column=2)
B2 = tk.Button(root, text='+')
B2.grid(row=2, column=2)
###################################
root.mainloop()