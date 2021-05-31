import random
contador = 0

while contador < 5:
    contador += 1
    
    aleatorio = random.randint(0,10)
    numero = input('Dige um número: ')

    if numero == aleatorio:
        print(f'Você acertou!') 
    else:
        print(f'Você errou, o número era {aleatorio}')