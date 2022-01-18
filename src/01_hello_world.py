#!/usr/bin/env python
# coding: utf-8

from tkinter import *

root = Tk()  # Create an instance of Tkinter Frame
root.geometry('700x350')  # Set the geometry
root.config(background='#aad5df')  # Set the default color of the window


def display_text():
    Label(
        root,
        text='Hello World!',
        background='white',
        foreground='purple1'
    ).pack()


Button(
    root,
    text='Click Me',
    background='white',
    foreground='black',
    font=('Helvetica 13 bold'),
    command=display_text
).pack(pady=50)

root.mainloop()
