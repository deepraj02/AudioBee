import tkinter
import pygame
import tkinter.messagebox as tmsg
import pyfiglet
import mysql.connector
from ttkthemes import themed_tk as t
from tkinter import ttk
from tkinter import filedialog as fd


def OpenFile():
    filetypes = (
        ('PDF files', '*.pdf'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir=r'C:\Users\deepr\Desktop',
        filetypes=filetypes)


root = t.ThemedTk(theme="radiance")
root.title("AudioBee")


root.geometry("480x650")
root.minsize(480, 650)
root.maxsize(480, 650)
root.configure(background='#2C3335')
root.wm_iconbitmap(r"icon.ico")

s = ttk.Style().configure('my.TButton', font="firacode 14")

ttk.Button(root, text="Choose", style="my.TButton",
           command=OpenFile, width=7).pack(padx=5, pady=10,expand=True)

root.mainloop()