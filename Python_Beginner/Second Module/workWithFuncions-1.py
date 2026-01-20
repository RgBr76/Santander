def greeting():
    print("Hello, world!")


greeting()  # Prints "Hello, world!"

def greeting_2(name):
    print(f"Hello, {name}!")

greeting_2('John')
greeting_2('Maria')

def sum(a, b):
    return a + b

result = sum(7, 9)
print(result)

def sum_2(c, d):
    result = c + d
    return print(f'O resultado da soma é {result}')

sum_2(3, 7)

#Funções anônimas

square = lambda x: x ** 2 #Função concisa em uma linha
print(square(5))  # Prints 25

cube = lambda s: s ** 3
print(cube(2))