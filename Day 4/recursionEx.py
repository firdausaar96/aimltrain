#Factorial
# def factorial(num):
#     if ((num==0) or (num==1)):
#         return 1
#     else:
#         return num*factorial(num-1)
    
# num=int(input('Enter a number to find out factorial: '))
# print(f"Factorial of {num} is: ",factorial(num))

#---------------------------------------------------------------
#write a function which convert inches to cms
#1 inch=2.5cm

def converter(num):
    return num*2.5

inches=int(input("Enter inches: "))
print(f"{inches} inch are equal to {converter(inches)} cm")