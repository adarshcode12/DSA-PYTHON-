def binarySearch(arr,low,high,element):
    if (low<=high):
        mid=(low+high)//2
        if arr[mid] == element:
            return mid
        elif (arr[mid]>element):
            return binarySearch(arr, low, mid-1, element)
        else:
            return binarySearch(arr, mid+1, high, element)
    else:
        return -1

arr=[10,20,30,40,50,60,70]
n=len(arr)
high=n-1
element=30
print(binarySearch(arr, 0, high, element))