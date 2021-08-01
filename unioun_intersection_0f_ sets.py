a=[];b=[]
n=int(input("entr the length of list="))
print("ENTER ELEMENTS OF LIST A")
for i in range(n):
      a.append(int(input("enter number=")))
print("ENTER ELEMENTS OF LIST B")
for i in range(n):
    b.append(int(input("enter element=")))
print(f"UNIOUN \n{list(set(a)|set(b))}\nINTERSECTION\n{list(set(a)&set(b))}")    

