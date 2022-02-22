while True:
    print()
    num1 = input('Digite um número: ')
    operador = input('Digite o operador (+,-,*,/): ')
    num2 = input('Digite um número: ')
    
    if not num1.isnumeric() or not num2.isnumeric():
        print('Escreva um número valido!')
        continue
    if not operador == '+' or not '-' or not '*' or not '/':
        print('Escreva uma operação valida!')

    num1 = float(num1)
    num2 = float(num2)
    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '*':
        print(num1 * num2)
    elif operador == '/':
        print(num1 / num2)
    print()
    sair = input('Você deseja sair? [s]im [n]ão:')

    if sair == 's':
        break
