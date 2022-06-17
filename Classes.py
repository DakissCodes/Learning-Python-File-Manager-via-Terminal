import shutil
import os
import pdb




def user_interface(num):

    user = input("[0] Exit\n[1] Create a New Folder\n[2] Move Folders\n[3] Delete Folder\n[4] Delete File\n\nENTER HERE: ")
    return int(user)

def create_file_input(bool):
    if not bool:
        user = input("\n[0] Exit\n[1] Go Back\n[Enter] Create Here\n\nENTER PATH HERE: ")
    elif bool:
        user = input("\n[0] Exit\n[Enter] Create Here\n\nENTER PATH HERE: ")

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


    def list_directory(self):

        path_list = []

        def listdir_nohidden(path): # removes hidden folders 
            for f in os.listdir(path):
                if not f.startswith('.'):
                    yield f

        for _ in listdir_nohidden(os.getcwd()): # loops through the directories

            path = os.getcwd() + '\\' + _  # directory

            
            if os.path.isdir(path): # check if file
                
                path_list.append(_) 
        
        ' '.join(_ for _ in path_list[0:len(path_list)//2])

        ' '.join(_ for _ in path_list[len(path_list)//2:len(path_list)+1])

        print(path_list)

        return path_list





