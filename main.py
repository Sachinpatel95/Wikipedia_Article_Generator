import requests
import webbrowser
from bs4 import BeautifulSoup
from tkinter import *

# A function that takes a link and opens it in the users preferred browser

def callback(url):
    webbrowser.open_new(url)

# A function called when the GENERATE NEW ARTICLE button is pressed.
# The function gets a random Wikipedia article and uses that article to create a hyperlink for the user

def get_article(link):
    random_link = "https://en.wikipedia.org/wiki/Special:Random"
    new_link = "https://en.wikipedia.org/wiki/"
    page = requests.get(random_link)
    soup = BeautifulSoup(page.content, 'html.parser')
    name = soup.find(id="firstHeading").text.strip()
    new_link += name.replace(" ", "_")
    link.configure(text="\n"+name, fg="blue", font=("Verdana 20 underline"))
    link.bind("<Button-1>", lambda e: callback(new_link))

# This code sets up the GUI for the app

window = Tk()
the_canvas = Canvas(window, width=500, height=240, highlightthickness=0, bg="orange")
the_canvas.create_oval(0, 0, 500, 207, fill="white", outline="")
the_canvas.create_rectangle(0, 0, 30, 240, fill="blue", outline="")
the_canvas.create_rectangle(30, 0, 35, 240, fill="orange", outline="")
the_canvas.create_rectangle(470, 0, 500, 240, fill="blue", outline="")
the_canvas.create_rectangle(465, 0, 470, 240, fill="orange", outline="")
the_canvas.place(x=0, y=0)
window.title("Wikipedia Article Generator")
window.resizable(False, False)
window.geometry("500x240")
generate_article = Button(text="GENERATE NEW ARTICLE", font=(
    "Verdana", 20), pady=0, command=lambda: get_article(link), borderwidth=10, bg="white")
generate_article.pack(side=BOTTOM)
title = Label(text="Wikipedia Article Generator", font=(
    "Verdana", 20), justify=CENTER, bg="white")
title.pack(side=TOP)
link = Label(text="\nClick GENERATE to get a link to a random Wikipedia article", font=(
    "Verdana", 20), justify=CENTER, wraplength=400, bg="white")
link.pack(side=TOP)
window.mainloop()