import random
def jogar():
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = percorrer_palavra(palavra_secreta)
    palavra_secreta, lista_oculta = percorrer_palavra(palavra_secreta)
    while(1):
        chute = pede_chute()
        retorno = verifica_chute(palavra_secreta, chute, lista_oculta)
        if retorno:
            print(lista_oculta)
        else:
            print('voce errou')
def carrega_palavra_secreta():
    arquivos_de_letras = open('palavras.txt', 'r')
    lista_palavras = []
    for palavra in arquivos_de_letras:
        lista_palavras.append(palavra.strip())
    indice_secreto = random.randint(0, 3)
    return lista_palavras[indice_secreto]

def pede_chute():
    chute = input('Digite uma letra para chute: ')
    chute = chute.strip()
    return chute
def percorrer_palavra(palavra):
    lista = []
    for letra in palavra:
        lista.append(letra)
    lista_oculta = ['-' for x in lista]    
    palavra_secreta = lista
    return palavra_secreta, lista_oculta

def verifica_chute(palavra_secreta, chute, lista_oculta):
    posicao = 0
    for letra in palavra_secreta:
        if chute == letra:
            lista_oculta[posicao] = chute
        posicao += 1
    if chute in palavra_secreta:
        return True
    else:
        return False

if __name__ == '__main__':
    jogar()
