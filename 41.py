from datetime import date

anoNascimento = int(input('Informe seu ano de nascimento:'))

anoAtual = date.today().year
idade = anoAtual - anoNascimento

if idade <= 9:
    print('Você tem {} ano(s) e está na categoria Mirim.'.format(idade))

elif idade >= 9 and idade <= 14:
    print('Você tem {} anos e está na categoria Infantil '.format(idade))

elif idade >= 15 and idade <= 19:
    print('Você tem {} anos e está na categoria Junior'.format(idade))

elif idade == 20:
    print('Você tem {} anos e está na categoria Sênior'.format(idade))

else:
    print('Você tem {} anos e está na categoria Master'.format(idade))
