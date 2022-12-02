def soma (numero1,numero2):
    return float (numero1) + float (numero2)
def sub (numero1,numero2):
    return float (numero1) - float (numero2)
def mult (numero1,numero2):
    return float (numero1) * float (numero2)
def div (numero1,numero2):
    if numero2 == '0':
        print( 'O numero 2 não pode ser 0')
        print ('Você digitou um operador inválido')
        global repetir
        repetir = True
    else:
        return float (numero1) / float (numero2)
def calculadora(n1,n2,op):
    if(op == '+'):
        print (soma(n1,n2))
    elif (op == '-'):
        print (sub(n1,n2))
    elif (op == '*'):
        print (mult(n1,n2))
        print (div(n1,n2))
    
    repetir = True
    while repetir == True:
        num1 = input( 'Escreva o numero 1: ')
        num2 = input( 'Escreva o numero 2: ')
        operador = input ('Escreva o op(+,-,*,/): ')
        if num1.isnumeric() and num2.isnumeric ():
            repetir = False
            calculadora (num1,num2,operador)
        else:
            repetir = True
            print('Você digitou um numero invalido')


