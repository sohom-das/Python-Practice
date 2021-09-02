from sys import *                           #importing function from the sys module

script, filename = argv                     #get argv command line arguments (when executing the file) and assigning it two variables

txt = open(filename)                        #Here we are opening the file and assigning it to a varialble
print(f"Here is your file: {filename}")
print(txt.read())                           #This read command is used to read the file and, we used print to display the txt

txt.close()                                 #Close the file
