while True:
    texto = input('Digite o texto:')
    caso = input('1 para Maiuscúlo \n2 para Capitalize.')
    if caso == '1':
        print(texto.upper())
    if caso == '2':
        print(texto.capitalize())
    if caso == '3':
        break