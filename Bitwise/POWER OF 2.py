#method-1:
n=15
count=0
while n>1:
    if n%2!=0:
        count=0
        break
    count=1
    n=n//2

if count:
    print('yes')
else:
    print('no')
    
#method-2
''' in power of 2 the set bit is always 1
    so if we use and operator between n and n-1
    if its 0 then its power of 2 ortherwise not'''

''' TIME COMPLEXITY: O(1)'''
    
c=False
if n==0:
    c=False
c=((n &(n-1))==0)
if c:
    print('yes')
else:
    print('no')    