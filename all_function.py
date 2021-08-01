def all_are_even(lis):
    return all(list(map(lambda i:i%2==0,lis)))
    

lis=[2,4,6,8,12,14]
print(all_are_even(lis))