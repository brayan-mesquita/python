# palavra = list('brayan')
# ocultar = ['-' for x in palavra]
# s = '-'
# print(f'{s.join(palavra)}')
import random
def carrega_palavra_secreta():
    arquivos_de_letras = open('palavras.txt', 'r')
    lista_palavras = []
    for palavra in arquivos_de_letras:
        lista_palavras.append(palavra.strip())
    indice_secreto = random.randint(0, (len(lista_palavras)+1))
    return len(lista_palavras)+1
    #return lista_palavras[indice_secreto]
print(carrega_palavra_secreta())