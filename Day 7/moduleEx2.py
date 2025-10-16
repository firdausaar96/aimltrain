#to print random number
# import random

# print('Random number from 1 to 1000: ')
# print(random.randint(1,1000))

#--------------------------------------------------------
import random
name=input('Enter Your Name: ')
luckyNumber=random.randint(1,10)
print(f'Welcome Mr/Mrs {name} \nYour coupon Number is ',luckyNumber)


if(luckyNumber==1):
    print(f"Congratessss.. Mr/Mrs {name}\n You won x50 Proton")
elif(luckyNumber==4):
    print(f"Congratessss.. Mr/Mrs {name}\n You won x50 Proton")
else:
    print('No luck!!!!Please try again')