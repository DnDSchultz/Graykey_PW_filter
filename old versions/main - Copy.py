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
        return answer
    else:
        if exist == False:
            output = open('C:/Users/Investigator/Desktop/Graykey password extraction/output.txt', 'w')
            with open('C:/Users/Investigator/Desktop/Graykey password extraction/copy.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if re.search("Item value:\ ((?!true|false).{4,15}$)", line):
                        output.write(line[12:])

            output.close()


result = clicked()

if result == True:
    output = open('C:/Users/Investigator/Desktop/Graykey password extraction/output.txt', 'w')
    with open('C:/Users/Investigator/Desktop/Graykey password extraction/copy.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if re.search("Item value:\ ((?!true|false).{4,15}$)", line):
                output.write(line[12:])

    output.close()
else:
    exit()
