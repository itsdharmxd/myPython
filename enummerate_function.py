def fun(lis,na):
    for pos,name in enumerate(lis):
        if name==na:
            return pos
    else:
         return -1    



lis=['dharmesh','upadhyaya','lalit','dubey','sneha','jagt']
print(f'index={fun(lis,"sneha")}')