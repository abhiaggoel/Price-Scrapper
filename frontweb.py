"""Importing Modules"""

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
        root.after(10, lambda: on_exit(root))
    else:
        root.destroy()
        exit()

    
top = Tk()
top.resizable(False,False)
top.geometry("612x408")


##top.config(bg="black")

top.minsize(612, 408)
top.maxsize(612, 408)
top.title("Web Scraping")

colour='#e8de87'

def update():
    ##color="%05x" %randint(0,0xFFFFFF)
    ##top.config(background ='#000000' + color)  or
    top.config(background=colour,highlightthickness='2')
    ##top.after(1000, update)
    top.iconbitmap('setimage\\index.ico')


update()

# image = PhotoImage(file='black.png')
# label = Label(top, image=image)
# label.place(x=0, y=0, relwidth=1, relheight=1)

##title = Label(top, text="PRICE SCRAPER", font="comicsansms 30 bold underline", bg="black", fg="yellow")
title=  Label(top, text='Price Scraper', font=('Calibri', '40', 'bold', 'underline'),bg=colour, fg='red')
title.place(x=155, y=10)


input_url = Label(top, text="ENTER THE URL", font="Calibri 15",bg=colour, fg="blue")
input_url.place(x=240, y=100)

input_url_value = StringVar()

url_entry = Entry(top, textvariable=input_url_value, bg="white", fg="black", borderwidth=6, relief=SUNKEN)
url_entry.place(x=70, y=140, height=25, width=500)

desire_price = Label(top, text="ENTER THE DESIRED PRICE ", font="Calibri 15",bg=colour, fg="blue")
desire_price.place(x=185, y=190)

input_desire_price = StringVar()

inp_dp = Entry(top, textvariable=input_desire_price, bg="white", fg="black", borderwidth=6, relief=SUNKEN)
inp_dp.place(x=240, y=230, height=25, width=150)



def button_clicked():
    url = url_entry.get()
    if not url:
        tkinter.messagebox.showerror("Error", "URL field is empty")
        return
    else:
        print(url)

        

    def check_price():
        read_url = urllib.request.urlopen(url).read()                           # Reading URL contents.
        parse = bs4.BeautifulSoup(read_url, 'html.parser')                      # Run through the html code of the web page.
        popp = parse.prettify()      
        # print(popp)                                                           # Prettify will indent the code which makes it look a lot better.  

        prices = parse.find('span', class_ = 'a-offscreen').get_text()          # Finding the price in HTML code.
        prices = float(prices.replace(",", "").replace("₹", ""))                # Converting the price(string) into float.
        title = parse.find('span', id="productTitle").get_text()                # Finding the title in HTML code.
        date = datetime.date.today()
        prices_list.append(prices)
        price_label = Label(top, text=prices, bg="black", fg="yellow")
        price_label.place(x=320,y=300)
        print(prices, title, date)
       
        
        


    def send_email(message):
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login('abinavtesting@gmail.com', 'pedehuczfozfeiwg')
        s.sendmail('abhinavtesting@gmail.com', 'abhinavgols@gmail.com', message)
        s.quit()
    def price_decrease(prices_list):
        if prices_list[-1] < prices_list[-2]:
            return True                             # The prices decrease
        else:
            return False                            # The prices did not decrease or went higher

    count = 1

    while True:

        current_price = check_price()
        if count > 1:
            flag = price_decrease(prices_list)
            if flag:
                decrease = prices_list[-1] - prices_list[-2]
                message = f"The price has decreased by ₹{decrease}"
                send_email(message)
        time.sleep(2)                                # Will wait n seconds to do the next step
        count = count + 1


    

b1 = Button(fg="red", text="ENTER", command=button_clicked, bg="black", foreground="yellow")
b1.place(x=258, y=305, height=35, width=120)


prices_list = []                                     # Storing the prices in this list.

# def show_new_window(prices):
#     new_window = Tk()
#     new_window.geometry("300x200")
#     new_window.title("New Window")

#     prod_name = Label(new_window, text=prices, font="Arial 15", bg="black", fg="yellow")
#     prod_name.place(x=10,y=30)

#     new_window.mainloop()


                  
#check_price()

top.mainloop()
