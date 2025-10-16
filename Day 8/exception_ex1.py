try:
    fnum=float(input('Enter First Number: '))
    snum=float(input('Enter Second Number: '))
    result=fnum/snum
    print(f'Result: {round(result,4)} after deviding {fnum} by {snum}')
except Exception as e:
    print('Error ',e)
finally:
    print('End of Program')