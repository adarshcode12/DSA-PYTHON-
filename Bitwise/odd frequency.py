#METHOD-1
'''TIME COMPLEXITY: O(N^2)'''

arr=[1,1,3,2,5,2,3,8,5,3]
freq=[]
for i in range(len(arr)):
    count=1
    if arr[i]!=-1:
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                arr[j]=-1
                count+=1
        print(arr[i],'--->',count)
        
        

#METHOD-2
'''USING PYTHON DICTONARY WE CAN USE KEY TO KEEP A COUNT IN THE ARRAY'''        
a=[1,1,3,5,5,9,3,3,9,4,2,6,8,3]
x={}
for i in a:
    if i in x:
        x[i]+=1
    else:
        x[i]=1
print(x)


#METHOD-3     ''TO COUNT PRINT FREQUENCY OF ODD ELEMENT''

count=0
for i in a:
    count=count ^ i
print(count)