"""Importing Modules"""

import tkinter
import bs4                              # Contains functions to fetch information (price of product) from the internet.
import urllib.request                   # It will help to open up a web page.
import smtplib                          # For mail sending
import time
import datetime
import sys
import csv
from tkinter import *
from tkinter import PhotoImage
from tkinter import ttk
from tkinter.messagebox import *
from random import randint
from PIL import Image
import matplotlib.pyplot as plt


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
top.geometry("800x500")

top.minsize(800, 500)
top.maxsize(800, 500)
top.title("Web Scraping")

colour='#e8de87'

def update():
    #color="%05x" %randint(0,0xFFFFFF)
    #top.config(background ='#000000' + colour)
    top.config(background=colour,highlightthickness='2')
    #top.after(1000, update)
    # top.iconbitmap('setimage\\index.ico')

def desired_screen():
    root=Tk()
    root.configure(background='light cyan')
    root.geometry('600x400')
    root.title('Your Desired Price is Matched')
    #root.resizable(False,False)
    root.iconbitmap('index.ico')
    
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


#update()
top.config(background=colour,highlightthickness='2')
# top.iconbitmap('index.ico')



# image = PhotoImage(file='black.png')
# label = Label(top, image=image)
# label.place(x=0, y=0, relwidth=1, relheight=1)



##title = Label(top, text="PRICE SCRAPER", font="comicsansms 30 bold underline", bg="black", fg="yellow")
title=Label(top, text='Price Scraper', font=('Calibri', '40', 'bold', 'underline'),bg=colour, fg='red')
title.place(x=275, y=10)


input_url = Label(top, text="ENTER THE URL", font="Calibri 15",bg=colour, fg="blue")
input_url.place(x=340, y=100)

input_url_value = StringVar()

url_entry = Entry(top, textvariable=input_url_value, bg="white", fg="black", borderwidth=6, relief=SUNKEN)
url_entry.place(x=150, y=140, height=25, width=500)

desire_price = Label(top, text="ENTER THE DESIRED PRICE ", font="Calibri 15",bg=colour, fg="blue")
desire_price.place(x=290, y=200)

input_desire_price = StringVar()

inp_dp = Entry(top, textvariable=input_desire_price, bg="white", fg="black", borderwidth=6, relief=SUNKEN)
inp_dp.place(x=300, y=240, height=25, width=200)

input_email = Label(top, text="ENTER YOUR EMAIL ADDRESS", font="Calibri 15",bg=colour, fg="blue")
input_email.place(x=300, y=300)

input_email_value = StringVar()

email_entry = Entry(top, textvariable=input_email_value, bg="white", fg="black", borderwidth=6, relief=SUNKEN)
email_entry.place(x=150, y=340, height=25, width=500)




def button_clicked():
    url = url_entry.get()
    if not url:
        tkinter.messagebox.showerror("Error", "URL field is empty")
        return  
    else:
        print(url)

    tkinter.messagebox.showinfo("Message","Your desired price is recorded. You will get notified when price will drop")

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
        #price_label = Label(top, text=prices, bg="black", fg="yellow")
        #price_label.place(x=320,y=300)
        print(prices, title, date)
        with open('prices.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Title', 'Price', 'Date'])
            writer.writerow([title, prices, date])
       
    def plot():
        # Plot a scatter graph of the prices in the CSV file
        with open('prices.csv', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            next(plots)  # Skip the header row
            x = []
            y = []
            for row in plots:
                x.append(row[2])
                y.append(row[1])
        plt.scatter(x, y)
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Price Scatter Plot')
        plt.show()      
        
        


    def send_email(message):
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login('abhinavtesting@gmail.com', 'pedehuczfozfeiwg')
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
        time.sleep(5)                                # Will wait n seconds to do the next step
        count = count + 1


    

b1 = Button(fg="red", text="ENTER", command=button_clicked, bg="black", foreground="yellow")
b1.place(x=320, y=400, height=35, width=160)


prices_list = []                                     # Storing the prices in this list.

top.mainloop()