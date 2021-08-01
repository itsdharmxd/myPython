def dic(n):
    di=dict.fromkeys(range(1,n+1))# ot di={}
    for i in range(1,n+1):
        di[i]=i**3

    return di

e=int(input("entr a number "))
di=dic(e)
print(di)        
