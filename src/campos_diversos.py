#!/usr/bin/env python
# coding: utf-8


from tkinter import *
from tkinter import Tk
from tkinter.messagebox import showinfo
from time import strftime, localtime

root = Tk()

def clicked():
    time = strftime('Day: %d.%m.%Y\nTime: %H:%M:%S\n', localtime())
    showinfo(message=time)


def btn_click():
    print('Botão clicado')
    btn_text['text'] = 'Puta Merda. Cliquei!'


# User Mail
user_email = Label(root, text='Insira seu nome aqui:')
user_email.pack()
user_email.config(bg='white', fg='black')
user_email = Entry(root, bd=2)
user_email.pack(fill=X)

# Add photo
photo = PhotoImage(file='../data/giphy.gif').subsample(5)
hello = Label(master=root, image=photo, width=300, height=180)
hello.pack(side=BOTTOM)

# Receiver e-mail
receiver_email = Label(root, text='Insira seu e-mail aqui:', font=('Arial', 16))
receiver_email.pack()
receiver_email.config(bg='white', fg='black')
receiver_email = Entry(root, bd=2)
receiver_email.pack(fill=X)

# Receiver e-mail
# btn = Button(root, text='Ok', command=btn_click)
btn = Button(root, text='Ok', command=clicked)
btn.pack()
btn_text = Label(root, text='Não clicado inicialmente')
btn_text.pack()

#
usermail = user_email.get()
print(usermail)

# Loop
root.mainloop()
