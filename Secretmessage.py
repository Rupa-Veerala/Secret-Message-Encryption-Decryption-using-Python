import tkinter
from tkinter import *
from tkinter import messagebox
import base64
import os

def main_screen():

    screen=Tk()
    screen.geometry("375x398")

    #icon
    image_icon=PhotoImage(file="keys.png")
    screen.iconphoto(False,image_icon)
    screen.title("PctApp")
    
    Label(text="Enter text for encryption and decryption",fg="red",font=("calbri",13)).place(x=10,y=10)
    text1=Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)

    Label(text="Enter secret key for encryption and decryption",fg="black",font=("calibri",13)).place(x=10,y=170)

    code=StringVar()
    Entry(textvariable=code,width=19,bd=0,)
    screen.mainloop()

main_screen()