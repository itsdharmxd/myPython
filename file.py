f=open(r'C:\Users\dharmesh\Documents\PYTHON\dharmesh.txt')
print(f.readline())
print(f.readlines())
print(f.tell())

f.close    
with open(r'C:\Users\dharmesh\Documents\PYTHON\dharmesh.txt') as g:
    print(g.readlines())
