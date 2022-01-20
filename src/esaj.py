#!/usr/bin/env python
# coding: utf-8

import os
from tkinter import *
from tkinter import filedialog

# Main
root = Tk()
root.title('TJSP: Juntar Documentos e-SAJ')
width = 500
height = 300
root.geometry('{}x{}'.format(width, height))


def merge_file():
    temp_path = lbl_temp['text']
    zipfile_path = lbl_zip['text']
    print('Label 5: {}'.format(temp_path))
    print('Label 7: {}'.format(zipfile_path))
    print(os.path.isfile(zipfile_path))
    print(os.path.isdir(temp_path))


def select_zip_file():
    """
    Function for opening the file explorer window
    """
    filename = filedialog.askopenfilename(
        initialdir='/',
        title='Selecionar arquivo zipado (.zip)',
        filetypes=(('Zip files', '*.zip'), ('All files', '*.*'))
    )
    lbl_zip.configure(text='Arquivo Selecionado: {}'.format(filename))


def select_temp_path():
    """
    Function for opening the file explorer window
    """
    folder_path = StringVar()
    folder_selected = filedialog.askdirectory(
        initialdir='/',
        title='Selecionar Diretório'
    )
    folder_path.set(folder_selected)
    lbl_temp['text'] = folder_path.get()


def hide_all_frames():
    """
    Function for opening the file explorer window
    """
    app_frame.grid_forget()
    about_frame.grid_forget()

    app_frame.pack_forget()
    about_frame.pack_forget()

    for widget in about_frame.winfo_children():
        widget.destroy()
    for widget in app_frame.winfo_children():
        widget.destroy()


def open_app_frame():
    global lbl_temp
    global lbl_zip
    hide_all_frames()

    # Create Frames
    app_frame.config(background='blue')
    app_frame.grid(row=0, column=0)
    app_frame.grid(sticky='nsew')

    # Button/Label: File Explorer
    btn_file = Button(app_frame, text='Selecionar arquivo .zip', height=2, command=select_zip_file)
    btn_file.grid(row=0, column=0, padx=10, pady=10)
    btn_file.grid(sticky='w')
    lbl_zip = Label(app_frame, text='Arquivo Selecionado: None')
    lbl_zip.config(background='green', foreground='blue')
    lbl_zip.config(height=2)
    lbl_zip.grid(row=0, column=1, padx=10, pady=10)
    lbl_zip.grid(sticky='w')

    # Button/Label: Select Path
    btn_temp = Button(app_frame, text='Selecionar Pasta', height=2, command=select_temp_path)
    btn_temp.grid(row=1, column=0, padx=10, pady=10)
    btn_temp.grid(sticky='w')
    lbl_temp = Label(app_frame, text='Pasta Selecionada: None')
    lbl_temp.config(background='white', foreground='black')
    lbl_temp.config(height=2)
    lbl_temp.grid(row=1, column=1, padx=10, pady=10)
    lbl_temp.grid(sticky='w')

    # Button
    btn_final = Button(app_frame, text='Converter .zip com pdfs individualizados ', height=2, command=merge_file)
    btn_final.grid(row=2, columnspan=2, padx=10, pady=10)
    btn_final.grid(sticky='s')


def open_about_frame():
    hide_all_frames()

    # Frame
    about_frame.pack(fill='both', expand=1)
    about_frame.config(background='red')

    # Add Label
    texto = """
    Programa escrito por Michel Metran,
    Biólogo, Assessor do MPSP.        
    """
    lbl_1 = Label(about_frame, text=texto)
    lbl_1.config(background='blue', foreground='black')
    lbl_1.pack()


# Frames
app_frame = Frame(root, width=width, height=height)
about_frame = Frame(root, width=width, height=height)

# Menu
my_menu = Menu(root)
root.config(menu=my_menu)
my_menu.add_command(label='Aplicação', command=open_app_frame)
my_menu.add_command(label='Sobre', command=open_about_frame)

# Grid
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Loop
open_app_frame()
root.mainloop()
