product = {
    'nome': 'Mouse',
    'preco': 50.00,
    'estoque': 10
}
print(product) #Debuger

new_key = {'category': ""}
product.update(new_key)

print(product) #Debuger

#Parte 2

vendas = [10.50, 20.00, 5.00, 50.00]

# i = 0

# for num in vendas:
#     vendas[i] = num * 1.1

#     i += 1

#Ou, de maneira mais eficiente

vendas_com_taxa = [num * 1.1 for num in vendas]

print(vendas)
print(vendas_com_taxa)
    