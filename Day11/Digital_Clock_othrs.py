#Digital Clock in GUI

import os
os.system('cls')
from tkinter import *
from tkinter import font
import datetime

def myClock(): #To declare a Function
    tm=datetime.datetime.now()
    time=tm.strftime('%H:%M:%S') #Hour Minutes Seconds
    mytext.set(time)
    win.after(1000,myClock) #After 1 second, Function Name


win=Tk()
win.title('Digital Clock By Python:')
win.geometry('800x200')#WidthxHeight
# win.attributes('-Fullscreen',False) #To stop the Maximise of Full Screen. Prvious version not work in python
win.resizable(False,False) #Width,Height
win.configure(background='skyblue') #Color of the Background

myfont=font.Font(family='comicsense', size=120, weight='bold') #Customizing the Font Style
mytext=StringVar() #
#mytext.set('Ceasar')# To show my name


lblTime=Label(win,textvariable=mytext, font=myfont, foreground='white',background='pink') #Customizing the text 
lblTime.place(relx=0.5, rely=0.5,anchor=CENTER) #Declare the cordinate to display Text for X & Y



win.after(1000,myClock) #To call the function which will update after every 1 second.
win.mainloop() #To make a loop for execute the Template