# Importa a biblioteca math para realizar os cálculos das operações
import math


# Método que faz o cálculo da adição
def adicao(num1, num2):
    return num1 + num2


# Método que faz o cálculo subtração
def subtracao(num1, num2):
    return num1 - num2

# Método que faz o cálculo da multiplicação
def multiplicacao(num1, num2):
    return num1 * num2

# Método que faz o cálculo da divisão mas da erro se divide o segundo número por 0 
def divisao(num1, num2):
    if num2 != 0:
        print("\nDivisão possível de ser realizada")
        return num1 / num2
    else:
        print("\nDivisão não é possível de ser realizada")
        return None
# Faz um loop das opções até sair do programa
while True:
    print("\nOlá, seja bem-vindo à calculadora do Alexandre!" +
          "\nEscolha qual operação matemática deseja realizar:" +
          "\n1 - Adição" +
          "\n2 - Subtração" +
          "\n3 - Multiplicação" +
          "\n4 - Divisão" +
          "\n5 - Sair")

    # Digite um número de 1 a 5 para escolher uma opção 
    entrada = input("Digite a opção: ")

    if not entrada.isdigit():
        print("Opção inválida. Por favor, digite um número entre 1 e 5.")
        continue  # Se a entrada não for um número, continua no loop e pede novamente

    opcoes = int(entrada)

    # Finaliza o programa se a opção digitada for 5 
    if opcoes == 5:
        print("Saindo...")
        break

    if opcoes not in [1, 2, 3, 4]:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        continue  # Se a opção não for 1,2,3 ou 4, volta para o início do loop e pede a opção novamente

    # Solicita os números apenas se a opção for válida
    num1 = float(input("\nDigite o primeiro número a ser calculado: "))
    num2 = float(input("\nDigite o segundo número a ser calculado: "))

    # Usando o match para escolher as operações e chamando os métodos:
    match opcoes:
        case 1:
            resultado = adicao(num1, num2)
        case 2:
            resultado = subtracao(num1, num2)
        case 3:
            resultado = multiplicacao(num1, num2)
        case 4:
            resultado = divisao(num1, num2)

    # Só imprimir o resultado se uma operação válida foi realizada
    if resultado is not None:
        print("\nO resultado é:", resultado)
    else:
        print("\nOperação inválida devido a erro.")