def lomuto_partition(arr,l,n):
    pivot=arr[n]
    i=l-1
    for j in range(l,n-1):
        if arr[j]<pivot:
            i+=1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    temp=arr[i+1]
    arr[i+1]=arr[n]
    arr[n]=temp
    return i+1


arr=[10,80,30,90,40,50,70]
n=len(arr)-1
print(lomuto_partition(arr, 0, n))
    