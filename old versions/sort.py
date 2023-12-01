# Open the file
with open("C:/Users/Investigator/Desktop/Graykey password extraction/output.txt", "r") as f:
    # Read the lines into a list
    lines = f.readlines()

# Sort the lines alphabetically
lines.sort()

# Write the sorted lines back to the file
with open("C:/Users/Investigator/Desktop/Graykey password extraction/output.txt", "w") as f:
    f.writelines(lines)