# try:
#     num1=float(input('Enter first number: '))
#     num2=float(input('Enter second number: '))
#     total=num1+num2
#     print(f"Sum of {num1} and {num2} = {total}")
# except Exception as e:
#     print('Error ',e)
# finally:
#     print('End of Program')

try:
    num1=float(input('Enter first number: '))
    num2=float(input('Enter second number: '))
    div=num1+num2
    print(f"Result of devision {num1} and {num2} = {div}")
except Exception as e:
    print('Error ',e)
finally:
    print('End of Program')