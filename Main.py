# use filter for file identification, ex. if file in list of directories. 


from xml.dom.minidom import Element
import Classes
import os
import pdb
import shutil



logic = Classes.directory()

while True:

    user_input = int(Classes.user_interface(0)) # displays user interface, asks for an input

    if user_input == 0: # exits the program
        os.system('cls')
        break

    elif user_input == 1: # create a new folder

        file_name = input("Enter file name: ") # name of the folder

        logic.max_index = 5
        logic.min_index = 0   



        while True:
            os.system('cls')
            
            in_home = True

            if os.getcwd() != 'C:\\Users\\ASUS': in_home = False # checks if in home directory


            logic.list_directory(True) # list of paths in current directory, and current directory paths
            # path list is the list of folders/files in a directory! 

            if len(logic.path_list) <= 5:

                for element in logic.path_list[::]: print('\n' + element)


            else:

                if len(logic.path_list[logic.min_index:logic.max_index]) == 0: 
                    print('\nNo more items! ')
                    logic.max_index -= 5
                    logic.min_index -= 5
        
                for element in logic.path_list[logic.min_index:logic.max_index]: print('\n' + element)



            user_input = Classes.create_file_input(in_home) # edit this
            
            if user_input == '0':
                os.system('cls')
                break
            
            if user_input == '': # create file in current directory 
                

                os.mkdir(os.path.join(os.getcwd(),file_name)) # creates the directory 

                os.system('cls')
                print('\nFolder successfully created!\n')
                break

            if user_input.upper() == 'B':

                if in_home:
                    print("\nAlready in home directory!")

                elif not in_home:
                    os.chdir('..')
                    print('\nMoved back a directory!')

                    logic.max_index = 5
                    logic.min_index = 0  
           
            logic.element_scroller(user_input)




        os.chdir('C:\\Users\\ASUS')

    elif user_input == 2: # move folders/file

        file_list = [] # files to move 

        logic.max_index = 5
        logic.min_index = 0   
        
        while True:
            os.system('cls')

            in_home = True
            if os.getcwd() != 'C:\\Users\\ASUS': in_home = False # checks if in home directory

            logic.list_directory(False) # displays both files and folders

            logic.element_displayer()

            print('\nFILES TO MOVE: ')
            print(file_list) # shows files to move

            user_input = Classes.move_interface() # user interface]

            if user_input.upper() == 'B':

                if in_home:
                    print("\nAlready in home directory!")

                elif not in_home:
                    os.chdir('..')
                    print('\nMoved back a directory!')

                    logic.max_index = 5
                    logic.min_index = 0              

            logic.element_scroller(user_input)
        
            if user_input == '0':
                break





            elif user_input == '1': # choose files in current directory (FOLDERS AND FILES)


                logic.list_directory(False)

                while True: # while user does not input 0
                    logic.element_displayer()

                    user_input = input('\n[0] Exit\nEnter file name: ')
                    

                    if user_input == '0': 
                        break
                    
                    elif user_input in logic.path_list: 
                        file_list.append(os.getcwd() + '\\' + user_input)
                        print('\nFile has been added!')
                    
                    else:
                         print('\nNo such file/folder!')





            elif user_input == '2': # change directory (FOLDERS ONLY)
                
                while True: 

                    user_input = input('Enter path name: ')

                    if user_input in logic.path_list: # change directory

                        os.chdir(os.getcwd() + '\\' + user_input) # moves to a new directory (from user input)

                        print('\nDirectory has been changed!')
                        break

                    else:
                        print('No such path!')


            elif user_input == '3': # move all files/folders in os.cwd()

                if len(file_list) == 0:
                    print('\nFile list is empty!')

                    continue

                else:
                    while True:
                        os.chdir('C:\\Users\\ASUS')

                        logic.list_directory(True)

                        logic.element_displayer()
                        print('\n')
                        print(os.getcwd())
                        user_input = input('\n[0] Exit\n[N] Next Page\n[P] Previous Page\n[M] Move Here\n\nEnt ')

                        if user_input == '0':
                            break

                        elif user_input == 'M':

                            for element in file_list:
                                path = os.getcwd()
                                shutil.move(element, os.getcwd())
                                print("\n Element: " + element.split('\\')[-1] + " is Successfully moved!\n")


                        logic.element_scroller(user_input)

                    for element in file_list:
                        path = os.getcwd()
                        shutil.move(element, os.getcwd())
                        print('\n Element: [' + element + "] is Successfully moved!\n") 









            ''' set a different directory for scrolling, and a different directory for  '''
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






