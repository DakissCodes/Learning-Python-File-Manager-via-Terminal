# use filter for file identification, ex. if file in list of directories. 

from msilib.schema import Class
import Classes
import os
import pdb
logic = Classes.directory()

while True:

    user_input = int(Classes.user_interface(0)) # displays user interface, asks for an input

    if user_input == 0: # exits the program
        break

    elif user_input == 1: # create a new folder

        file_name = input("Enter file name: ") # name of the folder

        

       
        while user_input != '0':

            in_home = True

            if os.getcwd() != 'C:\\Users\\ASUS': in_home = False # checks if in home directory


            path_list = logic.list_directory() # list of paths in current directory, and current directory paths

            user_input = Classes.create_file_input(in_home) 
            
            if user_input == '': # create file in current directory 

            
                os.mkdir(os.getcwd()) 

                print('\nFolder successfully created!')
                
                break

            if not in_home and user_input == '1':
                os.chdir('..')
                print('\nMoved back a directory!')

            else: # move directories

                if user_input in path_list: # change directory

                    
                    os.chdir(os.getcwd() + '\\' + user_input) # moves to a new directory (from user input)

                    print('\nDirectory has been changed!')

                else:
                    print('No such path!')


''' 
enter a file name, 
print list of directories (only folders), 
input directory name,
'''
'''use regex'''
