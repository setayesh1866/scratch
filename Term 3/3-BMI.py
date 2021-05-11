import tkinter as tk
from tkinter import messagebox

def BMI():
    try:
        w = float(E1.get())
        h = float(E2.get())
        index = w / (h*h)
        messagebox.showinfo('Your BMI', f'Your BMI value is: {index:.2f}')
        if index  < 18.5:
            print('You are UNDER WEIGHT!')
            uw = 18.5 - index + 1
            print(f'you have to add {uw} Kg to achieve the normal weight')
        elif index == 18.5, 24.9:
            print('You have NORMAl weight!')
        elif index == 25, 29.9:
            print('You are OVERWEIGHT!')
            ow = index - 20
            print(f'You have to lose {ow} Kg to achieve the normal weight')
        elif index == 30,34.9:
            print('You are OBESE')
            obs = index - 20
            print(f'You have to lose {obs} Kg to achieve the normal weight')
        elif index < 35:
            print('You are EXTERMELY OBESE!')
            eo = index - 20
            print(f'You have to lose {eo} Kg to achieve the normal weight')

    except:
        messagebox.showerror('FAILED', 'Ooops!')

dark = {
    'bg' : '#b3cbff',
    'fg' : '#000000',
}

root = tk.Tk()
print(root.configure().keys())
root.config(bg='#b3cbff')
#################################
L1 = tk.Label(root, text='Weight(Kg)', cnf=dark)
L1.grid(row=0, column=0)
E1 = tk.Entry(root, bg='#fff6b3', fg='#000000')
E1.grid(row=0, column=1)
#################################
L2 = tk.Label(root, text='Hight(M)', cnf=dark)
L2.grid(row=1, column=0)
E2 = tk.Entry(root, bg='#fff6b3', fg='#000000')
E2.grid(row=1, column=1)
#################################
frame = tk.Frame(root)
frame.grid(row=2, column=0, columnspan=2)
B1 = tk.Button(frame, text='Calculate', command=BMI, bg='#ff8adc', fg='#000000')
B1.grid(row=2, column=0)
B2 = tk.Button(frame, text='Cancle', command=root.destroy, bg='#d08aff', fg='#000000')
B2.grid(row=2, column=1)

root.mainloop()