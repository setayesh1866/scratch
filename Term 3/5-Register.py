import tkinter as tk
from tkcalendar import DateEntry
import reg
import tkinter.ttk as ttk


def alphabet (a, b, c):
    if name.get().isalpha():
        e1.config(bg='#69ff6b')
    else:
        e1.config(bg='#ff6e63')
    
def alphabetl (a, b, c):
    if last.get().isalpha():
        e2.config(bg='#69ff6b')
    else:
        e2.config(bg='#ff6e63')


def callback(a, b, c):
    c = code.get()
    e4.config(bg='#ff6e63')
    if c.isdigit():
        if len(c) == 10:
            e4.config(bg='#69ff6b')
        elif len(c) > 10:
            code.set(c[:10])
            e4.config(bg='#69ff6b')
    elif len(c) > 10:
        code.set(c[:10])

def srch():
    file = open('names.txt', 'r')
    top = tk.Toplevel()
    top.geometry(f'{root.winfo_width()}x{root.winfo_height()}')
    text = tk.Text(top)
    text.grid(row=0, column=0)
    for l in file:
        if Search.get() in l:
            text.insert(tk.INSERT, l)


def Register(a=None):
    reg.register(
        name.get(),
        last.get(),
        brith.get(),
        code.get(),
    )
    name.set(''),
    last.set(''),
    code.set(''),
    e1.config(bg='white')
    e2.config(bg='white')
    e4.config(bg='white')


root = tk.Tk()
root.bind('<Return>', Register)
##################################
tk.Label(root, text='Name:').grid(row=0, column=0)
tk.Label(root, text='Last Name:').grid(row=1, column=0)
tk.Label(root, text='Brith Date:').grid(row=2, column=0)
tk.Label(root, text='ID Code:').grid(row=3, column=0)

name = tk.StringVar()
name.trace('w', alphabet)
e1 = tk.Entry(root, textvariable=name)
e1.grid(row=0, column=1)

last = tk.StringVar()
last.trace('w', alphabetl)
e2 = tk.Entry(root, textvariable=last)
e2.grid(row=1, column=1)

brith = tk.StringVar()
e3 = DateEntry(root, width=12, bg='purple', fg='pink',
    borderwidth=2, date_pattern='y-mm-dd')
e3.grid(row=2, column=1, sticky='we')

code = tk.StringVar()
code.trace('w', callback)
e4 = tk.Entry(root, textvariable=code)
e4.grid(row=3, column=1)

fram = tk.Frame()
fram.grid(row=4, column=0, columnspan=2)

tk.Button(fram, text='Register', command=Register).grid(row=0, column=0)
tk.Button(fram, text='Cancle', command=root.destroy).grid(row=0, column=1)

ttk.Separator(root, orient=tk.HORIZONTAL).grid(row=5, column=0, columnspan=2, sticky='ew')
tk.Label(root, text='Search').grid(row=6, column=0)
Search = tk.Entry(root)
Search.grid(row=6, column=1)
tk.Button(root, text='Search', command=srch).grid(row=7, column=0, columnspan=2)


root.mainloop()