x=(input("enter num"))
y=(input("enter num"))
z=(input("enter num"))
def sum(x,y,z):
  if x==y:
    return 0
  elif x==z:
    return 0
  elif y==z:
    return 0
  else:
    return x+y+z
v=sum(x,y,z)
print(v)