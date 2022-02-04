def union_of_tow_sorted_array(arr1,arr2,n,m):
    i,j,a=0,0,[]
    while(i<n and j<m):
        if i>0 and arr1[i]==arr1[i-1]:
            i+=1
            continue
        if j>0 and arr2[j]==arr2[j-1]:
            j+=1
            continue
        
        if arr1[i]<arr2[j]:
            a.append(arr1[i])
            i+=1
        elif arr1[i]>arr2[j]:
            a.append(arr2[j])
            j+=1
        else:
            a.append(arr1[i])
            i+=1
            j+=1
    while(i<n):
        a.append(arr1[i])
        i+=1
    while(j<m):
        a.append(arr2[j])
        j+=1
    return a


arr1=[2,2,3,5,8]
arr2=[2,8,9,10,15]
n,m=len(arr1),len(arr2)
print(union_of_tow_sorted_array(arr1, arr2, n, m))
