n=12345



# METHOD-1   
''' TIME COMPLEXITY= O(n)  ''' 
c=0
while n > 0:
    n=int(n/10)
    c+=1
print(c)




#METHOD-2
n1=12345
c1=0
''' recurssive method'''
''' TIME COMPLEXITY= O(Logn)'''

def countdigit(n,c1):
    if n==0:
        return c
    c1+=1
    return countdigit(int(n/10),c1)

print(countdigit(n1,c1))






#METHOD-3
''' TIME COMPLEXITY= O(1) '''

import math
n3=12345
print(int(math.log(n3,10)+1))
