def Search_rotated(arr,n,x):
    low,high=0,n-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        if arr[mid]>arr[low]:
            if arr[mid]>x and arr[low]<x:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<x and arr[high]>=x:
                low=mid+1
            else:
                high=mid-1
    return -1


arr=[4,5,6,7,8,9,1,2,3]
n=len(arr)
x=2
print(Search_rotated(arr, n, x))