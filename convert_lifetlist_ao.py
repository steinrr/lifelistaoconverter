import csv
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import platform
import pyperclip as pc

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

aooutput = ''
i = 0

with open(file_path, newline='') as csvfile:
    lifelistreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in lifelistreader:
        if i == 0:
            aooutput = 'Artsnavn	Lokalitetsnavn	Fra dato	Fra klokkeslett	Antall	Kjønn'
        else:
            # Artsnavn
            aooutput += row[0]
            # Lokalitetsnavn
            aooutput += '\t' + row[4]
            # Fra dato
            aooutput += '\t' + row[2][8:10] + '.' + row[2][5:7] + '.' + row[2][0:4]
            # Fra klokkeslett
            aooutput += '\t' + row[3][0:5]
            # Antall
            aooutput += '\t' + row[7]
            # Kjønn
            aooutput += '\t' + row[8]
            
        aooutput += '\n'
        i +=1
        

pc.copy(aooutput)

messagebox.showinfo("showinfo", 'Converted ' + str(i) + ' records.\nResult copied to clipboard.')


