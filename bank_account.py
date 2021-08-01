net_amount=int(input("enter the net ammount="))
while True:
    print("\nenter [W/D:Amount]=",end=(""))
    ty,new=input("").split(':')
    new=int(new)
    if ty=='W':
        net_amount-=new
    elif ty=='D':
        net_amount+=new
    else:
        print("invlid input")
    if 'Y'==input('enter Y to continue='):
        pass
    else:
        print("NET AMOUNT=",net_amount)
        break


