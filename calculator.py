from operators import *

while(True):
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
	repeat=input('do you want to try again(yes/no): ')
  	if(repeat.lower()=='no'):
    		break
  	else:
    		pass