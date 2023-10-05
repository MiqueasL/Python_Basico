from datetime import date

anoAtual = date.today().year
anoNascimento = int(input('Qual seu ano de nascimento:'))


idade = anoAtual - anoNascimento


print('Você nasceu em {} tem {} anos em {}'.format(anoNascimento, idade, anoAtual))

if idade < 18:
    tempoA = 18 - idade
    print('Ainda falta {} ano para você se alistar'.format(tempoA))
    anoA = anoAtual + tempoA
    print('Seu ano de alistamento será em {}'.format(anoA))

elif idade == 18:
    print('Você tem que se alistar imediatamente')

elif idade > 18:
    tempoB = idade - 18
    print('Você já deveria ter se alistado a {} ano(s)'.format(tempoB))
    anoB = anoAtual - tempoB
    print('Você deveria ter se alistado no ano de {}'.format(anoB))
