from armazenamento import Armazenamento

class Hd(Armazenamento):
    def __init__(self, espaco, voltagem, leitura, rpm, preco, marca, modelo):
        Armazenamento.__init__(self, espaco, voltagem)
        self.__leitura = float(leitura)
        self.__rpm = float(rpm)
        self.__preco = float(preco)
        self.__marca = marca
        self.__modelo = modelo
    
    @property
    def leitura(self):
        return self.__leitura
    
    @leitura.setter
    def leitura(self, leitura):
        self.__leitura = float(leitura)

    @property
    def rpm(self):
        return self.__rpm
    
    @rpm.setter
    def rpm(self, rpm):
        self.__rpm = float(rpm)

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
    
    def infoHd(self):
        print(f'Preço: R$ {self.__preco}\nMarca: {self.__marca}\nModelo: {self.__modelo}\nEspaço: {self.__espaco} GB\nVoltagem: {self.__voltagem}\nLeitura: {self.__leitura}\nRPM: {self.__rpm}')
