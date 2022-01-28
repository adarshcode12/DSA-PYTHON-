def two_pointer(arr,n,x):
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
x=17
print(two_pointer(arr, n, x))