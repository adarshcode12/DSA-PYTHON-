def two_type_element(arr,n):
    i,j=0,n
    while(True):
        while(True):
            i+=1
            if arr[i]>0:
                break
        while(True):
            j-=1
            if arr[j]<0:
                break
        if i>j:
            return;
        arr[i],arr[j]=arr[j],arr[i]
        


arr=[-12,18,-10,15,-3]
n=len(arr)
two_type_element(arr, n)
print(arr)        