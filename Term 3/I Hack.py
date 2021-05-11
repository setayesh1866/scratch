import tkinter as tk
from tkinter import messagebox
###############################
l_colr = {
    'bg' : '#2d5e91',
    'fg' : '#000000',
}
b_colr = {
    'bg' : '#63b0ff',
    'fg' : '#000000',
}

def Carolyn():
    messagebox.showinfo('::target info', 'information gthered for selected target:\n\nName: Carolyn\nLastname: Scott\nGender: Female\nBrithadte: 01/31/1995\nOccupation: Dentist\nPassword difficulty: basic')
def Patrick():
    messagebox.showinfo('::target info', 'information gathered for selecred target:\n\nName: Patrick\nLasynAME: Taylor\nGender: Male\nBrithdate: 07/09/1989\nOccupation: Hotel manager\nPassword difficulty; intermediate')
def Linda():
    messagebox.showinfo('::target info', 'informtion gathered for selected terget:\n\nName: Linda\nLastname: Martin\nGender: Female\nBrithdate: 07/18/2001\nOccupation: Goverment lawyer\nFavorite Show: Simposons\nPassword difficulty: expert')
###############################
root = tk.Tk()
print(root.configure().keys())
root.config(bg='#2d5e91')
###############################
L1 = tk.Label(root, text='Target: Carolyn Scott', cnf=l_colr)
L1.grid(row=0, column=0)
B1 = tk.Button(root, text='Show Information',cnf=b_colr, command=Carolyn)
B1.grid(row=0, column=1)
L2 = tk.Label(root, text='Target: Patrick Taylor', cnf=l_colr)
L2.grid(row=1, column=0)
B2 = tk.Button(root, text='Show Information',cnf=b_colr, command=Patrick)
B2.grid(row=1, column=1)
L3 = tk.Label(root, text='Target: Linda Martin', cnf=l_colr)
L3.grid(row=2, column=0)
B3 = tk.Button(root, text='Show Information',cnf=b_colr, command=Linda)
B3.grid(row=2, column=1)
B4 = tk.Button(root, text='Cancle', command=root.destroy, bg='#ff3d3d')
B4.grid(row=3, column=0, sticky='we', columnspan=2)
###############################
root.mainloop()