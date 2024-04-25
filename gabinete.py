class Gabinete:
    def __init__(self, preco, marca, modelo, tamanho, fontebaixo):
        self.__preco = float(preco)
        self.__marca = marca
        self.__modelo = modelo
        self.__tamanho = float(tamanho) # em cm
        self.__fontebaixo = bool(fontebaixo)
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, preco):
        self.__preco = float(preco)
    
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):
        self.__marca = marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo
    
    @property
    def tamanho(self):
        return self.__tamanho
    
    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = float(tamanho)
    
    @property
    def fontebaixo(self):
        return self.__fontebaixo

    @fontebaixo.setter
    def fontebaixo(self, fontebaixo):
        self.__fontebaixo = bool(fontebaixo)
    
    def info(self):
        print(f'Preço: R$ {self.__preco}\nMarca: {self.__marca}\nModelo: {self.__modelo}\nTamanho: {self.__tamanho}\nFonte em baixo: {self.__fontebaixo}')
