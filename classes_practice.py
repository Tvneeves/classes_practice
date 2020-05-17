'''
1. Your program this week will use the OS library
2. Your program will prompt the user for:
	-the directory they would like to save the file in,
	-the name of the file, 
3. Validate that a directory exists,
4. Create a file in that directory,
5. The program should then prompt the user for thier: 
	-name, 
	-address, 
	-phone number.  
6. The program will write this data to a comma separated line in a file.
7. Store the file in the directory specified by the user. 
8. Read the file you just wrote to the file system .
9. Display the file contents to the user for validation purposes. 
'''

#imports the os module, pathlib module, and retieves Path from pathlib
import os 
import pathlib
from pathlib import Path

#prompts user for desired directory path
prompted_direc = input("Please Enter Directory Path of Where you would like to save your file. ") 

#checks if path is valid and returns true/false
os.path.isdir(prompted_direc)

#if path is invalid, prints to user that it does not exist
if os.path.isdir(prompted_direc) == False:
	print("Directory Does Not Exist.")

#if path is valid prints that directory was found and saves direc
if os.path.isdir(prompted_direc) == True:
	print("Directory Found.")

#creates a new file with user imputed filename, there probably should be a check here to ensure that they enter in correct format	
new_file = input("Please Enter new File name in format:'File_Name.txt' ")

#prompts user for their name, address, and phonenumber and writes it to the new file.
#this is a silly way to add the commas, without relying on the user to input them themself.
#but it was the only way I could figure out, im sure there is a better/more efficient way to have done this.
#maybe if I store the data in a list, and then write the list to the file?

with open(os.path.join(prompted_direc,new_file), 'w+') as fp:
	fp.write(input('Please enter your name. '))
	fp.write(', ')
	fp.write(input('Please enter your address. '))
	fp.write(', ')
	fp.write(input('Please enter your phonenumber. '))

#Reads the new file back to the user for validation.
p = Path(prompted_direc)
for file in p.iterdir():
	print(file.read_text())





