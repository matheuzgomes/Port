def plusOne(number):
    div = int(input("Agora o segundo número: "))
    return number / div


def plusTwo(number):
    div = int(input("Agora o segundo número: "))
    return number * div


def plusThree(number):
    div = int(input("Agora o segundo número: "))
    return number + div


def plusFour(number):
    div = int(input("Agora o segundo número: "))
    return number - div


ope = int(input("Escolha a operação, 1 para divisão / 2 para multiplicação / 3 para soma / 4 para subtração: "))

if ope == 1:
    print(plusOne(int(input("Você escolheu divisão, escolha o primeiro número da operação: "))))

elif ope == 2:
    print(plusTwo(int(input("Você escolheu multiplicação, escolha o primeiro número da operação: "))))

elif ope == 3:
    print(plusThree(int(input("Você escolheu soma, escolha o primeiro número da operação: "))))

elif ope == 4:
    print(plusFour(int(input("Você escolheu subtração, escolha o primeiro número da operação: "))))

