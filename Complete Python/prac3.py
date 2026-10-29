a=int(input("Enter the Value of a:"))
op=input("Choose the operator:")
b=int(input("Enter the Value of b:"))
# op= '+','-','*','%','**' No Need 
if op=='+':{
    print(a+b)
}
elif op=='-':{
    print(a-b)

}
elif op=='*':{
    print(a*b)
}
elif op=='%':{
    print(a%b)
}
elif op=='**':{
    print(a**b)
}
else:{
    print("Somting Wrong Try Again!")
}


