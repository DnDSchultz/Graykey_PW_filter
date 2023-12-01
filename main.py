# This script is designed to extract Graykey password text file plain text passwords.
# You should make a copy of the Graykey password file and name it 'copy.txt'.
# Place the file in the 'Graykey password' folder on the desktop.
# There is an output.txt file in the same folder.
# That file will be overwritten with the passwords extracted.

__version__ = "1.2.0"
__Author__ = "Darrin Schultz, Badge #108 Eagan Police Department"
__Contact__ = "dschultz.ea@gmail.com"


import re
import os.path
from pathlib import Path
from tkinter import *
from tkinter import messagebox

def show_message():
    """
    This function uses the Tkinter library to create a pop-up window with
    information about placing a copy of the Graykey '*_passwords.txt' file
    in the specified folder and renaming it to 'copy.txt'
    """

    message = "Place a copy of the Graykey '*_passwords.txt' file in this folder and rename it 'copy.txt.'\n\nThis script is designed to filter out tokens and other garbage.\n\nFiltered results will be created (or overwirtten) in an 'output.txt' file."

    root = Tk()
    root.withdraw()
    messagebox.showinfo("Information", message)
    root.destroy()


def clicked():
    """
    Extract and filter passwords from the 'copy.txt' file.

    This function reads the 'copy.txt' file, filters out unwanted lines
    based on a regular expression, and writes the unique lines to the
    'output.txt' file.
    """

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
                if re.search("Item value:\ ((?!true|false|float|reinstall|male|female|done|sent|exists|event_sent|null|\(\d{3}\) \d{3}-\d{4}|\d{3}[-\.]?\d{3}[-\.]?\d{4}|\+\d{10}|\{.*\}).{4,15}$)", line):
                    line = line[12:]
                    if line not in unique_lines:
                        unique_lines.append(line)

        with open('C:/Users/Investigator/Desktop/Graykey password extraction/output.txt', 'w') as output:
            for line in unique_lines:
                output.write(line)


# Display the information message
show_message()

# Execute the password extraction and filtering
result = clicked()


# Exit the script
exit()
