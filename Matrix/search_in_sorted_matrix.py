def search_matrix(arr,r,c,x):
    low,high=0,c-1
    while(low<r and high>=0):
        if arr[low][high]==x:
            print(low,high)
            return
        elif arr[low][high]>x:
            high-=1
        else:
            low+=1
    print('not found')
        
    
    
arr=[[1,2,3],[4,5,6],[7,8,9]]
c,r=3,3
x=5
search_matrix(arr, r, c,x)