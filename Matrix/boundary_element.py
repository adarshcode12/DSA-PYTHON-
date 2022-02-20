def boundary_element(arr,r,c):
    if r==1:
        for i in range(0,c):
            print(arr[0][i])
    elif c==1:
        for i in range(0,r):
            print(arr[i][0])
    else:
        for i in range(0,c):
            print(arr[0][i])
        for i in range(1,r):
            print(arr[i][r-1])
        for i in range(c-2,-1,-1):
            print(arr[r-1][i])
        for i in range(r-2,-1,-1):
            print(arr[i][0])
            
    
    
arr=[[1,2,3],[4,5,6],[7,8,9]]
c,r=3,3
boundary_element(arr, r, c)