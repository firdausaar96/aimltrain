# import os
# file_path=r'C:\Users\pc\Firdaus\Day 8\files\sample1.txt'
# file=open(file_path,"w")
# content=input('Enter text to write in file: ')
# file.write(content)
# file.close()

#-------------------------------------------------------------------------------------------------
# create file and write content 
# import os

# filepath=r'C:\Users\pc\Firdaus\Day 8\files'
# #filepath=os.getcwd()  #current directory
# filename=input('Enter File name to create file: ')
# fullpath=os.path.join(filepath,filename)   #join the directory with the filename
# file=open(fullpath,"w")
# content=input('Enter text to write in the file: ')
# file.write(content)
# print(f'File {filename} create at {fullpath} and content saved in the file')
# file.close()

#---------------------------------------------------------------------------------------------
#find file and update/append
# import os

# filepath=r'C:\Users\pc\Firdaus\Day 8\files'
# #filepath=os.getcwd()  #current directory
# filename=input('Enter File name to update file: ')
# fullpath=os.path.join(filepath,filename)   #join the directory with the filename
# if (os.path.exists(fullpath)):             #to check the file is exist or not
#     file=open(fullpath,"a")
#     content=input('Enter text to add in the file: ')
#     file.write(content)
#     print(f'File {filename} updated')
#     file.close()
# else:
#     print(f'No such file {filename} exist')

#---------------------------------------------------------------------------------------------
#find file and read
import os

filepath=r'C:\Users\pc\Firdaus\Day 8\files'
#filepath=os.getcwd()  #current directory
filename=input('Enter File name to read file: ')
fullpath=os.path.join(filepath,filename)   #join the directory with the filename
if (os.path.exists(fullpath)):             #to check the file is exist or not
    file=open(fullpath,"r")
    content=file.read()
    print('File content as follow: \n')
    print(content)
    file.close()
else:
    print(f'No such file {filename} exist')