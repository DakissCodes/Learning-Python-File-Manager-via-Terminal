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

    user = input('\n[B] Go Back a Directory\n[N] Next Page\n[P] Previous Page\n\n[0] Exit\n[1] Choose Files/Folders\n[2] Change Directory\n[3] Move Files\nENTER HERE: ')

    return user

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

        self.max_index = 5
        self.min_index = 0

    def element_scroller(self,user_input,in_home,path_list): # element displayer and scroller
        
        
        if user_input.upper() == 'B':

            if in_home:
                print("\nAlready in home directory!")
                return self.max_index,self.min_index

            elif not in_home:
                os.chdir('..')
                print('\nMoved back a directory!')

                self.self.max_index_index = 5
                self.min_index = 0  

                return self.max_index,self.min_index

        elif user_input.upper() == 'N':

            self.max_index += 5
            self.min_index += 5
            return self.max_index,self.min_index


        elif user_input.upper() == 'P': 

            if self.max_index == 5 and self.min_index == 0:

                print('\nAlready in first page!')
                return self.max_index,self.min_index

            else:

                self.max_index -= 5
                self.min_index -= 5
                return self.max_index,self.min_index
        
        elif user_input.upper() == 'C': 

            while True:

                user_input = input('\nEnter path name here: ')

                if user_input in path_list: # change directory

                    
                    os.chdir(os.getcwd() + '\\' + user_input) # moves to a new directory (from user input)

                    print('\nDirectory has been changed!')

                    self.max_index = 5
                    self.min_index = 0 
                    return self.max_index,self.min_index

                else:

                    print('\nNo such path!')   
        
        



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




    def element_displayer(self,path_list):
        if len(path_list) <= 5:

            for element in path_list[::]: print('\n' + element)

        else:

            if len(path_list[self.min_index:self.max_index]) == 0: 
                print('\nNo more items! ')
                self.max_index -= 5
                self.min_index -= 5     

            for element in path_list[self.min_index:self.max_index]: print('\n' + element)



