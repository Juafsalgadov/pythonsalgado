from nt import *
from mantenimiento import *
from modelo import *

a1=cliente('Isaac Hilberto',123456)

a2=carro('Mc Queen','rojo','1234')

a3=compañia('1111','llantas')

for cliente in a1.getnombre():
    print(cliente)

for compañia in a2.getrepuestos():
    print(compañia)

for carro in a3.gettipocarro():
    print(carro)