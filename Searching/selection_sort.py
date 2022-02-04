def selection_Sort(arr,n):  # first compare the minimum element and replace to 1st position
    for i in range(n):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
        temp=arr[i]
        arr[i]=arr[mini]
        arr[mini]=temp
    return arr


arr=[4,76,3,12,6,2,5]
n=len(arr)
print(selection_Sort(arr, n))
