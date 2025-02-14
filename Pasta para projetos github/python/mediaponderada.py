x = int(input("Digite um número:"))

for i in range(1,x):
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())

    multi1 = n1*2
    multi2 = n2*3
    multi3 = n3*5

    somamulti = multi1 + multi2 + multi3
    somapesos = 2 + 3 + 5

    resultado = somamulti / somapesos
    print(f"O resultado é: {resultado:.1f}")
