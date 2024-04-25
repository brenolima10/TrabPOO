class Pdvideo:
    def __init__(self, preco, marca, modelo, nucleos, frequencia, memoria, ddr, voltagem):
        self.__preco = float(preco)
        self.__marca = marca
        self.__modelo = modelo
        self.__nucleos = int(nucleos)
        self.__frequencia = float(frequencia)
        self.__memoria = float(memoria)
        self.__ddr = int(ddr)
        self.__voltagem = float(voltagem)

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
    def nucleos(self):
        return self.__nucleos
    
    @nucleos.setter
    def nucleos(self, nucleos):
        self.__nucleos = int(nucleos)
    
    @property
    def frequencia(self):
        return self.__frequencia
    
    @frequencia.setter
    def frequencia(self, frequencia):
        self.__frequencia = float(frequencia)
    
    @property
    def memoria(self):
        return self.__memoria
    
    @memoria.setter
    def memoria(self, memoria):
        self.__memoria = float(memoria)
    
    @property
    def ddr(self):
        return self.__ddr
    
    @ddr.setter
    def ddr(self, ddr):
        self.__ddr = int(ddr)

    @property
    def voltagem(self):
        return self.__voltagem
    
    @voltagem.setter
    def voltagem(self, voltagem):
        self.__voltagem = float(voltagem)
    
    def info(self):
        print(f'Preço: R$ {self.__preco}\nMarca: {self.__marca}\nModelo: {self.__marca}\nNucleos:{self.__nucleos}\nFrequência: {self.__frequencia} MHZ\nMemoria: {self.__memoria}\nDDR: {self.__ddr}\nVoltagem: {self.__voltagem}')
