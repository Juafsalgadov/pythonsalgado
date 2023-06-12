class Empleado:
    suma = 0
    contador = 0

    def _init_(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        Empleado.suma += salario
        Empleado.contador += 1

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cargo(self):
        return self.cargo

    def set_cargo(self, cargo):
        self.cargo = cargo

    def get_salario(self):
        return self.salario

    def set_salario(self, salario):
        self.salario = salario

    def Salarioxhora(self):
        return self.salario / 8

    def Sumaipc(self):
        incremento = 0
        if self.salario == "mínimo":
            incremento = self.salario * 0.03
        else:
            incremento = self.salario * 0.03
        return incremento

    def horasextra(self, horas_extras):
        if horas_extras > 2:
            horas_extras = 2
        salario_hora = self.Salarioxhora()
        salario_normal = salario_hora * 8
        salario_extra = salario_hora * horas_extras * 2
        return salario_normal + salario_extra

    def sumasalarios(cls):
        return cls.suma
    
    def promediosalarios(cls):
        return cls.suma / cls.contador