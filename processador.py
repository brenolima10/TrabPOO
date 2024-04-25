class Processador:
    def __init__(self, preco, marca, modelo, socket, frequencia, nucleos, threads, voltagem):
        self.__preco = float(preco)
        self.__marca = marca
        self.__modelo = modelo
        self.__socket = socket
        self.__frequencia = float(frequencia)
        self.__nucleos = int(nucleos)
        self.__threads = int(threads)
        self.__voltagem = float(voltagem) # tem q mudar pra tdp

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
    def socket(self):
        return self.__socket
    
    @socket.setter
    def socket(self, socket):
        self.__socket = socket
    
    @property
    def frequencia(self):
        return self.__frequencia
    
    @frequencia.setter
    def frequencia(self, frequencia):
        self.__frequencia = float(frequencia)
    
    @property
    def nucleos(self):
        return self.__nucleos

    @nucleos.setter
    def nucleos(self, nucleos):
        self.__nucleos = int(nucleos)

    @property
    def threads(self):
        return self.__threads
    
    @threads.setter
    def threads(self, threads):
        self.__threads = int(threads)
    
    @property
    def voltagem(self):
        return self.__voltagem
    
    @voltagem.setter
    def voltagem(self, voltagem):
        self.__voltagem = float(voltagem)

    def info(self):
        print(f'Preço: R$ {self.__preco}\nMarca: {self.__marca}\nModelo: {self.__modelo}\nSocket: {self.__socket}\nFrequência: {self.__frequencia}\nNucleos: {self.__nucleos}\nThreads: {self.__threads}\nVoltagem: {self.__voltagem}')
