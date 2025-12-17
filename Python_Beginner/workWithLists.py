# List methods
fruits = ["apple", "orange", "pear"]
print(fruits)

fruits.append('grape') #only add
print(fruits)

fruits.insert(0, "mango") #add on a specific position
print(fruits)

fruits.remove('orange') #only remove
print(fruits)

removed_fruit = fruits.pop(2) #remove on a specific position
print(fruits)
print(removed_fruit)

fruits.sort() #ascending order
print(fruits)

fruits.reverse() #reverse the order
print(fruits)

numbers = [1 ,2 ,3 ,4 ,5]
squares = [x ** 2 for x in numbers if x % 2 == 0 ]
print(numbers)
print(squares)