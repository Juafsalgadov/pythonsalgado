class carro:
    def __init__(self, tipocarro, color, matricula):
        self.__tipocarro=tipocarro
        self.__color=color
        self.__matricula=matricula

    def settipocarro(self,tipocarro):
        self.__tipocarro=tipocarro

    def gettipocarro(self):
        return self.__tipocarro

    def setcolor(self,color):
        self.__color=color

    def getcolor(self):
        return self.__color

    def setmatricula(self,matricula):
        self.__matricula=matricula

    def getmatricula(self):
        return self.__matricula