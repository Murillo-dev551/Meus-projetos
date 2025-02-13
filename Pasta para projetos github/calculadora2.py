import math
operacoes = "+,-,x,/."
print("Temos essas operaçãoes disponíveis: +,-,x,/,^,^^(Os dois últimos são potencia e radiciação).")
while True:
    n = int(input("Número: "))
    operacao1 = input("Qual operação deseja? ")
    n2 = int(input("Número2: "))

    if operacao1 == "+":
        soma = n+n2
        print(soma)
    elif operacao1 == "-":
        sub = n-n2
        print(sub)
    elif operacao1 == "x":
        multi = n*n2
        print(multi)
    elif operacao1 == "/":
        if n2 == 0:
            print("Essa divisão é inválida")
        divi = n/n2
        print(divi)
    elif operacao1 == "^":
        poten = n**n2
        print(poten)
    elif operacao1 == "^^":
        raiz = math.sqrt(n)
        print(raiz)
    else:
        print("Acabou")
        break