"""
GUI
"""
import os
os.system('cls')
from tkinter import *
from tkinter import font
import datetime


def clock():
    tm=datetime.datetime.now()
    time=tm.strftime("%H:%M:%S")
    myText.set(time)
    win.after(1000,clock)



win=Tk()
win.title('Digital Clock Sabit')
win.geometry('800x300')
win.resizable(False,False)
win.configure(background='white')

myFont=font.Font(family='comicsense',size=120,weight='bold')
myText=StringVar()

lblTime=Label(win,textvariable=myText,font=myFont,foreground='red',background='black')
lblTime.place(relx=0.5,rely=0.5,anchor = CENTER)
# myText.set('Test')

win.after(1000,clock)
win.mainloop()
