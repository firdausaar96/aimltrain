class InvalidMarks(Exception):
    pass


def check_mark(mark):       #raise digunakan untuk buat custom error
    if (mark<0):
        raise InvalidMarks ('Marks should not be negative(-)\nPlease put a valid marks (1-50)')
    elif (mark>50):
        raise InvalidMarks ('Marks should not be greater than 50\nPlease put a valid marks (1-50)')
    else: 
        print (f'Marks {mark} is accepted')

while True:
    try:
        usermark=int(input("Please Enter your Marks: \n"))
        check_mark(usermark)
    except InvalidMarks as e:
        print(e)
    except Exception as ex:
        print('Error ',ex)
    else:
        print('Recorded')
        break    
    choice=input("Do you want to enter marks?? Press y if Yes\n").lower()

    if (choice!='y'):
        print('Bye')
        break
   