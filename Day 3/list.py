# my_list=['zamil','ujang','anim',"py","Non"]
# #my_list=[1,23,33,4,344,32,21]
# print('Number of item in the list are: ',len(my_list))
# for a in my_list:
#     print(a,end=' ')

# my_list.sort()
# print("\n")
# print("\n List after sorting ")
# for e in my_list:
#     print (e,end=" ")

# my_list.reverse()
# print("\n")
# print("\n List after Reverse ")
# for e in my_list:
#     print (e,end=" ")

# newEmp=input("\nEnter employee name to add in the list: ")
# my_list.append(newEmp)
# print("\n After adding new employee, Number of Employees are: ",len(my_list))
# for e in my_list:
#     print(e,end=" ")

# newEmp=input("\nEnter employee name to add in the list: ")
# pos=int(input ("\n Enter position where you want to put inside the list: \n"))
# my_list.insert(pos,newEmp)
# print("\n After adding new employee, Number of Employees are: ",len(my_list))
# for e in my_list:
#     print(e,end=" ")

# emps=['vi','va','vu','ve']
# print('Number of employees in the list are: ',len(emps))
# for emp in emps:
#     print(emp,end=' ')

# newEmp=input("\nEnter employee name to add in the list: ")
# pos=int(input ("\n Enter position where you want to put inside the list: \n"))
# emps.insert(pos,newEmp)
# print("\n After adding new employee, Number of Employees are: ",len(emps))
# for e in emps:
#     print(e,end=" ")

#Remove name
emps=['vi','va','vu','ve','vua','via']
print('Number of employees in the list are: ',len(emps))
for emp in emps:
    print(emp,end=' ')

delEmp=input("\nEnter employee name to delete in the list: ")
if delEmp in emps:
    emps.remove(delEmp)
    print(f"\n  Number of Employees after deleting {delEmp} are: ",len(emps))
    for emp in emps:
        print(emp,end=" ")
else:
    print(f"Sorry, No such item {delEmp} in the list")