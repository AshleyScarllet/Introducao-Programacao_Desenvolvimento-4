operadores = ("+", "-", "x", "/")
num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
operador = str(input(f"Digite o operador, sendo ele {operadores}: "))

operacao_inexistente = operador not in operadores

if operacao_inexistente:
    print("0")
elif operador == "+":
    print(num_1 + num_2)
elif operador == "-":
    print(num_1 - num_2)
elif operador == "x":
    print(num_1 * num_2)
elif operador == "/":
    print(num_1 // num_2)