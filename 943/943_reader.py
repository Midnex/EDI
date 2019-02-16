# seriously nothing to see here yet. Just opens a file and does nothing. 

import csv, tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

reader = csv.DictReader(open('file_path'))
