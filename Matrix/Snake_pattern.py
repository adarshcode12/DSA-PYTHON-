def snake_pattern(arr,r,c):
    for i in range(0,r):
        if i%2==0:
            for j in range(0,c):
                print(arr[i][j]," ",end="")
        else:
            for j in range(c-1,-1,-1):
                print(arr[i][j]," ",end="")

arr=[[1,2,3],[4,5,6],[7,8,9]]
c,r=3,3
snake_pattern(arr, r, c)