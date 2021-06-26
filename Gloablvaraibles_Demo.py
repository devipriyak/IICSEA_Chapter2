def factorial(number):
      fact=1
      for i in range(1,number+1):
            fact=fact*i

      print "fact %d is %d" %(s,fact)
def printS():
      print "Gloabal variable s is %d" %s#print gloabal varaible s

s=int(raw_input("Enter number"))#s scope is started from this statement
factorial(s)#accept
printS()#accept
#Global Variable Accessed from any function
