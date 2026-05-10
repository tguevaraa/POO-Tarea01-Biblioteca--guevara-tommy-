# modelo/pila.py

class Pila:
    """Implementación del TAD Pila (LIFO)."""

    def __init__(self):
        self._elementos = []

    def push(self, elemento):
        self._elementos.append(elemento)

    def pop(self):
        if self.isEmpty():
            return None
        return self._elementos.pop()

    def isEmpty(self):
        return len(self._elementos) == 0

    def top(self):
        if self.isEmpty():
            return None
        return self._elementos[-1]

    def size(self):
        return len(self._elementos)

    def reverse(self):
        nueva = Pila()
        nueva._elementos = self._elementos[::-1]
        return nueva

    def copiar(self):
        nueva = Pila()
        nueva._elementos = self._elementos[:]
        return nueva
    
    def contain_boolean(self, number):
        if number in self._elementos:
            return True
        else:
            return False

    def pushAll(self, otraPila):
        for elemento in otraPila._elementos:
            self.push(elemento)

    def __str__(self):
        return f"Pila({self._elementos})"