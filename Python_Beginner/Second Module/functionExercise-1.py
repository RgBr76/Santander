inventario = {}

print('---------------------------------')
print('---- Bem-vindo ao inventário ----')
print('---------------------------------')

while True:

    escolha = int(input('Escolha sua ação: \n' +
    '1 - Adicionar item \n' +
    '2 - Atualizar item \n' +
    '3 - Deletar item \n' +
    '4 - Calcular totais \n'+
    '5 - Mostrar inventário \n'+
    '0 - Sair --> '))


    def adicionarItem(): # Funciona
        nome = str(input('Nome do item: '))
        if(nome != ""):
            qntd = int(input('Quantidade: '))
            categoria = str(input('Categoria: '))
            valor = int(input('Valor unitário: '))
            inventario[nome] = (qntd, categoria, valor)

    def atualizarItem():
        nome = str(input("Coloque o nome do item que deseja atualizar: "))
        if(nome in inventario):
            qntd = int(input('Quantidade atualizada: '))
            categoria = str(input('Categoria atualizada: '))
            valor = int(input('Valor unitário atualizado: '))
            inventario[nome] = (qntd, categoria, valor)
        else:
            print("Item não encontrado")

    def deletarItem():
        nome = str(input('Qual o item a ser deletado: '))
        if nome in inventario:
            del inventario[nome]
            print('Deletado com sucesso!')
        else:
            print('Item não encontrado!')

    
    def valorTotalInventario():

        # Empacotamento e desempacotamento de tupla
        # Então:
        # quantidade, categoria, valor_unitario = valor

        # # É equivalente a:
        # quantidade = valor[0]      # 10
        # categoria = valor[1]       # 'Fruta'
        # valor_unitario = valor[2]  # 2.50

        ac = 0
        for chave, valor in inventario.items(): #Função para as chaves do dicionário
            quantidade, categoria, valor_unitario = valor
            valor_total = quantidade * valor_unitario
            ac += valor_total

        return print(ac)

    def mostrarInventario():
        i = 1
        for chave, valor in inventario.items():
            print(f'Item {i}: {chave} | Qntd: {valor[0]} | Categoria: {valor[1]} | Valor unitário: {valor[2]}')
            i +=1

    match escolha:
        case 1:
            adicionarItem()
        case 2:
            atualizarItem()
        case 3:
            deletarItem()
        case 4:
            valorTotalInventario()
        case 5:
            mostrarInventario()
        case 6: 
            break
        case _:
            print('Nenhuma opção escolhida')
