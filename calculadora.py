def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    else:
        return a / b

def main():
    print("Calculadora Simples em Python")
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    operacao = input("Digite o número da operação: ")

    if operacao in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if operacao == '1':
            print("Resultado:", soma(num1, num2))
        elif operacao == '2':
            print("Resultado:", subtrai(num1, num2))
        elif operacao == '3':
            print("Resultado:", multiplica(num1, num2))
        elif operacao == '4':
            print("Resultado:", divide(num1, num2))
    else:
        print("Operação inválida.")

if __name__ == "__main__":
    main()
