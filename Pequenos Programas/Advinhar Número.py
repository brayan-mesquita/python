import random
aleatorio = random.randint(0,10)
numero = input('Dige um número: ')

if numero == aleatorio:
    print(f'Você acertou!') 
else:
    print(f'Você errou, o número era {aleatorio}')