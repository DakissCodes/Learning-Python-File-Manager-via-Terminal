import shutil
import os
import pdb




def user_interface(num):

    user = input("[0] Exit\n[1] Create a New Folder\n[2] Move Folders\n[3] Delete Folder\n[4] Delete File\n\nENTER HERE: ")
    return int(user)

def create_file_input(bool):
    if not bool:
        user = input("\n[0] Exit\n[B] Go Back a Directory\n[N] Next Page\n[P] Previous Page\n[C] Change Path\n[Enter] Create Here\n\nENTER HERE: ")
    elif bool:
        user = input("\n[0] Exit\n[N] Next Page\n[P] Previous Page\n[C] Change Path\n[Enter] Create Here\n\nENTER HERE: ")

    return user

def move_interface():

    user = input('\n[0] Exit\n[1] Choose Files in Current Directory\n[2] Change Directory\n[3] Move Files\nENTER HERE: ')

    return int(user)

def move_change_dir(bool): 
    if not bool:
        user = input("\n[0] Exit\n[1] Go Back\n\n\nEnter path here: ")
    elif bool:
        user = input("\n[0] Exit\n\nEnter path here: ")
    return user


    
    
''' function that will print files in a directory, receives a parameter that
    redirects the inventory '''


''' function that lists all files in a directory
    
    if a user inputs a name, it will redirect to that directory
        
    if a user input a name that is a file, print('not a folder!') '''

class directory: 

    os.chdir('C:\\Users\\ASUS') # home directory 
    
    def __init__(self):
 
        self.path = os.getcwd() # sets a parent directory 



    def list_directory(self,onlyfolders): # function to decorate! 

        path_list = []

        def listdir_nohidden(path): # removes hidden folders 
            for f in os.listdir(path):
                if not f.startswith('.'):
                    yield f

        for _ in listdir_nohidden(os.getcwd()): # loops through the directories

            path = os.getcwd() + '\\' + _  # directory

            
            if onlyfolders:
                
                if os.path.isdir(path): # check if file
                
                    path_list.append(_) 
                else:
                    continue

            else:

                path_list.append(_)  

    
        return path_list


def element_scroller(max,min,user_input,in_home,path_list):
    
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




