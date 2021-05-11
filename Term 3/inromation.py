import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
import tkinter.ttk as ttk
####################### Def #########################
def S1():
    messagebox.showinfo('BMW 1 Series', '➤BMW 1 Series 116i petrol model\n➤BMW 1 Series 118i petrol model\n➤BMW 1 Series 125i petrol model\n➤BMW 1 Series 135i M petrol model\n➤BMW 1 Series 140i M petrol model\n➤BMW 1 Series 114d Diesel\n➤BMW 1 Series 116d Diesel\n➤BMW 1 Series 118d Diesel\n➤BMW 1 Series 120d Diesel\n➤BMW 1 Series 125d Diesel\n')

def S2():
    messagebox.showinfo('BMW 2 Series', '➤BMW Series 2 Model 218i Gasoline\n➤BMW Series 2 Model 220i Gasoline\n➤BMW Series 2 Model 228i Gasoline\n➤BMW Series 2 Model 235i M Gasoline\n➤BMW Series 2 Model 240i M Gasoline\n➤BMW 2 Series Powerful M2 Gasoline Model\n➤BMW 2 Series Model 218d Diesel\n➤BMW 2 Series Model 220d Diesel\n➤BMW 2 Series Model 225d Diesel\n➤BMW 2 Series Model 235d Diesel(This car is used by the racing department (BMW Motorsport) due to its very high power and special dynamic powers.)\n')

 


####################### root #########################
root = tk.Tk()
root.title('Welcome to BMW information app')
root.geometry('450x500')
####################### notes #########################
note = ttk.Notebook(root)
note.grid(row=0, column=0)

mai = ttk.Frame(note)
note.add(mai, text='MainPage')

his = ttk.Frame(note)
note.add(his, text='History')

modl = ttk.Frame(note)
note.add(modl, text='Models')
####################### MainPage #########################
lf1 = tk.LabelFrame(mai)
lf1.grid(row=0, column=0)


l1 = tk.Label(lf1, text='Welcome!Here you can change setting\nAnd read helps')
l1.grid(row=0, column=0)

c1 = ttk.Combobox(lf1, value=['English', 'German', 'Farsi', 'French', 'Arabic', 'Korea', 'China', 'Japan'])
c1.grid(row=1, column=0, pady=10)
c1.set('Choose the language')

b1 = tk.Button(lf1, text='BG')
b1.grid(row=2, column=0)
b2 = tk.Button(lf1, text='FG')
b2.grid(row=3, column=0, pady=10)
b3 = tk.Button(lf1, text='Help')
b3.grid(row=4, column=0, sticky='')
####################### History Frame #########################
lf2 = tk.LabelFrame(his)
lf2.grid(row=0, column=0)

#Label
l1 = tk.Label(lf2, text='↓ History Buttons information ↓')
l1.grid(row=0, column=1, padx=10)

#Buttons
b1 = tk.Button(lf2, text='1916-1923')
b1.grid(row=1, column=0, pady=10)
b2 = tk.Button(lf2, text='1939-1923')
b2.grid(row=1, column=1, padx=10, pady=10)
b3 = tk.Button(lf2, text='1959-1945')
b3.grid(row=1, column=2, pady=10)

b4 = tk.Button(lf2, text='1968-1959')
b4.grid(row=3, column=0, pady=10)
b5 = tk.Button(lf2, text='1978-1968')
b5.grid(row=3, column=1, padx=10, pady=10)
b6 = tk.Button(lf2, text='1989-1978')
b6.grid(row=3, column=2, pady=10)

b7 = tk.Button(lf2, text='1990 to now')
b7.grid(row=7, column=1, padx=10, pady=10)
####################### Model Frame #########################
lf3 = tk.LabelFrame(modl)
lf3.grid(row=0, column=0)

#Labels
ll1 = tk.Label(lf3, text='↓ Models Buttons information ↓')
ll1.grid(row=0, column=1, padx=10)

#Buttons
bb1 = tk.Button(lf3, text='1 Series', command=S1)
bb1.grid(row=1, column=0, pady=10)
bb2 = tk.Button(lf3, text='2 Series', command=S2)
bb2.grid(row=1, column=1, padx=10, pady=10)
bb3 = tk.Button(lf3, text='3 Series')
bb3.grid(row=1, column=2, pady=10)

bb4 = tk.Button(lf3, text='4 Series')
bb4.grid(row=3, column=0, pady=10)
bb5 = tk.Button(lf3, text='5 Series')
bb5.grid(row=3, column=1, padx=10, pady=10)
bb6 = tk.Button(lf3, text='6 Series')
bb6.grid(row=3, column=2, pady=10)

bb7 = tk.Button(lf3, text='7 Series')
bb7.grid(row=5, column=0, pady=10)
bb8 = tk.Button(lf3, text='8 Series')
bb8.grid(row=5, column=1, padx=10, pady=10)
bb9 = tk.Button(lf3, text='X Series')
bb9.grid(row=5, column=2, pady=10)

bb10 = tk.Button(lf3, text='I Series')
bb10.grid(row=7, column=0, pady=10)
bb11 = tk.Button(lf3, text='M Series')
bb11.grid(row=7, column=1, padx=10, pady=10)
bb12 = tk.Button(lf3, text='Z Series')
bb12.grid(row=7, column=2, padx=10, pady=10)
################################################
root.mainloop()