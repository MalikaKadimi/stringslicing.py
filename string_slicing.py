
name = "malika"
print(name[0:4])
print(name[1:5])
print(name[ : ])
print(name[1:])

#reverse a string

name = "kadimi"
str = (name[::-1])
print(str)

# reverse a string without slicing

name = "malika"
str = "".join(reversed(name))
print(str)

# reverse a list items

names = list(("malika","bhavya","priyam"))
print(names[::-1])