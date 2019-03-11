def sum_list(a):
	i = 0
	for e in a:
		i = i+e
	return i

a = []
n= int(input("Number of element in list"))

for k in range(n):
	el = int(input("Give the elements of list"))
	a.append(el)

i = sum_list(a)

print(i, "is the sum of list")