#  TypeCasting

age = input("Enter Your age")
print("Age=",age)
print(type(age))
 #  We can't concenate with the string  --->   print (age+1)

new_age = int(age) +1
print(new_age)

#TypeConversion 
print(5+1.5) # Implicit
#TypeCasting
print(5+int(1.5)) # Explicit

#Sum Program
a=input("Enter a")
b=input("Enter b")
sum=(int(a)+int(b))  #----> sum=(a+b) As a string add ho jata hai
print(sum)

# Strings Method
name = "hari"
grade='A'
#Sting Operations
print("UpperCase:",name.upper())
print("LowerCase:",name.lower())
# String are Immutable (Don't Chage in real string)
print(name.find("ari")) #Index Hoke AA Jayega
print(name.replace("hari","Hariom"))
#Presence
print('s'in name)  # in is a KeyWord
print('a'in name)

# KeyWords True,in,False,While,for,break,continue

