def isprime(n):
    if n==0 or n==1:
        return False
    i=2
    root=pow(n, 1/2)
    while i<root:
        if n%i==0:
            return False
        i+=1
    return True


def count3divisors(n):
    i=2
    count=0
    while i*i<n:
        if(isprime(i)):
            print (i*i)
            count+=1
        i+=1
    return count


print(count3divisors(10))
        