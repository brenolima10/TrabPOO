class Armazenamento:
    def __init__(self, espaco, voltagem):
        self.__espaco = float(espaco)
        self.__voltagem = float(voltagem)
    
    @property
    def espaco(self):
        return self.__espaco
    
    @espaco.setter
    def espaco(self, espaco):
        self.__espaco = float(espaco)
    
    @property
    def voltagem(self):
        return self.__voltagem
    
    @voltagem.setter
    def voltagem(self, voltagem):
        self.__voltagem = float(voltagem)
    
    def info(self):
        print(f'Espaço: {self.__espaco} GB\nVoltagem: {self.__voltagem}')
