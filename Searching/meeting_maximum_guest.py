def meeting_maximum_guest(arr,dep,n,m):
    arr.sort()
    dep.sort()
    i,j,cur=0,0,0
    res=0
    while(i<n and j<m):
        if arr[i]<dep[j]:
            i+=1
            cur+=1
        else:
            j+=1
            cur-=1
        res=max(res,cur)
    return res



arr=[800,700,600,500]
dep=[840,820,830,530]
n,m=len(arr),len(dep)
print(meeting_maximum_guest(arr, dep, n, m))