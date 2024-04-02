from operators import *

#User Input
a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
op=input("Enter the operator: ")

#Conditional Call
if(op=="+"):
  sum(a,b)

elif(op=="-"):
  dif(a,b)

elif(op=="*"):
  prod(a,b)

elif(op=="/"):
  quo(a,b)

elif(op=="%"):
  rem(a,b)

else:
  print("Invalid Operator")