emps=['vi','va','vu','ve','vua','via']
print('Number of employees in the list are: ',len(emps))
for emp in emps:
    print(emp,end=' ')

del_index=int(input("\nEnter index to pop item: \t"))
print('\nPop Result: ',emps.pop(del_index))

print("Number of Employees after pop are: ",len(emps))
for emp in emps:
        print(emp,end=" ")
