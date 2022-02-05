def partation(arr,low,high):
    pivot=arr[high]
    l=low
    for i in range(low,high):
        if pivot<=arr[i]:
            arr[l],arr[i]=arr[i],arr[l]
            l+=1
    arr[l],arr[high]=arr[high],arr[l]
    return l+1    
            



def kth_smallest(arr,n,k):
    l,r=0,n-1
    while(l<=r):
        p=partation(arr,l,r)
        if p == k-1:
            return p
        elif p>k-1:
            r=p-1
        else:
            l=p+1
            

arr=[10,4,5,8,11,6,26]
k=5
n=len(arr)
print(kth_smallest(arr, n, k))
        