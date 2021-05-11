import tkinter as tk

def up():
    global temp
    temp =+ 1
    fan()

def down():
    global temp
    temp -= 1
    fan()

def fan():
    temptature.set('Temprature: ', str(temp))
    if temp >= 30:
        Fan_state.set('Fan is on')
        label2['background'] = '#00fc04'
    else:
        Fan_state.set('Fan is off')
        label2['background'] = '#fc0000'

################################################
root = tk.Tk()
root.geometry('300x150')
temp = 25
temptature = tk.StringVar()
Fan_state = tk.StringVar()
Button1 = tk.Button(root, text='▴', command=up)
Button2 = tk.Button(root, text='▾', command=down)
label1 = tk.Label(root, textvariable=temptature)
label2 = tk.Label(root, textvariable=Fan_state)
Button1.pack()
Button2.pack()
label1.pack()
label2.pack()
root.mainloop()