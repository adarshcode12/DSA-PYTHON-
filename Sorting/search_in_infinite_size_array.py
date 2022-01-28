def binarySearch(arr,n,element):
    low,high=0,n-1
    while(low<=high):
        mid=(low+high)//2
        if (arr[mid]==element):
            return mid
        elif (arr[mid]>element):
            high=mid-1
        else:
            low=mid+1
    return -1


def infi(arr,x):
    if arr[0]==x:
        return 0
    else:
        i=1
        while(arr[i]<x):
            i=i*2
        if arr[i]==x:
            return i
        return binarySearch(arr,x,i/2+1,i-1)




