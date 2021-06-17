import random

while True:
    aleatorio = random.randint(0,10)
    numero = int(input('Dige um número: '))
    if numero == aleatorio:
        print(f'Você acertou {numero}')
        break
    else:
        print(f'Você errou, digitou {numero} e deu {aleatorio}')