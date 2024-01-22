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

with open(file_path, newline='', encoding='utf-8') as csvfile:
    lifelistreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in lifelistreader:
        if i == 0:
            aooutput = 'Artsnavn	Lokalitetsnavn	Fra dato	Fra klokkeslett	Antall	Kjønn	Aktivitet	Kommentar (synlig for alle)'
        else:
            # Artsnavn
            aooutput += row[0]
            # Lokalitetsnavn
            aooutput += '\t' + row[4]
            # Fra dato
            if row[2] == "":
                aooutput += '\t'    
            else:
                aooutput += '\t' + row[2][8:10] + '.' + row[2][5:7] + '.' + row[2][0:4]
            # Fra klokkeslett
            aooutput += '\t' + row[3][0:5]
            # Antall
            aooutput += '\t' + row[7]
            
            # Notes
            notes = row[8].split("/")
            
            if len(notes) > 0:
                # Kjønn
                aooutput += '\t' + notes[0]

            if len(notes) > 1:
                # Aktivitet
                aooutput += '\t' + notes[1]

            if len(notes) > 2:
                # Kommentar (synlig for alle)
                aooutput += '\t' + notes[2]


        aooutput += '\n'
        i +=1
        
pc.copy(aooutput)

messagebox.showinfo("showinfo", 'Converted ' + str(i-1) + ' records.\nResult copied to clipboard.')


