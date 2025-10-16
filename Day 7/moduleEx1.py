# import math
# num=int(input('Enter Number to find out square root: '))
# print(f'Square root of {num} : ',round(math.sqrt(num),2))  #round off number into 2 decimal places round(),2
    
#----------------------------------------------------------------------------------
import math
import inspect

functions=inspect.getmembers (math,inspect.isbuiltin)
print('All function is math module: ')
for n, func in functions:
    print(n,end='\t')