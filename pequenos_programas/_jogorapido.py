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
        print(lista_oculta)
        return True
    else:
        print('nao encontrei')
        False


a, c = percorrer_palavra('brasil')
verifica_chute(a, 'a', c)
verifica_chute(a, 'p', c)
verifica_chute(a, 'l', c)
verifica_chute(a, 'e', c)
verifica_chute(a, 'z', c)

