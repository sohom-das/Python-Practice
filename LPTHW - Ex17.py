from sys import *                                                   #importing function from the sys module
from os.path import *                                               #importing function from os.path module

script, from_file, to_file = argv                                   #get argv command line arguments (when executing the file) and assigning it three variables

in_file = open(from_file).read()                                    #Opening the file, from where data will be copied. And storing the data in a variable

print(f"The input file is {len(in_file)} bytes long")               #printing the length of the file
print(f"Does the file exists: {exists(to_file)}")                   #using the exists function, to chech whether the file exists or not.

out_file = open(to_file, 'w')                                       #opening destination file in write mode
out_file.write(in_file)                                             #coping all the data stored in the variable *data*

print("Alright all done!")
out_file.close()                                                    #finally, closing the file
