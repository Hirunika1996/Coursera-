largest= None
smallest=None
while True:
    num=input("Enter a number: ")
    if num=='done':
        break
    try:
        fnum=float(num)
    except:
        print('Invalid input')
    if largest is None:
        largest=fnum
    elif fnum>largest:
        largest=fnum
    elif smallest is None:
        smallest=fnum
    elif fnum<smallest:
        smallest=fnum
        continue
sm=int(smallest)
lr=int(largest)
print("Maximum is",lr)
print("Minimum is",sm)
