# Creating a list
fruits = ["apple", "banana", "mango"]

# Accessing
print(fruits[0])  # apple

# Editing
fruits[1] = "orange"
print(fruits)

# Deleting
del fruits[2]
print(fruits)

# List Methods
#append()
fruits.append("grape")
print(fruits)
#insert()
fruits.insert(1, "cherry")
print(fruits)
#remove()
fruits.remove("apple")
print(fruits)

# String Methods on elements
print(fruits[0].upper())  # CHERRY
