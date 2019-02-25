import random
l=["r","p","s"]
while True:
	i=input("enter your choice,press n to discont")
	if i=="n":
		print("game over")
		exit()
	c=random.choice(l)
	print("computer chooses",c)
	if i==c:
		print("tie")
	elif i=="r" and c=="p":
		print("computer won")
	elif i=="r" and c=="s":
		print("you won")
	elif i=="p" and c=="r":
		print("you won")
	elif i=="p" and c=="s":
		print("comp won")
	elif i=="s" and c=="r":
		print("comp won")
	elif i=="s" and c=="p":
		print("you won")

