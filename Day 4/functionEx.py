#Function without Parameter

# def welcome():
#     print("Welcome to Functions")
#     print("Our First Function")

# welcome()

#-----------------------------------------------------------------------
#Function with Parameter

# def welcome(name):
#     print("Welcome to Functions in Python Mr.\\Ms",name)

# username=input("Enter Your Name: ")
# welcome(username)        #Function call

#-----------------------------------------------------------------------
#Function with Parameter and return

# def add(num1,num2):
#     return num1+num2

# def multi(num1,num2):
#     return num1*num2

# fnum=int(input("Enter first number: "))
# snum=int(input("Enter second number: "))
# print(f"Result after adding {fnum} and {snum} is = ",add(fnum,snum))
# print(f"Result after multiply {fnum} and {snum} is = ",multi(fnum,snum))

#-----------------------------------------------------------------------
#Function Exercise

# def salary(num1):
#     return num1*0.1

# Bonus=float(input("Please Enter your Salary to calculate your bonus: "))
# TotalSalary=Bonus+salary(Bonus)
# print(f"Your bonus is {salary(Bonus)} \nYour total salary is :",TotalSalary)

#-----------------------------------------------------------------------
#Default parameter in function

# def info(id,name,place='New Delhi'):
#     print(f"The detail as follow \n ID: {id} Name:  {name} Place: {place} ")

# info(1,'Sam', 'KL')
# info(2,'Firdaus')

#-----------------------------------------------------------------------
#We want to create a single method that can able to add 5 numbers even not provide all 5 numbers
#and return correct total

def add(n1=0,n2=0,n3=0,n4=0,n5=0):
    return n1+n2+n3+n4+n5

print("Result is: ",add(1,2))
print("Result is: ",add(1,2,5,4,12))
print("Result is: ",add(1,23,44))

#-----------------------------------------------------------------------
def add(*nums):
    return sum(nums)

print("Sum of 1,10,33,2 is:  ",add(1,10,33,2))
print("Sum of 1,10 is:  ",add(1,10))
print("Sum of 1,10,33,2,44,32,222 is:  ",add(1,10,33,2,44,32,222))

#-----------------------------------------------------------------------
print("maximum number of 1,10,33,2 is:  ",max(1,10,33,2))
print("minimum number of 1,10,33,2 is:  ",min(1,10,33,2))