#METHOD-1
'''TIME COMPLEXITY = O(N)'''
n1= 12
n2= 15
r=min(n1,n2)
while r>0:
    if(n1%r==0 and n2%r==0):
        break
    r-=1
print(r)

#METHOD-2
'''time complexity: O(n)'''
a=12
b=15
while(a!=b):
    if(a>b):
        a=a-b
    else:
        b=b-a
print(a)

#method-3
'''recurssion
    time complexity: O(logn)'''

def gcd(n3,n4):
    if n4==0:
        return n3
    else:
        return gcd(n4,n3%n4)

print(gcd(12,15))