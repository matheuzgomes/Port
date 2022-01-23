
operation = 0
prod_list = []
while operation < 6:
    operation += 1


    def Prod(product):
        descrip = str(input("Insira uma descrição para o produto: "))
        price = int(input("Adicione agora um valor para o produto: " + 'R$ '))
        sell = int(input("Disponível para a venda? 1 - sim / 2 - não  "))
        prod_list.append(product)
        prod_list.append(price)
        print(prod_list)
        return product, descrip, price, sell

    ope = int(input("Bem vindo ao cadastro da Oak, deseja cadastrar um novo produto? 1 para sim, 2 para não:  "))

    if ope == 1:
        print(Prod(str(input("Favor Digitar o nome do produto: "))))
    else:
        print("Obrigado e volte sempre")



