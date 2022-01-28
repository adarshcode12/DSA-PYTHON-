def two_pointer(arr,n,x):
    print(x)
    low,high=0,n-1
    while(low<high):
        if arr[low]+arr[high]==x:
            return True
        elif arr[low]+arr[high] >x:
            high-=1
        else:
            low+=1
    return False


arr=[3,5,9,2,8,10,11]
n=len(arr)
x=5
result=False
for i in range(0,n-1,1):
    if (two_pointer(arr, n, x-arr[i])):
        result=True