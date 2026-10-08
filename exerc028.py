import random
from time import sleep
computador = random.randint(0, 5)

print('--' * 30)
print("Vou escolher um número entre 0 e 5. Tente adivinhar...")
print('--' * 30)
e = int(input("Em que número eu pensei? "))
print('PROCESSANDO...')
sleep(3)
if e == computador:
  print('\033[1;32mParabéns, você ganhou!')
else:
  print('\033[1;31mGANHEI! Pensei no número {}'.format(computador)) 