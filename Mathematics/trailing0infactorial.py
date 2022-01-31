#method-1
'''AS THE TIME COMPLEXITY: O(N)
   WHICH IS NOT VERY GOOD AND CAN BE 
   REDUCED BY NOT FINDING FACTORIAL'''
mai=100
n=mai
c=1
while n!=1:
    c=c*n
    n-=1
print(c)
count=0
while(c!=0):
    r=c%10
    if r<1:
        count+=1
    else:
        break
    c=c//10
print(count)

#METHOD-2
''''WE WILL NOT CALCULATE THE FACTORIAL
THE METHOD GO LIKE THIS:
    AS 10 IS COMPOSED OF --> 2*5 AND
    THE NO. OF 2 IS ALWAYS GREATER THAN 5 SO
    IF NO. OF 0 IN FACTORIAL IS EQUAL TO NO. OF 5 IN N
    '''
'''IF WE LOOK ON 5 --> IT HAS 1'5'
   IF WE LOOK AT 25 --> IT HAS 2'5' 
   ABD SO ON......'''
   
'''TIME COMPLEXITY:O(LOGN)'''
n1=25
count=0
i=5
while i<n1: 
    count=count+(n1//i)
    i=i*5
print(count)