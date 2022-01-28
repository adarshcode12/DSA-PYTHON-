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





# MAIN
arr=[2,10,20,30,37,56,90]
n=len(arr)
element=100
print(binarySearch(arr, n, element))

