#fileName:CompareDemo01
import random
print("begin run")
def compareNum(num1,num2):
    if(num1>num2):
        return 1
    elif(num1==num2):
        return 0
    else:
        return -1
print ("end run function")
num1=random.randrange(1,10,2)
num2=random.randrange(1,10,1)
print ("num1=",num1)
print ("num2=",num2)
x=compareNum(num1,num2)
print x