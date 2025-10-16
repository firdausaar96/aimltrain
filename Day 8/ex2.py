from ourpack import calc

while True:
    try:
        fnum=float(input('Enter First Number: '))
        snum=float(input('Enter Second Number: '))
        op=input('Choose operation +,-,*,/ : ')

        if (op=="+"):
            print("Result: ",calc.add(fnum,snum))
        elif (op=="-"):
            print("Result: ",calc.sub(fnum,snum))
        elif (op=="*"):
            print("Result: ",calc.multi(fnum,snum))
        elif (op=="/"):
            print("Result: ",calc.div(fnum,snum))
        else:
            print('Wrong Operation')
    except ZeroDivisionError as zd:
        print("Number cannot be devided to 0")
    except Exception as e:
        print('Error ',e)
    choice=input("Press y to continue\n").lower()

    if (choice!='y'):
        print('Bye')
        break
