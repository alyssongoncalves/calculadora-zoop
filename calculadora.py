while True:
    operacao = input('Qual operação (+,-,*,/) você quer fazer ou \'exit\' para sair? ')
    if operacao == 'exit':
        break
    elif operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':
        operando1 = int(input('Digite o primeiro numero: '))
        operando2 = int(input('Digite o segundo numero: '))
    else:
        print('Operacao invalida')
 
    if operacao == '+':
        total = operando1 + operando2
        print(total)
    elif operacao == '-':
        total = operando1 - operando2
        print(total)
    elif operacao == '*':
        total = operando1 * operando2
        print(total)
    elif operacao == '/':
        total = operando1 / operando2
        print(total)