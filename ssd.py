from armazenamento import Armazenamento

class Ssd(Armazenamento):
    def __init__(self, espaco, voltagem, leitura, nvme, preco, marca, modelo):
        Armazenamento.__init__(self, espaco, voltagem)
        self.__leitura = float(leitura)
        self.__nvme = bool(nvme) # True ou False
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
    def nvme(self):
        return self.__nvme
        
    @nvme.setter
    def nvme(self, nvme):
        self.__nvme = bool(nvme)
        
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

    def infoSsd(self):
        print(f'Preço: R$ {self.__preco}\nMarca: {self.__marca}\nModelo: {self.__modelo}\nEspaço: {self.__espaco} GB\nVoltagem: {self.__voltagem}\nLeitura: {self.__leitura}\nNVME: {self.__nvme}')
