def bubble_sort(arr,n):   # compare the next element if bigger then replace --->
    for i in range(n):    # largest element at last then 2nd largest
        for j in range(n-i-1):
            if arr[j+1]<arr[j]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr




arr=[4,76,3,12,6,2,5]
n=len(arr)
print(bubble_sort(arr, n))

