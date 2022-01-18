#!/usr/bin/env python
# coding: utf-8

from tkinter import ttk

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

