class Fonte:
    def __init__(self, preco, marca, modelo, voltagem, selo80plus):
        self.__preco = float(preco)
        self.__marca = marca
        self.__modelo = modelo
        self.__voltagem = float(voltagem)
        self.__selo80plus = bool(selo80plus)

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
    def voltagem(self):
        return self.__voltagem
    
    @voltagem.setter
    def voltagem(self, voltagem):
        self.__voltagem = float(voltagem)
    
    @property
    def selo80plus(self):
        return self.__selo80plus
    
    @selo80plus.setter
    def selo80plus(self, selo80plus):
        self.__selo80plus = bool(selo80plus)
    
    def info(self):
        print(f'Preço: R$ {self.__preco}\nMarca: {self.__marca}\nModelo: {self.__modelo}\nVoltagem: {self.__voltagem}\nSelo 80 plus: {self.__selo80plus}')
