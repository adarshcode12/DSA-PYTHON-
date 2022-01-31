n=4

#method-1
'''time complexity=O(n)'''
for i in range(1,n):
    if n%i==0:
        print(i)



#method-2
'''time complexity=O(root n)'''

sq=int(pow(n,1/2))
for i in range(1,sq+1):
    if n%i==0:
        print(i)
    if(i!=n/i):
        print(int(n/i))
    
#method-3
'''print factor in sequence order
    time complexity= O(root n)'''        
sq=int(pow(n,1/2))
for i in range(1,sq+1):
    if n%i==0:
        print(i)
for i in range(sq,1,-1):
    if n%i==0:
        print(int(n/i))        