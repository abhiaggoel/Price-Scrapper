import tkinter
import bs4                              # Contains functions to fetch information (price of product) from the internet.
import urllib.request                   # It will help to open up a web page.
import smtplib                          # For mail sending
import time
import datetime
import sys
from tkinter import *
from tkinter import PhotoImage
from tkinter import ttk
from tkinter.messagebox import *
from random import randint
from PIL import Image

def on_exit(root):
    alpha = root.attributes("-alpha")
    if alpha > 0.01:
        alpha -= .01
        root.attributes("-alpha", alpha)
        root.after(150, lambda: on_exit(root))
    else:
        root.destroy()
        exit()

def desired_screen():
    root=Tk()
    root.configure(background='light cyan')
    root.geometry('600x400')
    root.title('Your Desired Price is Matched')
    #root.resizable(False,False)
    root.iconbitmap('setimage\\index.ico')
    
    canvas = Canvas(root, width=400, height=100, highlightbackground="red",
                    highlightthicknes=5, bg='light cyan')
    canvas.place(x=300, y=200, anchor='center')
    canvas.create_text(200, 20, fill="tomato", font="Times 16",
                       text='''Hi''')
    canvas.create_text(200, 65, fill="dark violet", font="Times 14 italic",
                       text='''The Price of the Product has Dropped,
                                    you can now check it out...''')
    on_exit(root)
    #ok_btn = Button(fg="red", text="OK", command=on_exit(root), bg="black", foreground="yellow")
    #ok_btn.place(x=200, y=300, height=35, width=160)
    root.mainloop()
desired_screen()

