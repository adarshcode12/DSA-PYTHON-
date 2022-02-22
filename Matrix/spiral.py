def spiral(arr,c,r):
    top,right,bottom,left=0,c-1,r-1,0
    while(top<=bottom and left<=right):
        for i in range(left,right+1):
            print(arr[top][i])
        top+=1
        for i in range(top,bottom+1):
            print(arr[i][right])
        right-=1
        for i in range(right,left-1,-1):
            print(arr[bottom][i])
        bottom-=1
        for i in range(bottom,top-1,-1):
            print(arr[i][left])
        left+=1
    
    
    
arr=[[1,2,3],[4,5,6],[7,8,9]]
c,r=3,3
spiral(arr, r, c)