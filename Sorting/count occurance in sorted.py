def last_occ(arr,n,x):
    low,high=0,n-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==x:
            if arr[mid]!=arr[mid+1] or mid==0:
                return mid
            else:
                low=mid+1
        elif arr[mid]>x:
            high=mid-1
        else:
            low=mid+1
    return -1

def first_occ(arr,n,x):
    low,high=0,n-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==x:
            if arr[mid]!=arr[mid-1] or mid==0:
                return mid
            else:
                high=mid-1
        elif arr[mid]>x:
            high=mid-1
        else:
            low=mid+1
    return -1


arr=[1,5,10,20,20,20,20,30,40]
n=len(arr)
x=100
if first_occ(arr, n, x) == -1:
    print("not found")
else:
    print( (last_occ(arr, n, x) -first_occ(arr, n, x)  )+1)
            