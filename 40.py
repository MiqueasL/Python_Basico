n1 = float(input('Primeira Nota:'))
n2 = float(input('Segunda Nota:'))
n3 = float(input('Terceira Nota:'))

media = (n1 + n2 + n3) / 3

if media < 5:
    print('Reprovado Media {:.2f}'.format(media))

elif media >= 5 and media <= 6.9:
    print('Recuperação Media {:.2f}'.format(media))

elif media > 6.5:
    print('Aprovado Media {:.2f}'.format(media))