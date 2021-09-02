from sys import *                                           #importing function from the sys module

script, filename = argv                                     #get argv command line arguments (when executing the file) and assigning it two variables

print(f"This is your file: {filename}")
print("If you don't want that, hit CTRL- C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')                                #Here we are opening the file in "write mode" and assigning it to a varialble

print("Now i am going to ask you for three line")

line1 = input("Line1: ")                                    #Taking input from user and assigning in the variables line 1, line 2 and line 3
line2 = input("Line2: ")
line3 = input("Line3: ")

target.write(f"{line1} \n{line2} \n{line3}")                #Writing the data from the user, into the chosen file

print("And finally, we close it")
target.close()                                              #And finally we close the file

target = open(filename)                                     #Again opening the file in normal read mode
print("This is the newly added txt: ")
print(target.read())                                        #printing the newly added txt in the file
target.close()                                              #again closing the file
