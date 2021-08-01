def reverse(l):
     l2=[]
     i=0
     for sub in l:
         l2.append(sub[::-1])
         i=+1 
     return l2





l=['dharmesh','lalit','sneha']
l=reverse(l)
print(l)