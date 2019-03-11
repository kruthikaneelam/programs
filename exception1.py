try:
	print(s)
except:
	print("u hve error") 

try:
	s=1
	print(s)
except:
	print("u hve no error")

try:
	print(s)
except:
	print("u hve error")
else:
	print("o")
finally:
	print("success")
