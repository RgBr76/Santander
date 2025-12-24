estoque = [
    {'nome': 'Teclado', 'preco': 150, 'categoria': 'periferico'},
    {'nome': 'Mouse', 'preco': 80, 'categoria': 'periferico'},
    {'nome': 'Monitor', 'preco': 900, 'categoria': 'video'}
]
print(estoque)

new_item = {'nome': 'Headset', 'preco': 200, 'categoria': 'periferico'}

estoque.append(new_item)

print(estoque)
# new_item = {'nome':'Headset', 'preco': 200, 'categoria': 'periferico'}
# estoque.update(new_item)
# print(estoque)

print(estoque[1]['nome']) #Especificamente pega a posição 1 da lista, e o nome da chave 'nome' do dicionário
 
