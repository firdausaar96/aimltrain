# set_one={'laptop','earphone','ipad','mobile','headphone','laptop','ipad'}
# print('Number of item in set_one are: ',len(set_one))
# for item in set_one:
#     print(item,end=' ')

#--------------------------------------------------------------------------------
#clear(): remove all the items from set

# set_one.clear()
# print('\n')
# print('Number of item in set_one after clear are: ',len(set_one))
# for item in set_one:
#     print(item,end=' ')

#--------------------------------------------------------------------------------
#set.remove(): updates the set and remove item from the set

# set_one.remove('ipad')
# print('\nAfter removing one item from set: ',len(set_one))
# for item in set_one:
#     print(item,end=" ")

#--------------------------------------------------------------------------------
#s1.union(s2): returns a new set with all items from both sets S1,S2
#gabungkan kedua2 set, dan abaikan item yg duplicate dalam kedua2 item

# set_one={100,200,300,500,700,900,150}
# set_two={100,400,700,1000,1300}

# print(f'Set_one contain : {len(set_one)} items')
# print(set_one)
# print(f'\nSet_two contain : {len(set_two)} items')
# print(set_two)

# unionset=set_one.union(set_two)
# print(f'\nUnion of set_one and set_two contains: {len(unionset)} items')
# print(unionset)


#--------------------------------------------------------------------------------
#s1.intersection(s2): Return set which contain only item in both sets s1,s2
#untuk keluarkan item yg sama sahaja dalam kedua2 set

# set_one={100,200,300,500,700,900,150}
# set_two={100,400,700,1000,1300}

# print(f'Set_one contain : {len(set_one)} items')
# print(set_one)
# print(f'\nSet_two contain : {len(set_two)} items')
# print(set_two)

# newset=set_one.intersection(set_two)
# print(f'\nIntercection of set_one and set_two contains: {len(newset)} items')
# print(newset)


#--------------------------------------------------------------------------------
#s1.difference(s2): Return set which dows not contain item in both sets s1,s2
#untuk keluarkan item yg berbeza sahaja dalam kedua2 set

set_one={100,200,300,500,700,900,150}
set_two={100,400,700,1000,1300}

print(f'Set_one contain : {len(set_one)} items')
print(set_one)
print(f'\nSet_two contain : {len(set_two)} items')
print(set_two)

newset=set_one.difference(set_two)
print(f'\nDifference of set_one and set_two contains: {len(newset)} items')
print(newset)