# josephus recurssive algorithm

"""in this algorithm we have to 
    in each recurssive the loop start from 0 again
    so we we add +k in return as next count for kill should
    start from kth term 
    also, the return can become more than n so we have to do 
    %n"""
    
    
def josh(n,k):
    if n==1:
        return 0
    return (josh(n-1,k)+k)%n

print(josh(6,3))