# METHOD-1
n=4
multi=1
for i in range(n,1,-1):
    multi=multi*i
print(multi)


#METHOD-2
''' RECURSIVE FUNCTION'''
''' TIME COMPLEXITY: O(n)'''
def fact(n1):
    if n1==1:
        return 1
    return n1*fact(n1-1)


n1=5
print(fact(n1))

