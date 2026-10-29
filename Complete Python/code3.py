#airthmetic op.
print(5+2)
print(5-2)
print(5*2)
print(5/2)
print(5//2) #Remove Decimal part from //
print(5%2)
print(5**2)

# Assignment op

CGPA=7.29
#CGPA=CGPA+2
CGPA+=2
print(CGPA)

CGPA=7.29
CGPA-=2
print(CGPA)

CGPA=7.29
CGPA*=2
print(CGPA)

CGPA=7.29
CGPA/=2
print(CGPA)

CGPA=7.29
CGPA%=2
print(CGPA)

CGPA=7.29
CGPA**=2
print(CGPA)

CGPA=7.29
CGPA//=2
print(CGPA)

#Operator Precidence : Priority of operator
# ()>*,/>+,->

# Comperision Op
print(3>2) # True
print(3>=2)
print(3<2) #False
print(3<=2)
print(3==2)
print(3!=2)


#Logical Op
# (OR,AND,NOT)
st1= 3>2
st2=3<2
print(st1 or st2)
print(st1 and st2)
print(not st1)

# Conditionals Statements
age=int(input("Enter Your Age"))
print(age)
if age>=18:{
    print("You Can Vote")
}
else:                              #elif Also We can use 
    {print("You Can't Vote")

}    

    Marks=int(input("Enter the Student Marks"))
    print(Marks)
    if Marks>=80:{
        print('A+')
    }
    elif Marks>=65:{
        print('A')
    }
    elif Marks>=50:{
        print('B')
    }
    elif Marks>=33:{
        print('C')
    }
    else:{
        print("Fail")
    }



