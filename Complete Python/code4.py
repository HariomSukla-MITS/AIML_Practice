# range
num= range(5)  #[ 0,1,2,3,4,]
print(num) # 5 is Excluded

# 1 t0 5
range(1,6)
# range(start(by default 0),end,step(by default +1))

#While loop
#loop: Repeatation
n=1;
while n<=5:
    print(n,"Hariom")
    n +=1    # if can't Write so Infinite loop run Here.


# for loop
num=range(5)
for i in num:
    print(i)


# for i in range(5):
#     print(i)

# 1 to 10 even num
for i in range(1,11):
    if i%2==0:
        print(i,"Even Num")
# for i in range(2,11,2):   Here print 2,4,6,8,10
#print(i)

# Break & Continue
#Multiples of 3 stop 0n 21 ; range (1,50)
for i in range(1,51):
    if i==21:
        break
    if i%3==0:
        print(i)

print("Out Of Loop")  

# Continue

# for i in range(1,51):
#     if i==21:
#         continue
#     if i%3==0:
#         print(i)

# print("Out Of Loop")   


