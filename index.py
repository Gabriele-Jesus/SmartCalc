# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão
# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        return num1 / num2
    if num2 != 0:
        return num1/num2
    else:
        return " O número de operação não existe"
    
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
operacao = int(input("Digite a operação (1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão)"))

resultado = calculadora(num1, num2, operacao)
print(f"Resultado: {resultado}")
   