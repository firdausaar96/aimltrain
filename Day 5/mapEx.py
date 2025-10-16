# numbers=[10,25,30,40,2,1]
# double_num=list(map(lambda x: 2*x, numbers))
# print(double_num)

# print("original List")
# for num in numbers:
#     print(num,end=" ")

# even_numbers=list(filter(lambda x: x%2==0, numbers))

# print("\nEven Numbers from list as follows: \n")
# for num in even_numbers:
#     print(num,end=" ")

#-------------------------------------------------------------------
#write a code using filter to find out all the number less than 5

# our_list=[4,2,5,6,7,3,1,10]
# our_numbers=list(filter(lambda x: x<5, our_list))

# print("original List")
# for num in our_list:
#     print(num,end=" ")

# print("\nNew list as follows: \n")
# for num in our_numbers:
#     print(num,end=" ")

#-------------------------------------------------------------------
#same example using Dictionary

student_marks={'Sam':60,
               'Deep':45,
               'Sandy':76,
               'Niraj':40,
               'Garima':54}

print('All Students')
print(student_marks)    #print together with curly bracket
for k,v in student_marks.items():
    print(f"Name: {k} , Marks: {v}")
pass_students=dict(filter(lambda item:item[1]>=50, student_marks.items()))
print("\nPassed Students")
print(pass_students)

sort_pass_students=dict(sorted(pass_students.items(),key=lambda x:x[1]))
print("\nAscending Order")
print(sort_pass_students)
for k,v in sort_pass_students.items():
    print(f"Name: {k} , Marks: {v}")

sort_pass_students_desc=dict(sorted(pass_students.items(),key=lambda x:x[1], reverse=True))
print("\nDescending Order")
print(sort_pass_students_desc)
for k,v in sort_pass_students_desc.items():
    print(f"Name: {k} , Marks: {v}")