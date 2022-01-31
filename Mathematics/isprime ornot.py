#METHOD-1
'''TIME COMPLEXITY: O(N)'''
n=4
r=int(13/2)+1
count=True
for i in range(2,r+1):
    if(n%i==0):
        count= False
        break
if (count):
    print('prime')
else:
    print('not prime')
    
    
#METHOD-2
'''TIME COMPLEXITY= O(1)'''
'''ANY PRIME NUMBER IS EQUAL TO 6N+1 OR 6N-1'''
'''ALSO 25 MAY CONSIDER SO N IS NOT DIVISIBLE BY 5'''
'''IS A PRIME NUMBER'''    
n=5

if(((n+1)%6) ==0 or ((n-1)%6)==0 ):
    if((n%5)!=0):
        print('prime')
    elif(n%5==0):
        print('not prime')
else:
    print('not prime')
    
    
#METHOD-3
'''AS X*Y=N AND X*X=N ----->  X<=ROOT(N)
   AS X IS SMALL NO. AND SO IF WE TAKE Y THERE WILL ALWAYS BE A SMALL VALUE X AS ITS PAIR
   WHICH IS DIVISIBLE BY X AND Y BOTH SO WE CONSIDERED X'''
'''SO WE MOVE FROM 2 TO SQRT N'''
'''GFG RECOMMENDED'''
n5=4
rr=int(pow(n5,1/2))
count1=True
for i in range(2,rr):
    if(n5%i==0):
        print(r)
        count1=False
        break
if(count1):
    print('prime')
else:
    print('not prime')
