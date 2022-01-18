#!/usr/bin/env python
# coding: utf-8


from tkinter import *
from tkinter import filedialog
from tkinter import ttk


root = Tk()  # Create the root window
root.title('Ferramentas para TJSP e-SAJ')  # Set window title
root.geometry('700x350')  # Set window size
root.config(background='white')  # Set window background color


def get_folder_path():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)


# Function for opening the file explorer window
def browse_files():
    filename = filedialog.askopenfilename(
        initialdir='/',
        title='Selecionar arquivo zipado (.zip)',
        filetypes=(('Zip files', '*.zip*'), ('All files', '*.*'))
    )

    # Change label contents
    label_file_explorer.configure(text='File Opened: {}'.format(filename))
    # print(filename)
    #return filename


# Create a File Explorer label
label_file_explorer = Label(
    root,
    text='File Explorer using Tkinter',
    width=100,
    height=4,
    fg='blue',
)
label_file_explorer.grid(column=1, row=1)

# Botão
Button(
    root,
    text='Selecionar arquivo Zipado',
    height=4,
    command=browse_files,
).grid(column=1, row=2)

# Exit
Button(
    root,
    text='Exit',
    command=exit
).grid(column=1, row=3)

# dddd
folder_path = StringVar()
Label(
    root,
    text='ddddd',
    width=100,
    height=4,
).grid(column=1, row=5)

# ffffff
Entry(
    root,
    textvariable=folder_path,
).grid(column=1, row=6)

#
ttk.Button(
    root,
    text='Browse Folder',
    command=get_folder_path,
).grid(column=1, row=7)

print(folder_path)

# Let the window wait for any events
root.mainloop()
