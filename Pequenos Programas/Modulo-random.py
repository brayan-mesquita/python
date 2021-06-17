import random

number = [34, 23, 54, 24, 53] #lista de numeros
sequencia = [] # lista vaziqa
for x in range(6):
    if x == 5:
        print(sequencia)
    sequencia.append(random.choice(number))


    


# valores entre 0 e 1 nao incluido este
#print(random.random())

#imprime valores inteiros, conforme especificado
#print(random.randint(1, 10))

