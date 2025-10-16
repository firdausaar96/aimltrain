# subject=('python','sql','power bi','dotnet','java')
# print('\n All subject are: ')
# for sub in subject:
#     print(sub,end= '\t')

numbers=(1,2,3,4,5,6,7,8,90,22)
print('\n All numbers in tupple are: ',len(numbers))
for num in numbers:
    print(num,end= '\t')

#--------------------------------------------------------------------------------------------------
#tupleName.index(item) will return the index of first occurance of the item in tupleName
# search_num=int(input("\nEnter Number to find out index: ")) 
# if search_num in numbers:
#     print(f"Index of {search_num} is : ",numbers.index(search_num))
# else:
#     print(f"There is no such number {search_num} in the list")

#--------------------------------------------------------------------------------------------------
# tupleName.count(item) will return the frequency of the number in the tupleName
search_num=int(input("\nEnter Number to find out frequency: ")) 
if search_num in numbers:
    print(f"The number {search_num} is : {numbers.count(search_num)} times")
else:
    print(f"There is no such number {search_num} in the list")


