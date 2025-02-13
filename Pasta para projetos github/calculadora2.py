import tkinter as tk
import math

def calcular(operacao):
    try:
        n1 = float(entry1.get())  
        n2 = float(entry2.get()) if operacao != "√" else 0  

        if operacao == "+":
            resultado = n1 + n2
        elif operacao == "-":
            resultado = n1 - n2
        elif operacao == "x":
            resultado = n1 * n2
        elif operacao == "/":
            resultado = "Erro" if n2 == 0 else n1 / n2
        elif operacao == "^":
            resultado = n1 ** n2
        elif operacao == "√":
            resultado = math.sqrt(n1)
        else:
            resultado = "Inválido"
        
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Erro: Insira números válidos!")

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora Simples")
root.geometry("300x400")

# Entradas
entry1 = tk.Entry(root, font=("Arial", 12))
entry1.grid(row=0, column=0, columnspan=2, pady=10)

entry2 = tk.Entry(root, font=("Arial", 12))
entry2.grid(row=1, column=0, columnspan=2, pady=10)

# Botões das operações
botoes = [
    ("+", 2, 4), ("-", 3, 4), 
    ("x", 4, 4), ("÷", 5, 4), 
    ("^", 5, 4), ("√", 6, 4)
]

for texto, linha, coluna in botoes:
    tk.Button(root, text=texto, font=("Arial", 14), width=5, command=lambda t=texto: calcular(t)).grid(row=linha, column=coluna, pady=5)

# Label para exibir o resultado
label_resultado = tk.Label(root, text="Resultado: ", font=("Arial", 12), fg="black")
label_resultado.grid(row=5, column=0, columnspan=1, pady=10)

# Inicia o loop da interface gráfica
root.mainloop()
