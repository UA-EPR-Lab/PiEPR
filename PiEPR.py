# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 09:54:31 2019

@author: Student
"""

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from tkinter import filedialog

from Spectrum_Parent_Class import Spectrum

# Executed Code
def choose_files():

    """choose files from file dialog box;
    displays Bruker .DTA files"""

    root = tk.Tk()
    root.withdraw()
    filenamelist = filedialog.askopenfilenames(
        parent=root,
        defaultextension='.DTA',
        title="Select Data files",
        filetypes=[('Bruker', '.DTA'), ('all', '.*')])
    return filenamelist

FILENAMELIST = choose_files()
THE_SPECTRUM = list()

for j in range(0, len(FILENAMELIST)):
    THE_SPECTRUM.append(Spectrum(FILENAMELIST[j]))

    if THE_SPECTRUM[j].spec_type == "ENDOR":
        THE_SPECTRUM[j].lineplot()
        THE_SPECTRUM[j].write_txt()

    elif THE_SPECTRUM[j].spec_type == "HYSCORE":
        THE_SPECTRUM[j].contour_plot()
        THE_SPECTRUM[j].write_txt()