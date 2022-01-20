#!/usr/bin/env python
# coding: utf-8


# https://www.youtube.com/watch?v=MK6e3Tj8dS4
# https://www.youtube.com/watch?v=ZS2_v_zsPTg


from tkinter import *


def sem_comando():
    Label(root, text='sssssss').pack()


def open_frame():
    hide_all_frames()
    novo_contato_frame.pack(fill='both', expand=1)
    Label(novo_contato_frame, text='sssssss').pack()


def open_frame_2():
    hide_all_frames()
    novo_contato_frame2.pack(fill='both', expand=1)
    Label(novo_contato_frame2, text='aaaaaaaaaaaaas').pack()


def hide_all_frames():
    novo_contato_frame.pack_forget()
    novo_contato_frame2.pack_forget()


root = Tk()
root.geometry('400x300')  # Set window size

# Cria uma Barra de Menus
my_menu = Menu(root)
root.config(menu=my_menu)

# Contatos
menu_contatos = Menu(my_menu, tearoff=0)
menu_contatos.add_command(label='Novo', command=open_frame)
menu_contatos.add_command(label='Pesquisar', command=open_frame_2)
menu_contatos.add_command(label='Deletar', command=sem_comando)
menu_contatos.add_separator()
menu_contatos.add_command(label='Fechar', command=root.quit)
my_menu.add_cascade(label='Contatos', menu=menu_contatos)

# Manutenção
menu_manutencao = Menu(my_menu, tearoff=0)
menu_manutencao.add_command(label='Novo', command=sem_comando)
menu_manutencao.add_command(label='Pesquisar', command=sem_comando)
menu_manutencao.add_command(label='Deletar', command=sem_comando)
my_menu.add_cascade(label='Manutenção', menu=menu_manutencao)

# Sobre
menu_sobre = Menu(my_menu, tearoff=0)
menu_sobre.add_command(label='Novo', command=sem_comando)
menu_sobre.add_command(label='Pesquisar', command=sem_comando)
menu_sobre.add_command(label='Deletar', command=sem_comando)
my_menu.add_cascade(label='Sobre', menu=menu_sobre)

# Create Frames
novo_contato_frame = Frame(root, width=400, height=300, bg='red')
novo_contato_frame2 = Frame(root, width=400, height=300, bg='blue')

# Loop
root.mainloop()
