# add=lambda a,b: a+b
# multi=lambda a,b: a*b
# div=lambda a,b: a/b
# avg=lambda a,b: (a+b)/2
# sub=lambda a,b: a-b

# num1=int(input("Enter first Number: "))
# num2=int(input("Enter second Number: "))

# print("Multiplication Result: ",multi(num1,num2))
# print("Subtraction Result: ",sub(num1,num2))

#-----------------------------------------------------------------------------

check_odd=lambda n:"Odd number " if n%2==1 else "Even Number"
num1=int(input("Enter Number to check Odd or Even: "))
print(check_odd(num1))