#METHOD-1
''' TIME COMPLEXITY= O(N)'''
pal=78987
i=0
temp,r=pal,0
while temp!=0:
    r=temp%10
    i=i*10+r
    temp=int(temp/10)
print(i)
if pal == i:
    print('yes it is palindrone')
else:
    print("it is not palindrone")
    
    
#METHOD-2
n2=str(12321)
n=len(n2)
i=0
j=len(n2)-1
yes=0
while i!=j:
    if n2[i] == n2[j]:
        i+=1
        j-=1
        yes=0
    else:
        yes=-1
if(yes==0):
    print('palindrone')
else:
    print('not a palindrone')
    