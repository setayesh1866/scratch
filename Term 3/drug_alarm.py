import tkinter as tk
from tkinter.constants import ACTIVE, DISABLED
import tkinter.ttk as ttk
from time import sleep

################# Def ########################
def callback1(a, b, c):
    p1.set(name1.get())
        
def callback2(a, b, c):
    p2.set(name2.get())

def callback3(a, b, c):
    p3.set(name3.get())

def time_format(second):
    h = int(second/3600)
    tem = h%3600
    m = int(tem/60)
    s = m%60
    return '%02d:%02d:%02d', h, m, s

def counter(seconds, var, button):
    button.config(state=DISABLED)
    while seconds:
        sleep(1)
    seconds -= 1
    var.set(time_format(seconds))
    button.config(state=ACTIVE)


def callback_t1(a, b, c):
    h1 = int(h_p_1.get())
    m1 = int(m_p_1.get())
    s1 = int(s_p_1.get())
    p4.set('%02d:%02d:%02d'%(h1, m1, s1))

def callback_t2(a, b, c):
    h2 = int(h_p_2.get())
    m2 = int(m_p_2.get())
    s2 = int(s_p_2.get())
    p5.set('%02d:%02d:%02d'%(h2, m2, s2))

def callback_t3(a, b, c):
    h3 = int(h_p_3.get())
    m3 = int(m_p_3.get())
    s3 = int(s_p_3.get())
    p6.set('%02d:%02d:%02d'%(h3, m3, s3))

def start(number):
    if number == 1:
        seconds1 = int(h_p_1.get())*3600 + int()





#########################################
root = tk.Tk()
root.geometry('300x300')

note = ttk.Notebook(root)
note.grid(row=0, column=0)
#########################################
patients = ttk.Frame(note)
note.add(patients, text='Patients')
timers = ttk.Frame(note)
note.add(timers, text='Timers')
##################### patient ####################
lf1 = tk.LabelFrame(patients, text='Patient 1')
lf1.grid(row=0, column=0)

tk.Label(lf1, text='Name').grid(row=0, column=0)
tk.Label(lf1, text='Time').grid(row=1, column=0)
name1 = tk.StringVar()
En1 = tk.Entry(lf1, textvariable=name1).grid(row=0, column=1)
name1.trace('w', callback1)

lf2 = tk.LabelFrame(patients, text='Patient 2')
lf2.grid(row=1, column=0)
name1.trace('w', callback1)

tk.Label(lf2, text='Name').grid(row=0, column=0)
tk.Label(lf2, text='Time').grid(row=1, column=0)
name2 = tk.StringVar()
En2 = tk.Entry(lf2, textvariable=name2).grid(row=0, column=1)
name2.trace('w', callback2)

lf3 = tk.LabelFrame(patients, text='Patient 3')
lf3.grid(row=2, column=0)

tk.Label(lf3, text='Name').grid(row=0, column=0)
tk.Label(lf3, text='Time').grid(row=1, column=0)
name3 = tk.StringVar()
En3 = tk.Entry(lf3, textvariable=name3).grid(row=0, column=1)
name3.trace('w', callback3)
################## timers #######################
f1 = tk.Frame(lf1)
f1.grid(row=1, column=1)
h_p_1 = tk.StringVar()
h_p_1.set('12')
m_p_1 = tk.StringVar()
m_p_1.set('30')
s_p_1 = tk.StringVar()
s_p_1.set('30')
tk.Spinbox(f1, from_=0, to=23, wrap=True, width=2, textvariable=h_p_1, state='readonly').grid(row=0, column=0)
tk.Spinbox(f1, from_=0, to=59, wrap=True, width=2, textvariable=m_p_1, state='readonly').grid(row=0, column=1)
tk.Spinbox(f1, from_=0, to=59, wrap=True, width=2, textvariable=s_p_1, state='readonly').grid(row=0, column=2)

f2 = tk.Frame(lf2)
f2.grid(row=1, column=1)
h_p_2 = tk.StringVar()
h_p_2.set('12')
m_p_2 = tk.StringVar()
m_p_2.set('30')
s_p_2 = tk.StringVar()
s_p_2.set('30')
tk.Spinbox(f2, from_=0, to=23, wrap=True, width=2, textvariable=h_p_2, state='readonly').grid(row=0, column=0)
tk.Spinbox(f2, from_=0, to=59, wrap=True, width=2, textvariable=m_p_2, state='readonly').grid(row=0, column=1)
tk.Spinbox(f2, from_=0, to=59, wrap=True, width=2, textvariable=s_p_2, state='readonly').grid(row=0, column=2)

f3 = tk.Frame(lf3)
f3.grid(row=1, column=1)
h_p_3 = tk.StringVar()
h_p_3.set('12')
m_p_3 = tk.StringVar()
m_p_3.set('30')
s_p_3 = tk.StringVar()
s_p_3.set('30')
tk.Spinbox(f3, from_=0, to=23, wrap=True, width=2, textvariable=h_p_3, state='readonly').grid(row=0, column=0)
tk.Spinbox(f3, from_=0, to=59, wrap=True, width=2, textvariable=m_p_3, state='readonly').grid(row=0, column=1)
tk.Spinbox(f3, from_=0, to=59, wrap=True, width=2, textvariable=s_p_3 , state='readonly').grid(row=0, column=2)
################### timer ######################
p1 = tk.StringVar()
p1.set('Patient 1')
tk.Label(timers, textvariable=p1).grid(row=0, column=0, padx=10, pady=10)

p2 = tk.StringVar()
p2.set('Patient 2')
tk.Label(timers, textvariable=p2).grid(row=0, column=1, pady=10)

p3 = tk.StringVar()
p3.set('Patient 3')
tk.Label(timers, textvariable=p3).grid(row=0, column=2, padx=10, pady=10)

p4 = tk.StringVar()
p4.set('00:00:00')
tk.Label(timers, textvariable=p4).grid(row=1, column=0, pady=10)

p5 = tk.StringVar()
p5.set('00:00:00')
tk.Label(timers, textvariable=p5).grid(row=1, column=1, pady=10)

p6 = tk.StringVar()
p6.set('00:00:00')
tk.Label(timers, textvariable=p6).grid(row=1, column=2, pady=10)
################### Button ######################
p7 = tk.Button(timers, text='Start').grid(row=2, column=0)

p8 = tk.Button(timers, text='Start').grid(row=2, column=1)

p9 = tk.Button(timers, text='Start').grid(row=2, column=2)

p10 = tk.Button(timers, text='Cancle', command=root.destroy).grid(row=3, column=0, pady=10, columnspan=4, sticky='we')
#########################################
h_p_1.trace('w', callback_t1)
m_p_1.trace('w', callback_t2)
s_p_1.trace('w', callback_t3)
h_p_2.trace('w', callback_t1)
m_p_2.trace('w', callback_t2)
s_p_2.trace('w', callback_t3)
h_p_3.trace('w', callback_t1)
m_p_3.trace('w', callback_t2)
s_p_3.trace('w', callback_t3)
#########################################
root.mainloop()