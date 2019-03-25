fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)


def reverse(s):
	str=""
	for i in s:
		str=i+str
	return str
s=str(input("enter name"))
print("name is:")
print(s)
print("reversed name is:")
print(reverse(s))