senha = int(input("Digite a senha: "))

while senha != 2002:
    print("Senha incorreta. Tente na próxima.")
    senha = int(input("Digite a senha: "))
    if senha == 2002:
        print("Senha correta.")
        break
