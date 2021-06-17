texto = input('Digite o texto:')
caso = 0
while caso != 3:
    caso = input('1 para Maiuscúlo \n2 para Capitalize\n3 para sair')
    if caso == '1':
        print(texto.upper())
    if caso == '2':
        print(texto.capitalize())
    if caso == '3':
        break