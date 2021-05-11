import tkinter as tk
from tkinter import messagebox

def Mama():
    messagebox.showinfo('Mama Album.2012', 'Songs:\n*Mama\n*What is love\n*History\n*Angel\n*Two moons\n*Machine')

def Xoxo():
    messagebox.showinfo('Xoxo Album.2013', 'Songs:\n*Wolf\n*Black pearl\n*Let out the beast\n*Heart attack\n*Baby\n*Baby don’t cry\n*Don’t go\n*3.6.5\n*Peter pan\n*My lady')

def MID():
    messagebox.showinfo('Miracles in December Album.2013', 'Songs:\n*Miracles in December\n*The star\n*The first snow\n*Christmas day\n*My turn to cry')

def Overdose():
    messagebox.showinfo('Overdose Album.2014', 'Songs:\n*Overdose\n*Moonlight\n*Thunder\n*run\n*Love, Love, Love')

def Exodus():
    messagebox.showinfo('Exodus Album.2015', 'Songs:\n*Call me baby\n*What if…\n*EXODUS\n*Playboy\n*lady luck\n*Transformer\n*My answer\n*EL Dorado\n*Hurt\n*Beautiful')

def SFU():
    messagebox.showinfo('Sing for you Album.2015', 'Songs:\n*Unfair\n*Sing for u\n*Girl x friend\n*On the snow\n*Lightsaber')

def ExAct():
    messagebox.showinfo('ExAct Album.2016', 'Songs:\n*Lucky one\n*Monster\n*Artificial love\n*Cloud 9\n*Heaven\n*White noise\n*One and only\n*They never know\n*stronger\n*lotto')

def Forlife():
    messagebox.showinfo('For Life Album.2016', 'Songs:\n*For life\n*Falling for u\n*What i want for Christmas\n*Twenty four\n*Winter heart')

def TheWar():
    messagebox.showinfo('The War Album.2017', 'Songs:\n*The war\n*Ko ko bop\n*What do u?\n*Forever\n*Diamond\n*Touch it\n*Chill\n*Walk on memories\n*Going crazy\n*power')

def Universe():
    messagebox.showinfo('Universe Album.2017', 'Songs:\n*Universe\n*Been trough\n*Stay\n*Fall\n*Good night\n*Lights out')

def Countdown():
    messagebox.showinfo('Countdown Album.2018', 'Songs:\n*Electric kiss\n*Coming over\n*Love me right\n*Lightsaber\n*Tactix\n*Into my world\n*Lovin’ you mo’\n*Drop that\n*Run this\n*Cosmic railway')

def Tempo():
    messagebox.showinfo('tempo Album.2018', 'Songs:\n*Tempo\n*Sign\n*Ooh la la la\n*Gravity\n*24.7\n*Damage\n*Smile on my face\n*Love shot')

def Obsession():
    messagebox.showinfo('Obsession Album.2019', 'Songs:\n*Obsession\n*Trouble\n*Jekyll\n*Groove\n*Ya Ya Ya\n*Baby u are\n*Non stop\n*Day after day\n*Butterfly Effect')

col = {
    'bg' : '#ff7a69',
    'fg' : '#000000',
}

clu = {
    'bg' : '#69ffe9',
    'fg' : '#000000',
}

root = tk.Tk()
print(root.configure().keys())
root.config(bg='#81d493')
#####################################
L1 = tk.Label(root, text='Hi!You can see EXO Albums and Songs =)', bg='#81d493')
L1.grid(row=0, column=1)
#####################################
L2 = tk.Label(root, text='Mama Album', cnf=col)
L2.grid(row=1, column=0)
B1 = tk.Button(root, text='Mama', command=Mama, cnf=clu)
B1.grid(row=2, column=0)
#########################
L3 = tk.Label(root, text='Xoxo Album', cnf=col)
L3.grid(row=1, column=1)
B2 = tk.Button(root, text='Xoxo', command=Xoxo, cnf=clu)
B2.grid(row=2, column=1)
#########################
L4 = tk.Label(root, text='Miracles in December Album', cnf=col)
L4.grid(row=1, column=2)
B3 = tk.Button(root, text='M.I.D', command=MID, cnf=clu)
B3.grid(row=2, column=2)
#####################################
L5 = tk.Label(root, text='Overdose Album', cnf=col)
L5.grid(row=3, column=0)
B4 = tk.Button(root, text='Overdose',command=Overdose , cnf=clu)
B4.grid(row=4, column=0)
#########################
L6 = tk.Label(root, text='Exodus Album', cnf=col)
L6.grid(row=3, column=1)
B5 = tk.Button(root, text='Exoeus',command=Exodus , cnf=clu)
B5.grid(row=4, column=1)
#########################
L7 = tk.Label(root, text='Sing for you Album', cnf=col)
L7.grid(row=3, column=2)
B6 = tk.Button(root, text='S.F.U',command=SFU , cnf=clu)
B6.grid(row=4, column=2)
#####################################
L8 = tk.Label(root, text='ExAct Album', cnf=col)
L8.grid(row=5, column=0)
B7 = tk.Button(root, text='ExAct',command=ExAct , cnf=clu)
B7.grid(row=6, column=0)
#########################
L9 = tk.Label(root, text='For life Album', cnf=col)
L9.grid(row=5, column=1)
B8 = tk.Button(root, text='Forlife',command=Forlife , cnf=clu)
B8.grid(row=6, column=1)
#########################
L10 = tk.Label(root, text='The war Album', cnf=col)
L10.grid(row=5, column=2)
B9 = tk.Button(root, text='TheWar',command= TheWar , cnf=clu)
B9.grid(row=6, column=2)
#####################################
L11 = tk.Label(root, text='Universe Album', cnf=col)
L11.grid(row=7, column=0)
B9 = tk.Button(root, text='Universe',command=Universe , cnf=clu)
B9.grid(row=8, column=0)
#####################################
L12 = tk.Label(root, text='Countdown Album', cnf=col)
L12.grid(row=7, column=1)
B9 = tk.Button(root, text='Countdown',command=Countdown , cnf=clu)
B9.grid(row=8, column=1)
#####################################
L13 = tk.Label(root, text='Don’t mess up my Tempo Album', cnf=col)
L13.grid(row=7, column=2)
B9 = tk.Button(root, text='Tempo',command=Tempo , cnf=clu)
B9.grid(row=8, column=2)
#####################################
L14 = tk.Label(root, text='Obsession Album', cnf=col)
L14.grid(row=9, column=1)
B9 = tk.Button(root, text='Obsession',command=Obsession , cnf=clu)
B9.grid(row=10, column=1)
#####################################
root.mainloop()