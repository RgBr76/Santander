my_tuple = (1, 2, 3, 2, 4, 2)

print (my_tuple.index(2))   # Output: 1
print (my_tuple.index(2, 2))   #Output: 3
print (my_tuple.index(2, 2, 4))   #Output: 3

my_tuple2 = (1, 2, 3, 2, 4, 2, 5)
# my_tuple2 = list[] # error
print(my_tuple2)

print(my_tuple2.count(2))
print(my_tuple2.index(2))
print(my_tuple2.index(4, 2, 5 ))
print(len(my_tuple2))