a = int(input('Primeiro Numero:'))
b = int(input('Segundo Numero:'))

if a > b and b < a:
    print('O primeiro numero e maior')

elif b > a and a < b:
    print('O segundo numero e maior')

elif a == b and b == a:
    print('Os numeros são iguais')
