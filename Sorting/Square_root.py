def Squareroot(arr,x):
    low,high=1,x
    ans=-1
    while low<=high:
        mid=(low+high)//2
        sq=mid**2
        if sq==x:
            return mid
        elif sq>x:
            high=mid-1
        else:
            low=mid+1
            ans=mid
    return ans


arr=[1,2,3,4,5,6,7,8,9,10]
n=len(arr)
x=6
print(Squareroot(arr, x))



# as we are looking for the floor of the quare root number therefoce, 
#we consider the square root smaller than the number.