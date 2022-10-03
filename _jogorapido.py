class Mercadoria:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.promo = True
    def funcaomercadoria(self):
        print(self.promo)
class Carnes(Mercadoria):
    def __init__(self, tipo, peso):
        self.tipo = tipo
        self.peso = peso
class Utensilios:
    def __init__(self, espetos, carvao):
        self.espetos = espetos
        self.carvao = carvao
        self.tamanho = '5kg'
class Kitchurras(Carnes, Utensilios):
    pass

pacote1 = Kitchurras('Carne', '1kg')
#pacote1.nome = 'Costela'
#pacote1.preco = 14.90
# pacote1.peso = '1kg'
# pacote1.carvao = True
pacote1.espetos = 'Carne, Frango'
print(pacote1.peso)