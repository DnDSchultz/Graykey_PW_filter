# Graykey Password Extraction Script

This Python script is designed to extract and filter passwords from a Graykey password text file.

## Usage

1. Place a copy of the Graykey '*_passwords.txt' file in the same folder as this script.
2. Rename the copied '*_passwords.txt' file to 'copy.txt'.
3. Simply double click the 'Run_Python.bat' file to run the script and follow the prompts.  It will filter out unwanted lines
   and create/overwrite an 'output.txt' file with the extracted passwords.

## Warning

If 'output.txt' already exists in the same folder, the script will prompt you to confirm overwriting.

## Dependencies

- Python 3.x
- Tkinter library (included with most Python installations, no separate installation needed)

## Notes

- This script filters out lines based on a regular expression pattern.
- Filtered results are stored in the 'output.txt' file.
