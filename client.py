PORT = 8050
SERVER = None
IP_ADDRESS = '127.0.0.1'
BUFFER_SIZE = 4096


import socket
from threading import Thread

from tkinter import *


def musicWindow():
    window=Tk()
    window.title('Music Window')
    window.geometry("300x300")
    window.config(bg='LightSkyBlue')

    selectlabel = Label(window, text="Select Song", bg="LightSkyBlue", font=("Calibri", 0))
    selectlabel.place(x=2, y=1)

    listbox = listbox(window, height = 10, width= 39, activestyle = "dotbox", bg="LightSkyBlue", borderwidth = 2, font=("Calibri", 10))
    listbox.place(x=10, y=10)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight= 1, relx=1)
    scrollbar1.config(command=listbox.yview)

    playButton = Button(window, text="Play", width=10, bd=1, bg="skyBlue", font=("Calibri", 10))
    playButton.place(x=30, y=200)

    stop = Button(window, text="Stop", width=10, bd=1, bg="skyBlue", font=("Calibri", 10))
    stop.place(x=200, y=200)

    Upload = Button(window, text="Upload", width=10, bd=1, bg="skyBlue", font=("Calibri", 10))
    Upload.place(x=30, y=250)

    Download = Button(window, text="Download", width=10, bd=1, bg='skyBlue', font= ("Calibri", 10))
    Download.place(x=200, y=250)

    infoLabel = Label(window, text="", fg="blue", font= ("Calibri", 10))
    infoLabel.place(x=4, y=280)

    window.mainloop()

def setup():

    from tkinter import ttk
    from tkinter import filedialog

    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()
setup()

