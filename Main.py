# use filter for file identification, ex. if file in list of directories. 


import Classes
import os
import pdb
import shutil


logic = Classes.directory()

while True:

    user_input = int(Classes.user_interface(0)) # displays user interface, asks for an input

    if user_input == 0: # exits the program
        break

    elif user_input == 1: # create a new folder

        file_name = input("Enter file name: ") # name of the folder

        
        max = 5
        min = 0      
        
        while user_input != '0':

            in_home = True

            if os.getcwd() != 'C:\\Users\\ASUS': in_home = False # checks if in home directory


            path_list = logic.list_directory(True) # list of paths in current directory, and current directory paths
            # path list is the list of folders/files in a directory! 

            if len(path_list) <= 5:
                for element in path_list[::]: print('\n' + element)


            else:

                if len(path_list[min:max]) == 0: 
                    print('\nNo more items! ')
                    max -= 5
                    min -= 5
        
                for element in path_list[min:max]: print('\n' + element)



            user_input = Classes.create_file_input(in_home) # edit this!
            
            if user_input == '': # create file in current directory 
                

                os.mkdir(os.path.join(os.getcwd(),file_name)) # creates the directory 

                print('\nFolder successfully created!')
                
                break

            if user_input.upper() == 'B':

                if in_home:
                    print("\nAlready in home directory!")

                elif not in_home:
                    os.chdir('..')
                    print('\nMoved back a directory!')
                    max = 5
                    min = 0  

            elif user_input.upper() == 'N':
                max += 5
                min += 5

            elif user_input.upper() == 'P': 

                if max == 5 and min == 0:

                    print('\nAlready in first page!')

                else:

                    max -= 5
                    min -= 5
            
            elif user_input.upper() == 'C': 

                while True:

                    user_input = input('\nEnter path name here: ')

                    if user_input in path_list: # change directory

                        
                        os.chdir(os.getcwd() + '\\' + user_input) # moves to a new directory (from user input)

                        print('\nDirectory has been changed!')

                        max = 5
                        min = 0  
                        break

                    else:

                        print('\nNo such path!')                

        os.chdir('C:\\Users\\ASUS')

    elif user_input == 2: # move folders/file

        file_list = [] # files to move 

        while True:


            print('Current Directory: ' + os.getcwd())

            print(file_list) # shows files to move

            user_input = Classes.move_interface() # user interface

            if user_input == 0:
                break

            elif user_input == 1: # choose files in current directory
                

                
                while True: # while user does not input 0
                    
                    path_list = logic.list_directory(False) # displays all files and folders

                    

                    user = input('\n[0] Exit\nEnter file name: ')

                    if user == '0': 
                        break
                    
                    elif user in path_list: 
                        file_list.append(user)
                        print('\nFile has been added!')
                    
                    else:
                         print('\nNo such file/folder!')

            elif user_input == 2: # change directory
            
                while True: 

                    in_home  = True
                    
                    if os.getcwd() != 'C:\\Users\\ASUS': in_home = False # to check if in home directory
                    
                    path_list = logic.list_directory(True) # lists the directory, folders only
                

                    user_input = Classes.move_change_dir(in_home)

                    if user_input == '0':
                        break

                    elif user_input == '1' and not in_home:
                        os.chdir('..')
                        print('\nMoved back a directory!')

                    else:

                        if user_input in path_list: # change directory

                            os.chdir(os.getcwd() + '\\' + user_input) # moves to a new directory (from user input)

                            print('\nDirectory has been changed!')


                        else:
                            print('No such path!')


            elif user_input == 3: # move all files/folders in os.cwd()

                if len(file_list) == 0:
                    print('\nFile list is empty!')

                    continue

                else:

                    for element in file_list:

                        print('\n Element: [' + element + "] is Successfully moved!\n")
                        shutil.move(os.getcwd() + '\\' + element,os.curdir())



                









            ''' provide another prompt to let you enter a path name '''
 #
                #
#
#
#
#






''' BUG: Cannot create a folder that already exists!
    BUG: When returning to interface, go back to home directory (C:\\Users\\ASUS)
    BUG: Remove a file from the list once selected ( in moving files )
    Imporvements:
    - Better way to display the directories ( Scrolling through pages! )

    BUG: In moving files, after moving a directory, moving files still in home directory


    '''






