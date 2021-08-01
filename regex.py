import re
regex='\.[0]*'
i='215.094.45.006'
print(re.sub(regex, '.',i))
help(re)