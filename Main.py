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

        logic.max_index = 5
        logic.min_index = 0   
        
        while True:

            in_home = True

            if os.getcwd() != 'C:\\Users\\ASUS': in_home = False # checks if in home directory


            path_list = logic.list_directory(True) # list of paths in current directory, and current directory paths
            # path list is the list of folders/files in a directory! 

            if len(path_list) <= 5:

                for element in path_list[::]: print('\n' + element)


            else:

                if len(path_list[logic.min_index:logic.max_index]) == 0: 
                    print('\nNo more items! ')
                    logic.max_index -= 5
                    logic.min_index -= 5
        
                for element in path_list[logic.min_index:logic.max_index]: print('\n' + element)



            user_input = Classes.create_file_input(in_home) # edit this!
            if user_input == '0':
                break
            
            if user_input == '': # create file in current directory 
                

                os.mkdir(os.path.join(os.getcwd(),file_name)) # creates the directory 

                print('\nFolder successfully created!')
                
                break
            
            logic.element_scroller(user_input,in_home,path_list)




        os.chdir('C:\\Users\\ASUS')

    elif user_input == 2: # move folders/file

        file_list = [] # files to move 

        logic.max_index = 5
        logic.min_index = 0   
        
        while True:

            in_home = True
            if os.getcwd() != 'C:\\Users\\ASUS': in_home = False # checks if in home directory

            path_list = logic.list_directory(False) # displays both files and folders

            logic.element_displayer(path_list)

            print(file_list) # shows files to move



            user_input = Classes.move_interface() # user interface

            logic.element_scroller(user_input,in_home,path_list)
        
            if user_input == '0':
                break






            elif user_input == '1': # choose files in current directory
                
                while True: # while user does not input 0
                    path_list = logic.list_directory(False) # displays all files and folders
                    logic.element_displayer(path_list)

                    user_input = input('\n[0] Exit\n[N] Next Page\n[P] Previous Page\n\nEnter file name: ')
                    
                    logic.element_scroller(user_input,None,path_list)
                    if user_input == '0': 
                        break
                    
                    elif user_input in path_list: 
                        file_list.append(user_input)
                        print('\nFile has been added!')
                    
                    else:
                         print('\nNo such file/folder!')





            elif user_input == '2': # change directory
            
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


            elif user_input == '3': # move all files/folders in os.cwd()

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
    - Intialize max, min in class 
    BUG: In moving files, after moving a directory, moving files still in home directory


    '''






