# METHOD-1
''' IF THE NUMBER HAS REMAINDER 1 THEN THE COUNT INCREASES
    OTHERWISE IT DOES NOT INCREASE.'''
''' TIME COMPLEXITY: O(LOG N)'''
n1=5
count1=0
while n1>0:
    if(n1%2!=0):
        count1+=1
    n1=n1//2
print(count1)







# METHOD-2
'''  BRIAN KERNINGAN'S ALGORITHM:   '''
'''IN THIS METHOD  LAST  SET BIT(1) FROM RIGHT BECOME 0 
   AND USING AND OPERATOR IT GIVES ASSIGN A VALUE WITH SAME NO. OF SET BIT IN ORIGINAL-RIGHT BIT
   AND AT END IT BECOME A NIL OR 0 VALUE.'''

'''TIME COMPLEXITY = O(NO. OF SET BIT)'''
n2=40
count2=0
while n2>0:
    n2=(n2 & (n2-1))
    count2+=1
print(count2)





