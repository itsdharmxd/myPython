def tower(n,a,b,c):
    if n>=1:    
        tower(n-1,a,c,b)
        print(f"{a} to {c}")
        tower(n-1,b,a,c)
e=int(input("enter the number of disks="))
a='A';b='B';c='C'
tower(e,a,b,c)    