#function : Block of code
#Calculate of 2 num sum

def sum (a,b): # Define the function
    print(a+b)
print(sum(3,5)) # call the  fuction

# GST Function
def cal_gst(old_price):   # old_price is our parameters
    new_price=old_price + old_price*0.18
    print(new_price)
    #return new_price    -->Value print bhi krwana hoga agr hum return karate hai tb
print(cal_gst(100))   # 100 is a our arguments

#Type of function 1. user defined function (Already disscussed) 2.  inbuild Function Ex. print(),range(),len(),min(),type(),max(),etc.
# 3. Module Function : Bundle of Related thing
import math
print(dir(math))

from math import sqrt, log2
print(sqrt(16))
print(log2(16))

import random
print(random.random()) #0 to 1
print(random.randint(1,20))
