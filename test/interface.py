import tkinter as tk
import csv
import cv2
import os
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time

window = tk.Tk()
window.title("STUDENT ATTENDANCE USING FACE RECOGNITION SYSTEM")
window.geometry('800x500')

dialog_title = 'QUIT'
dialog_text = "are you sure?"
window.configure(background='green')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)


def clear():
    std_name.delete(0, 'end')
    res = ""
    label4.configure(text=res)


def clear2():
    std_number.delete(0, 'end')
    res = ""
    label4.configure(text=res)


label1 = tk.Label(window, background="green", fg="black", text="Name :", width=10, height=1,
                  font=('Helvetica', 16))
label1.place(x=83, y=40)
std_name = tk.Entry(window, background="yellow", fg="black", width=25, font=('Helvetica', 14))
std_name.place(x=280, y=41)
label2 = tk.Label(window, background="green", fg="black", text="Matric Number :", width=14, height=1,
                  font=('Helvetica', 16))
label2.place(x=100, y=90)
std_number = tk.Entry(window, background="yellow", fg="black", width=25, font=('Helvetica', 14))
std_number.place(x=280, y=91)

clearBtn1 = tk.Button(window, background="red", command=clear, fg="white", text="CLEAR", width=8, height=1,
                      activebackground="red", font=('Helvetica', 10))
clearBtn1.place(x=580, y=42)
clearBtn2 = tk.Button(window, background="red", command=clear2, fg="white", text="CLEAR", width=8,
                      activebackground="red", height=1, font=('Helvetica', 10))
clearBtn2.place(x=580, y=92)

label3 = tk.Label(window, background="green", fg="red", text="Notification", width=10, height=1,
                  font=('Helvetica', 20, 'underline'))
label3.place(x=320, y=155)
label4 = tk.Label(window, background="yellow", fg="black", width=55, height=4, font=('Helvetica', 14, 'italic'))
label4.place(x=95, y=205)

takeImageBtn = tk.Button(window, command=takeImage, background="yellow", fg="black", text="CAPTURE IMAGE",
                         activebackground="red",
                         width=15, height=3, font=('Helvetica', 12))
takeImageBtn.place(x=130, y=360)
trainImageBtn = tk.Button(window, command=trainImage, background="yellow", fg="black", text="TRAINED IMAGE",
                          activebackground="red",
                          width=15, height=3, font=('Helvetica', 12))
trainImageBtn.place(x=340, y=360)
trackImageBtn = tk.Button(window, command=trackImage, background="yellow", fg="black", text="TRACK IMAGE", width=12,
                          activebackground="red", height=3, font=('Helvetica', 12))
trackImageBtn.place(x=550, y=360)

window.mainloop()
