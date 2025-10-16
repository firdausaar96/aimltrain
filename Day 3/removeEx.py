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