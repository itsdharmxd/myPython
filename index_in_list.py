lis=[10,10,10,20,20,30,40,50]
find=[]
for i in lis:
    find.append(lis.index(i))
print(list(set(find)))    