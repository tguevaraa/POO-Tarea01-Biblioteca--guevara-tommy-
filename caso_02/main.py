# main.py
from modelo.pila import Pila
from modelo.cola import Cola

print("=" * 50)
print("   TAD PILA — Comportamiento LIFO")
print("=" * 50)

pila = Pila()
pila.push("A")
pila.push("B")
pila.push("C")

print(f"Pila inicial:     {pila}")
print(f"Tope (top):       {pila.top()}")
print(f"Extrae (pop):     {pila.pop()}")
print(f"Pila luego pop:   {pila}")
print(f"Tamaño (size):    {pila.size()}")
print(f"¿Vacía?:          {pila.isEmpty()}")

pila2 = Pila()
pila2.push("X")
pila2.push("Y")
pila.pushAll(pila2)
print(f"Luego pushAll:    {pila}")

invertida = pila.reverse()
print(f"Pila invertida:   {invertida}")

'''
Desafio adicional: Agregar un método contain_boolean(number) a 
la clase Pila que devuelva True si el número está presente en la pila, 
o False en caso contrario. Luego, probar este método con algunos números.
'''

pila = Pila()
pila.push(10)
pila.push(20)
pila.push(30)

print(pila.contain_boolean(20))   # True
print(pila.contain_boolean(99))   # False
print(pila)                # Pila([10, 20, 30])  ← sin cambios

print()
print("=" * 50)
print("   TAD COLA — Comportamiento FIFO")
print("=" * 50)

cola = Cola()
cola.push("A")
cola.push("B")
cola.push("C")

print(f"Cola inicial:     {cola}")
print(f"Frente (top):     {cola.top()}")
print(f"Extrae (pop):     {cola.pop()}")
print(f"Cola luego pop:   {cola}")
print(f"Tamaño (size):    {cola.size()}")
print(f"¿Vacía?:          {cola.isEmpty()}")

cola2 = Cola()
cola2.push("X")
cola2.push("Y")
cola.pushAll(cola2)
print(f"Luego pushAll:    {cola}")

invertida_cola = cola.reverse()
print(f"Cola invertida:   {invertida_cola}")

print(cola.contain_boolean("X"))   # True
print(cola.contain_boolean("Z"))   # False
print(cola)

print()
print("=" * 50)
print("   PRUEBA DE COPIAR")
print("=" * 50)

pila = Pila()
pila.push("A")
pila.push("B")
pila.push("C")

copia = pila.copiar()

print(copia.pop())   # C   ← misma cima que el original
print(copia.pop())   # B
print(pila)          # Pila(['A', 'B', 'C'])  ← original intacto

cola = Cola()
cola.push("A")
cola.push("B")
cola.push("C")

copia = cola.copiar()

print(copia.pop())   # A   ← mismo frente que el original
print(copia.pop())   # B
print(cola)          # Cola(['A', 'B', 'C'])  ← original intacto