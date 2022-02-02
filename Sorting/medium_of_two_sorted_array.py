def medium_sorted(arr1,arr2,n,m):
    low,high=0,n
    while(low<=high):
        mid1=(low+high)//2
        mid2=(n+m+1)//2 - mid1
        # if left side is not present in arr1
        if (mid1==0):
            max1=float('inf')
        else:
            max1=arr1[mid1-1]
        # if left side is not present in arr2
        if (mid2==0):
            max2=float('inf')
        else:
            max2=arr2[mid2-1]
        #if right side is not present in arr1
        if (mid1==n):
            min1=float('-inf')
        else:
            min1=arr1[mid1]
        #if right side is not present in arr2
        if (mid2==m):
            min2=float('-inf')
        else:
            min2=arr2[mid2]
        
        # if left max is less than right min and visa versa then the combine array is sorted
        if(max1<=min2 and max2<=min1):
            if(n+m)%2 ==0:
                return(max(max1,max2)+min(min1,min2))/2
            else:
                return(max(max1,max2))
        # we can only work with arr1 as we only define aar1 low,high so:
        #for max1>min2 we can only manipulate max1 so by decreasing max2 we can increase min2
        elif (max1>min2):
            high=mid1-1
        # for min1<max2 we can only manipulate min1 of arr1 so we increase min1
        else:
            low=mid1+1
        
        
arr1=[10,20,30]
arr2=[5,15,25,35,45]    #[1,2,3,3,4,5,6,7,8,9]
n=len(arr1)-1
m=len(arr2)-1
print(medium_sorted(arr1, arr2, n, m))
            
        
        
            
        