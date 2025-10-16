class InvalidAge(Exception):
    pass

def check_age(age):       #raise digunakan untuk buat custom error
    if (age<=0):
        raise InvalidAge ('Age should not be negative(-)')
    elif (age<18):
        raise InvalidAge ('Age should be greater than 18 Years Old')
    elif (age>=65):
        raise InvalidAge ('Unrealistic age')
    else: 
        print (f'Age {age} is accepted and valid age for employment')

try:
    userage=int(input("Please Enter your age: \n"))
    check_age(userage)
except Exception as ex:
    print('Error ',ex)

#--------------------------------------------------------------------------------------------------------

