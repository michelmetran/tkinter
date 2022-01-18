#!/usr/bin/env python
# coding: utf-8


from tkinter import *
from tkinter import filedialog

# filename = filedialog.askopenfilename()
# print(filename)


root = Tk()  # Create an instance of Tkinter Frame
root.title('Ferramentas para TJSP e-SAJ')
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
    text='Selecionar Arquivo Zipado',
    background='white',
    foreground='black',
    font=('Helvetica 13 bold'),
    command=filedialog.askopenfilename()
).pack(pady=50)

root.mainloop()
