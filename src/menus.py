#!/usr/bin/env python
# coding: utf-8


# https://www.youtube.com/watch?v=MK6e3Tj8dS4

from tkinter import *


def sem_comando():
    print('')


root = Tk()

# Cria uma Barra de Menus
menu_bar = Menu(root)

# Contatos
menu_contatos = Menu(menu_bar, tearoff=0)
menu_contatos.add_command(label='Novo', command=sem_comando)
menu_contatos.add_command(label='Pesquisar', command=sem_comando)
menu_contatos.add_command(label='Deletar', command=sem_comando)
menu_contatos.add_separator()
menu_contatos.add_command(label='Fechar', command=root.quit)
menu_bar.add_cascade(label='Contatos', menu=menu_contatos)

# Manutenção
menu_manutencao = Menu(menu_bar, tearoff=0)
menu_manutencao.add_command(label='Novo', command=sem_comando)
menu_manutencao.add_command(label='Pesquisar', command=sem_comando)
menu_manutencao.add_command(label='Deletar', command=sem_comando)
menu_bar.add_cascade(label='Manutenção', menu=menu_manutencao)

# Sobre
menu_sobre = Menu(menu_bar, tearoff=0)
menu_sobre.add_command(label='Novo', command=sem_comando)
menu_sobre.add_command(label='Pesquisar', command=sem_comando)
menu_sobre.add_command(label='Deletar', command=sem_comando)
menu_bar.add_cascade(label='Sobre', menu=menu_sobre)

root.config(menu=menu_bar)
root.mainloop()
