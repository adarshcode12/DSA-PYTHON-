def isKthBitSetleft(n, k):
    if n & (1 << (k - 1)):
        print( "SET")
    else:
        print("NOT SET")
    print(n & k)
 
    
def isKthBitSetright(n,k):
    if n & (((n>>(k-1))&1) ==1):
        print('SET')
    else:
        print("not set")
    
 
    
# Driver code
n = 5
k = 3
isKthBitSetleft(n, k)
isKthBitSetright(n,k)
 