# import datetime
# import inspect

# dtclasses=inspect.getmembers(datetime, inspect.isclass)
# print('All classes inside datetime module')

# for n, func in dtclasses:
#     print (n)

# print('\nAll function inside datetime.date classes')

# functions=inspect.getmembers(datetime.date, inspect.isbuiltin)
# for n, func in functions:
#     print (n)

# print('Today is (Date): ',datetime.date.today())

#-------------------------------------------------------------

import os

listDirs=os.listdir()
for dir in listDirs:
    print(dir)