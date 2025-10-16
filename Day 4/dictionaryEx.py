employee={"id":1,"name":"firdaus","salary":55000.5022}

print("Employees details are as follows: ")
for key,value in employee.items():
    print(key,"-->",value)

#-----------------------------------------------------------------------
#Adding key in Dictionary

employee["city"]="Muscat"
print("\nDictionary after adding city\n")

for key,value in employee.items():
    print(key,"-->",value)


#-----------------------------------------------------------------------
#Delete key in Dictionary

del employee["salary"]
print("\n Employee Details after deleting salary \n")
for key, value in employee.items():
    print(key,"->",value)

#-----------------------------------------------------------------------
#to see all keys in Dictionary

print("\n\nAll keys from Employee")
for k in employee.keys():
    print(k,end=" ")

#-----------------------------------------------------------------------
#to see all values in Dictionary

print("\n\nAll Values from Employee")
for v in employee.values():
    print(v,end=" ")

print("\nKey: Value")
for k,v in employee.items():
    print (k,' : ',v)