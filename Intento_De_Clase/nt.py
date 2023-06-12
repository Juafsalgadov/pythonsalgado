class cliente:
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento

    def setnombre(self,nombre):
        self.__nombre

    def getnombre(self):
        return self.__nombre

    def setdocumento(self,documento):
        self.__documento

    def getdocumento(self):
        return self.__documento