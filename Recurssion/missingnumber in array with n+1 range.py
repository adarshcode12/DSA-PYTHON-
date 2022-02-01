n=[1,5,3,7,4,8,6]
simi=0
for i in n:
    simi=simi+i
    
l=len(n)+1
original=(l*(l+1))//2
missing=original-simi
print(missing)


