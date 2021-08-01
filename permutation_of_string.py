from itertools import permutations
st='ABC'
s=permutations(st)
lis=[]
for i in list(s):
    lis.append(''.join(i))



print(lis)   