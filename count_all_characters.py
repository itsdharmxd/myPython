string=input("Enter a string : ")
while string:
    c=string[0]
    count=0
    i=0
    for i in string:
        if i==c:
            count+=1   
            
    
    print(f"=>{c}={count}")
    string=string.replace(c,'')

