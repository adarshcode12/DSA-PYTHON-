s='abc'
length=len(s)
power=pow(2,length)
for i in range(power):
    for j in range(length):
        if i & (1 << j)!=0:
            print(s[j],end=' ')
    print('\n')