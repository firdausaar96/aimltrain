# num=1
# print('Print Number from 1 to 100')
# while (num<=100):
#     print(num,end=' ')
#     num+=1

# Break Example 
# num=1
# print('Print Number from 1 to 100 before we get the number devisible by 11')
# while (num<=100):
#     if (num==11):
#         break
#     print(num,end=' ')
#     num+=1

#continue Example
# num=1
# while (num<=100):

#     if (num%11==0):
#         num+=1
#         continue
#     print(num,end=' ')
#     num+=1

# for i in range (1,100):
#     if (i%5==0):
#         continue
#     print(i,end='\t ')

#Correct Password
# CorrectPwd='Firdaus123'
# while True:
#     pwd=input('Enter Password to start the Game :')
#     if (CorrectPwd==pwd):
#         print('Welcome to the access the game')
#         break
#     else:
#         print('Please enter the correct password')

# 3 time attempt
CorrectPwd='Firdaus123'
count=0
while True:
    pwd=input('Enter Password to start the Game :')
    if (CorrectPwd==pwd):
        print('Welcome to the access the game')
        break
    else:
        print('Wrong Password')
        count+=1
        if(count>=3):
            print('Blocked for further attempt')
            break