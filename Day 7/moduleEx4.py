# import os   #All function related to directory
# print('Current Directory: ',os.getcwd())

#-----------------------------------------------------------------------
#create a folder inside current directory using python
# import os

# cdir=os.getcwd()
# folder_name=input('Enter Folder name to create:- ')
# folder_path=os.path.join(cdir,folder_name)

# if(os.path.exists(folder_path)):
#     print('Folder Already Existed')
# else:
#     os.makedirs(folder_path,exist_ok=True)
#     print(f'{folder_name} created at {folder_path}')

#--------------------------------------------------------------
#rename a folder name

import os

def folder():
    cdir=os.getcwd()
    old_name=input('Enter Folder name you want to rename:- ')
    folder_path=os.path.join(cdir,old_name)


    if(os.path.exists(folder_path)):
        folder_name=input('Enter New Name for the Folder: ')
        old_name=os.rename(old_name,folder_name)
        print(f'Well Done, Your new folder name is: {folder_name}')

    else:
        print(f'Sorry!!! No Folder >>{old_name}<< found')
