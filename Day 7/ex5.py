import calc
import moduleEx4

first_num=float(input('Enter First Number:- '))
second_num=float(input('Enter Second Number:- '))
print(f'Total of {first_num}, {second_num} = ',round(calc.add(first_num,second_num)),2)
print(f'Average of {first_num}, {second_num} = ',round(calc.avg(first_num,second_num)),2)
