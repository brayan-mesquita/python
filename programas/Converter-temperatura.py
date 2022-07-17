entrada = input('Conversão de F em C: ')
try:
    conversao = (float(entrada) - 32.0) * 5.0 / 9.0
    print(conversao)
except:
    print('Digite um número')