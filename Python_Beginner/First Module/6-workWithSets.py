# fruits = {'Apple', 'Banana', 'Orange'}
# numbers = set([1, 2, 3, 4, 5])

# print(fruits)
# print(numbers)

set1 = {1, 2, 3, 6}
set2 = {2, 3, 4, 5, 6}

union = set1 | set2
print(union) #Ele junta e exclui repetidos

intersection = set1 & set2
print(intersection) #Mostra os itens que são iguas em ambos os sets.

difference = set1 - set2
print(difference) #Mostra apenas os itens que estão do lado do set1 e que não foram cortas após a diferença

symmetric_difference = set1 ^ set2
print(symmetric_difference) #Mostra os itens que não são repetidos

#Set methods

fruits = {'Apple', 'Banana', 'Orange'}

fruits.add("Pear")
print(fruits)

fruits.remove("Banana")
print(fruits)

fruits.discard("Grape") #Discard remove apenas se existir, se usar o remove dá erro
print(fruits)

fruits.clear()
print(fruits)