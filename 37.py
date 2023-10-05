from time import sleep
from builtins import bin, oct, hex
print('')
print('Abaixo informe o numero correspondente\n'
      'para fazer a conversão: \n'
      '\n'
      '1 para Binario\n'
      '2 para Octal\n'
      '3 para Hexadecimal')
print('')

numero = int(input('Informe o numero correspondente de 1 a 3:'))

print('Iniciando...')
sleep(3)

if numero == 1:
    numeroB = int(input(' Digite um numero qualquer:'))
    print('Calculando...')
    sleep(3)
    print(' Opção escolhida "1"\n O numero {:.2f} convetido em Binario é {}'.format(numeroB, bin(numeroB)))

elif numero == 2:
    numeroO = int(input(' Digite um numero qualquer:'))
    print('Calculando...')
    sleep(3)
    print(' Opção escolhida "2"\n O numero {:.2f} convetido em Octal é {}'.format(numeroO, oct(numeroO)))

elif numero == 3:
    numeroH = int(input(' Digite um numero qualquer:'))
    print('Calculando...')
    sleep(3)
    print(' Opcão escolhida "3"\n O numero {:.2f} convertido em Hexadecimal é {}'.format(numeroH, hex(numeroH)))
