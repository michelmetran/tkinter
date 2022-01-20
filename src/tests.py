#!/usr/bin/env python
# coding: utf-8


# https://www.youtube.com/watch?v=MK6e3Tj8dS4
# https://www.youtube.com/watch?v=ZS2_v_zsPTg


from tkinter import *

frame = tk.Frame(...)
l1 = tk.Label(frame, ...)
l2 = tk.Label(frame, ...)
l1.grid(row=0, column=0, sticky="nsew")
l2.grid(row=1, column=1, stickky="nsew")
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Loop
frame.mainloop()
