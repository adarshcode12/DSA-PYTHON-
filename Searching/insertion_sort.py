def insertion_sort(arr,n):  #??
    for i in range(n):
        key=arr[i]
        j=i-1
        while(j>0 and arr[j]>key):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

    return arr



arr=[4,76,3,12,6,2,5]
n=len(arr)
print(insertion_sort(arr, n))
