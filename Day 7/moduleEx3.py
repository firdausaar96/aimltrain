import datetime
import inspect

dtclass=inspect.getmembers (datetime,inspect.isclass)
print('All Classes is datetime module: ')
for n, func in dtclass:
    print(n,end='\t')

print("\n\n Today is: ",datetime.date.today(),"  ",datetime.datetime.now().time())

cttime=datetime.datetime.now().time()
formatedtime=datetime.datetime.now().strftime('%I %M %S %p')

print('Current time ',cttime)
print('Formated time ',formatedtime)