class compañia:

    def __init__(self, codigocarros, repuestos):
        self.codigocarros=codigocarros
        self.repuestos=repuestos

    def setcodigocarros(self,codigocarros):
        self.__codigocarros=codigocarros

    def getcodigocarros(self):
        return self.__codigocarros

    def setrepuestos(self,repuestos):
        self.__repuestos=repuestos


    def getrepuestos(self):
        return self.__repuestos 