import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter.ttk import Combobox
import tkinter.ttk as ttk
#########################################
root = tk.Tk()
root.title('Welcome to BMW information APP')
root.geometry('450x500')

note = ttk.Notebook(root)
note.grid(row=0, column=0)


mai = ttk.Frame(note)
note.add(mai, text='MainPage')


his = ttk.Frame(note)
note.add(his, text='History')


mod = ttk.Frame(note)
note.add(mod, text='Models')
#image2 = Image.open('F:\Cars\BMW', 'BMW BG.png', formats=PNG)
#image1 = ImageTk.PhotoImage(image2)
#w = image1.width()
#h = image1.height()
#########################################
lf1 = tk.LabelFrame(mai)
lf1.grid(row=0, column=0)

L1 = tk.Label(lf1, text='Bayerich Motoren Verke Ag, also known as BMW and BMW,\nis a German multinational automotive super company\nWhich is one of the manufacturers of luxury cars and motorcycles in the world.')
L1.grid(row=0, column=0)
C1 = Combobox(lf1, value=['English', 'German', 'Farsi', 'French', 'Arabic', 'Korea', 'China', 'Japan'])
C1.grid(row=1, column=0)
C1.set('Choose the language')
#########################################
lf2 = tk.LabelFrame(his)
lf2.grid(row=0, column=0)
L3 = tk.Label(lf2, text='1916-1923: Aircraft engine production era')
L3.grid(row=0, column=0)
B1 = tk.Button(lf2, text='Show Information')
B1.grid(row=0, column=1)

lf3 = tk.LabelFrame(his)
lf3.grid(row=1, column=0)
L4 = tk.Label(lf3, text='1939-1923: The era of motorcycle and car production')
L4.grid(row=0, column=0)
B2 = tk.Button(lf3, text='Show Information')
B2.grid(row=0, column=1)

lf4 = tk.LabelFrame(his)
lf4.grid(row=2, column=0)
L5 = tk.Label(lf4, text='1945-1939: World War II')
L5.grid(row=0, column=0)
B3 = tk.Button(lf4, text='Show Information')
B3.grid(row=0, column=1)

lf5 = tk.LabelFrame(his)
lf5.grid(row=3, column=0)
L6 = tk.Label(lf5, text='1959-1945: Reconstruction period after World War II')
L6.grid(row=0, column=0)
B4 = tk.Button(lf5, text='Show Information')
B4.grid(row=0, column=1)

lf6 = tk.LabelFrame(his)
lf6.grid(row=4, column=0)
L7 = tk.Label(lf6, text='1968-1959: Hard times and new class')
L7.grid(row=0, column=0)
B5 = tk.Button(lf6, text='Show Information')
B5.grid(row=0, column=1)

lf7 = tk.LabelFrame(his)
lf7.grid(row=5, column=0)
L7 = tk.Label(lf7, text='1978-1968: The era of making 3,5,7 series')
L7.grid(row=0, column=0)
B5 = tk.Button(lf7, text='Show Information')
B5.grid(row=0, column=1)

lf8 = tk.LabelFrame(his)
lf8.grid(row=5, column=0)
L8 = tk.Label(lf8, text='1989-1978: Production period of the sector M')
L8.grid(row=0, column=0)
B6 = tk.Button(lf8, text='Show Information')
B6.grid(row=0, column=1)

lf9 = tk.LabelFrame(his)
lf9.grid(row=5, column=0)
L8 = tk.Label(lf9, text='1989-1978: Production period of the sector M')
L8.grid(row=0, column=0)
B6 = tk.Button(lf9, text='Show Information')
B6.grid(row=0, column=1)
#########################################
root.mainloop()