
set1={1,2,3,4,5,6,7,24,25,26}
set2={1,2,3,4,5,6,7,8,9,10,11,12,13,14}
'''#Subset or not verification
print "Is the set1 is sub set of Set2:%s" %set1.issubset(set2)
print "set1<set2 %s" %(set1<set2)
#SuperSet Verification

print "Is the set1 is super set of Set2:" ,set1.issuperset(set2)
print "set1>set2 %s" %(set1>set2)
#Symmetric Differenece
'''
res=set1.symmetric_difference(set2)
print("Symmetric Difference two sets are %s" %res)
print("Set1^Set2 %s" %(set1^set2))
'''
 set([8, 9, 10, 11, 12, 13, 14, 24, 25, 26])

'''


