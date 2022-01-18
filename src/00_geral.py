#!/usr/bin/env python
# coding: utf-8


from tkinter import *
from tkinter import filedialog
from time import strftime, localtime

# --------------------------------------------

root = Tk()  # Create the root window
# root.withdraw()
root.title('Título da Janela')  # Set window title
# root.geometry('700x350')  # Set window size
# root.geometry('300x300+100+100')  # Largura x Altura + Distância da Esq + Distância do Topo
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

# Label
label_5 = Label(root, text='Irá ter a data/hora (Label 5)')
label_5.config(bg='white', fg='black')
label_5.grid(
    row=5,
    column=2,
    padx=10,
    pady=10
)

# --------------------------------------------

# Label
label_6 = Label(root, text='---------- Label 6 ----------')
label_6.config(bg='white', fg='black')
label_6.grid(
    row=6,
    # column=1,
    # rowspan=3,
    columnspan=3,
)


# --------------------------------------------

def browse_files():
    """
    # Function for opening the file explorer window
    :return:
    """
    filename = filedialog.askopenfilename(
        initialdir='/',
        title='Selecionar arquivo zipado (.zip)',
        filetypes=(('Zip files', '*.zip'), ('All files', '*.*'))
    )
    # Change label contents
    label_7.configure(text='File Opened: {}'.format(filename))


# Button
Button(
    root,
    text='Selecionar Arquivo',
    height=2,
    command=browse_files,
    font=('Helvetica 13 bold'),
).grid(row=7, column=1, padx=10, pady=10)

# Create a File Explorer label
label_7 = Label(
    root,
    text='File Explorer using Tkinter',
    # width=100,
    background='green',
    foreground='blue',
    height=2,
)
label_7.grid(row=7, column=2, padx=10, pady=10)

# Exit
btn_exit = Button(
    root,
    text='Exit',
    command=exit
)
btn_exit.grid(
    row=10,
    # column=1,
    columnspan=3,
    padx=10,
    pady=10
)



# Loop
root.mainloop()
