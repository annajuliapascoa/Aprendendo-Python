v = float(input('Qual a velocidade atual do carro? '))
if v <= 80:
  print('Tenha um bom dia e dirija com cuidado!')
else:
  print('MULTADO! Você utrapassou o limite de velocidade de 80km/h!')
  print('Você terá que pagar um multa de R${:.2f}!'.format(7.00 * (v - 80)))