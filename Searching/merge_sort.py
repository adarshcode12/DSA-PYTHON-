def merge(arr,low,mid,high):
    n1,n2=mid-low+1,high-mid
    l,r=[],[]

    for i in range(n1):
        l.append(arr[low+i])
    for i in range(n2):
        r.append(arr[mid+i+1]) 
    i,j,k=0,0,low
    while(i<n1 and j<n2):
        if l[i]>r[j]:
            arr[k]=r[j]
            k+=1
            j+=1
        else:
            arr[k]=l[i]
            k+=1
            i+=1
    while(i<n1):
        arr[k]=l[i]
        i+=1
        k+=1
    while(j<n2):
        arr[k]=r[j]
        j+=1
        k+=1


def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
        
        
arr=[5,24,2,7,45,65,4,90,34]
mergeSort(arr, 0,len(arr)-1)
print(arr)