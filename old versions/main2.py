# This script is designed to extract Graykey password text file plain text passwords.
# You should make a copy of the Graykey password file and name it 'copy.txt'.
# Place the file in the 'Graykey password' folder on the desktop.
# There is an output.txt file in the same folder.
# That file will be overwritten with the passwords extracted.

import re
import os.path
from pathlib import Path
from tkinter import *
from tkinter import messagebox


def clicked():
    path_to_file = 'C:/Users/Investigator/Desktop/Graykey password extraction/output.txt'
    exist = os.path.exists(path_to_file)
    if exist == True:
        root = Tk()
        root.withdraw()
        answer = messagebox.askokcancel('Warning!', "'output.txt' exists.  Overwrite?")
        root.destroy()
        if answer == False:
            return
    if exist == False or answer == True:
        with open('C:/Users/Investigator/Desktop/Graykey password extraction/copy.txt', 'r') as f:
            lines = f.readlines()
            unique_lines = []
            for line in lines:
                if re.search("Item value:\ ((?!true|false|male|female|done|sent|exists|event_sent|null|\(\d{3}\) \d{3}-\d{4}|\d{3}[-\.]?\d{3}[-\.]?\d{4}|\+\d{10}|\{.*\}).{4,15}$)", line):
                    line = line[12:]
                    if line not in unique_lines:
                        unique_lines.append(line)
            unique_lines.sort()

        with open('C:/Users/Investigator/Desktop/Graykey password extraction/output.txt', 'w') as output:
            for line in unique_lines:
                output.write(line)

result = clicked()
exit()