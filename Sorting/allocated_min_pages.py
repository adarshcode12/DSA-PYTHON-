def allocated_pages(arr,n,k,mid):
    res,pages=0,0
    for i in range(n):
        if pages+arr[i]>mid:
            res+=1
            pages=arr[i]
        else:
            pages+=arr[i]
    return (res<=k)
            
    
    
    
def min_pages(arr,n,k):
    sumi,maxi=0,0
    for i in range(n):
        sumi+=arr[i]
        maxi=max(maxi,arr[i])
    low,high,res=maxi,sumi,0
    while(low<=high):
        mid=(low+high)//2
        if(allocated_pages(arr,n,k,mid)):
            res=mid
            high=mid-1
        else:
            low=mid+1
    return res




arr=[10,5,20]
k=2
n=len(arr)
print(min_pages(arr, n, k))