#finding max number
def max(a,b,c):
	if(a>b) and (a>c):
		largest=a
	elif(b>a) and  (b>c):
		largest=b
	else:
		largest=c
		print(largest)
max(1,2,3)

#input value in output
a=int(input("enter the numbers:a"))
b=int(input("enter the numbers:b"))
c=int(input("enter the numbers:c"))
def max(a,b,c):
	if(a>b) and (a>c):
		print("max is:",a)
	elif(b>a) and  (b>c):
		print("max is:",b)
	else:
		print("max is:",c)
max(a,b,c)