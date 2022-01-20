#!/usr/bin/env python
# coding: utf-8

from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from time import strftime, strptime

root = Tk()
root.title('Msg Box')
root['bg'] = 'white'  # Background

root.geometry('300x300')  # Largura x Altura


def clicked():
    global entry
    date = entry.get()
    weekday = strftime('%A', strptime(date, '%Y-%m-%d'))  # 2021-01-01
    messagebox.showinfo(title='Info', message='{} was um {}'.format(date, weekday))
    messagebox.showerror(title='Erro', message='Erro')
    messagebox.showwarning(title='Alerta', message='Alerta')


def show_msgbox():
    # messagebox.showwarning(title='Alerta', message='Alerta')
    messagebox.askyesno()
    # messagebox.askokcancel()
    # messagebox.askquestion()
    # messagebox.askretrycancel()
    # messagebox.askyesnocancel()


# Label
label = Label(root, text='Digite uma data: ')
label.pack()

# Entry
entry = Entry(root)
entry.pack()

# Botão
btn1 = Button(root, text='Clique', command=clicked)
btn1.pack()

# Label
lbl2 = Label(root, text='-----------------')
lbl2.pack()

# Botão
btn2 = Button(root, text='Clique', command=show_msgbox)
btn2.pack()

# Loop
root.mainloop()
