#method-1
'''TIME COMPLEXITY: O(n)'''
n1=12
n2=24
r=1
while(True):
    if(r%n1==0 and r%n2==0):
        print(r)
        break
    r+=1


#method-2
'''time complexity: O(logn)'''

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

n3=(gcd(n1,n2))
print(int((n1*n2)/n3))