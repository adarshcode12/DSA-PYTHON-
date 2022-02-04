def insertion_two_sorted_array(arr1,arr2,n,m):
    i,j,a=0,0,[]
    while(i<n and j<m):
        if arr1[i]==arr2[j]:
            a.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i]>arr2[j]:
            j+=1
        else:
            i+=1
    return a


arr1=[2,3,4,5,6,6,6,6,7,8]
arr2=[2,5,6,6,6,7,8,9,10,12]
m,n=len(arr1),len(arr2)
print(insertion_two_sorted_array(arr1, arr2, n, m))
    