# def cube(num):
#     cube_num=num*num*num
#     print(f"Cube of given Number {num} is : {cube_num}")

# def square(num):
#     return num*num

# username=input("Please Enter your username: ")
# my_num=int(input("Enter Number to find out cube and square: "))

# print(f"\n#####Welcome {username}#######")
# cube(my_num)
# print(f"Square number of {my_num} is : {square(my_num)}")

#---------------------------------------------------------------------------
def salBonus(salary):
    return salary*0.10

my_sal=float(input("Enter Salary to find out bonus: "))
bonus=salBonus(my_sal)
print(f"Salary {my_sal} \nBonus: {bonus}")
print(f"Salary after bonus is {my_sal+bonus}")