import tkinter as tk

####################################
b_col = {
    'bg' : '#ff5454',
    'fg' : '#000000',
}

l_col = {
    'bg' : '#54ff68',
    'fg' : '#000000',
}
####################################
root = tk.Tk()
print(root.configure().keys())
root.config(bg='#54ff68')
####################################
l1 = tk.Label(root, text='20:00', cnf=l_col)
l1.grid(row=0, column=0)
l2 = tk.Label(root, text='20:00', cnf=l_col)
l2.grid(row=0, column=2)

b1 = tk.Button(root, text='Stop', cnf=b_col)
b1.grid(row=1, column=0)
b2 = tk.Button(root, text='Stop', cnf=b_col)
b2.grid(row=1, column=2)

b3 = tk.Button(root, text='Cancle', cnf=b_col, command=root.destroy)
b3.grid(row=2, column=0, columnspan=4, sticky='we')

root.mainloop()