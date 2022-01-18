#!/usr/bin/env python
# coding: utf-8


from tkinter import *
from tkinter import filedialog
from time import strftime, localtime


# --------------------------------------------
def browse_files():
    """
    # Function for opening the file explorer window
    :return:
    """
    filename = filedialog.askopenfilename(
        initialdir='/',
        title='Selecionar arquivo zipado (.zip)',
        filetypes=(('Zip files', '*.zip*'), ('All files', '*.*'))
    )


root = Tk()  # Create the root window
# root.withdraw()
root.title('Título da Janela')  # Set window title
# root.geometry('700x350')  # Set window size
root.config(background='white')  # Set window background color

# --------------------------------------------

# Label
label_1 = Label(root, text='Label 1')
label_1.config(bg='blue', fg='black')
label_1.grid(row=1, column=1, rowspan=2, padx=10, pady=10)

# Label
label_2 = Label(root, text='Label 2')
label_2.config(bg='red', fg='black')
label_2.grid(row=2, column=2, padx=10, pady=10)


# --------------------------------------------

# Function
def get_time():
    time = strftime('Day: %d.%m.%Y\nTime: %H:%M:%S\n', localtime())
    label_3['text'] = time


# Button
btn_01 = Button(root, text='Pegar Dia/Hora', height=3, command=get_time)
btn_01.grid(
    row=3,
    column=1,
    padx=10,
    pady=10
)

# Label
label_3 = Label(root, text='Irá ter a data/hora (Label 3)')
label_3.config(bg='white', fg='black')
label_3.grid(
    row=3,
    column=2,
    padx=10,
    pady=10
)

# --------------------------------------------

# Label
label_4 = Label(root, text='---------- Label 4 ----------')
label_4.config(bg='white', fg='black')
label_4.grid(
    row=4,
    # column=1,
    # rowspan=3,
    columnspan=3,
)


# --------------------------------------------


def get_folder_path():
    folder_path = StringVar()
    folder_selected = filedialog.askdirectory(
        initialdir='/',
        title='Selecionar Diretório'
    )
    folder_path.set(folder_selected)
    label_5['text'] = folder_path.get()


# Botão
Button(
    root,
    text='Selecionar Pasta',
    height=3,
    command=get_folder_path,
).grid(row=5, column=1, padx=10, pady=10)

# print(folder_path)

# Label
label_5 = Label(root, text='Irá ter a data/hora (Label 5)')
label_5.config(bg='white', fg='black')
label_5.grid(
    row=5,
    column=2,
    padx=10,
    pady=10
)

# Loop
root.mainloop()
