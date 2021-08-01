st=input("enter a string=")
for i in range(len(st)):
    if st[i]>='a' and st[i]<='z':
      st=st.replace(st[i],chr(ord(st[i])-32))
print(st)        