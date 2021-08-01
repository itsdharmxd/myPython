with open(r'C:\Users\dharmesh\Documents\PYTHON\dharmesh.txt','r') as f1:
    with open(r'C:\Users\dharmesh\Documents\PYTHON\dharmesh2.txt','w') as f2:
        lin=f1.readlines()
        for i in lin:
            a,b=i.split(',')
            f2.write(f'{a} got {int(b)} in all total\n') 