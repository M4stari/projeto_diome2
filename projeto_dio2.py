#DESAFIO 2#

meses = ['January','February','March','April','May','June','July','August','September','October','November','December']

numero_mes = int(input('Digite o Número do mês:'))

if(numero_mes < 1 or numero_mes > 12):
  print('Numero invalido, Digite um numero entre 1 e 12')

else:
  
  nome_mes = meses[numero_mes - 1]
  print(nome_mes)