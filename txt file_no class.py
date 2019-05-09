# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 05:47:13 2019

@author: Joe Butler
"""
import numpy as np
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog



root = tk.Tk()
root.withdraw()
filenamelist = filedialog.askopenfilenames(
    parent=root,
    defaultextension='.txt',
    title="Select Data files",
    filetypes=[('Bruker', '.txt'), ('all', '.*')])

txt = []
with open(filenamelist[0]) as txt_file:
    for line in txt_file:
        txt.append(line.rstrip().split())
        
RF = np.zeros((1024))
Amp = np.zeros((1024))
for i in range (len(txt) - 1024, len(txt)):
    RF[i-2] = np.float(txt[i][1])
    Amp[i -2] = np.float(txt[i][2])
    
try:
    application_window = tk.Tk()
    application_window.withdraw()
    mag_field = simpledialog.askfloat("Magnetic Field",
                                       """ Enter Magnetic Field in Gauss""", parent=application_window)
except:
    mag_field = 3494
    application_window = tk.Tk()
    application_window.withdraw()
    simpledialog.messagebox.showerror("Field Input Error",
                                                      """Invalid Field Input detected. 
                Default 3494 Selected""", parent = application_window)
try:        
    application_window = tk.Tk()
    application_window.withdraw()
    freq = simpledialog.askfloat("Frequency",
                                       """ Enter Frequency in GHz""", parent=application_window)
except:
    freq = 9.78
    application_window = tk.Tk()
    application_window.withdraw()
    simpledialog.messagebox.showerror("Frequency Input Error",
                                                      """Invalid Frequency Input detected. 
                Default 9.78 Selected""", parent = application_window)