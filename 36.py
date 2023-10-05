from time import sleep

print('* Iniciando *')
sleep(3)
print(' Insira os dados requeridos abaixo:')

valorCasa = float(input(' Iforme o valor da casa ?'))
salario = float(input(' Qual a sua renda mensal ?'))
parcelasAnos = int(input(' Em quantos anos sera dividido ?'))

prestacao = valorCasa / parcelasAnos

limiteSalario = (30 * salario) / 100

if prestacao >= limiteSalario:
    print('Credito Negado o valor ultrapassa os 30% da renda mensal.')
else:
    print('Credito aprovado, Total de parcelas {}X no valor de {:.2f}.'.format(parcelasAnos, prestacao))
