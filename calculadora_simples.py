#Transformando pseudocódigo em códifo
#Atividade pseudocódigo 2 da Data Science Academy por Mayra Silva

def simple_calculator():

    print('Bem-vindo à Calculadora')

    operand_1 = float(input('Insira o primeiro número: '))
    operand_2 = float(input('Insira o segundo número: '))
    operator = input('Selecione a operação (+, -, *, /): ')
    result = 'Não foi possível calcular'



    if operator == '+':
        result = operand_1 + operand_2
    
    elif operator == '-':
        result = operand_1 - operand_2

    elif operator == '*':
        result = operand_1 * operand_2

    elif operator == '/':
        result = operand_1 / operand_2

    else:
        print('Operação Inválida')

    print(f'O resultado da operação é: {result}')

    return

simple_calculator()