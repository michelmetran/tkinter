#!/usr/bin/env python
# coding: utf-8


from tkinter import *
from tkinter import Tk
from tkinter.messagebox import showinfo
from time import strftime, strptime

root = Tk()
root.title('Calculadora')
root['bg'] = 'white'  # Background

root.geometry('300x300')  # Largura x Altura


def clicked():
    global entry
    date = entry.get()
    weekday = strftime('%A', strptime(date, '%Y-%m-%d'))  # 2021-01-01
    showinfo(message='{} was um {}'.format(date, weekday))


# Label
label = Label(root, text='Digite uma data:')
label.grid(row=0, column=0)

# Entry
entry = Entry(root)
entry.grid(row=0, column=1)

# Botão
btn = Button(root, text='Clique', command=clicked)
btn.grid(row=1, column=0, columnspan=2)


# Loop
root.mainloop()
