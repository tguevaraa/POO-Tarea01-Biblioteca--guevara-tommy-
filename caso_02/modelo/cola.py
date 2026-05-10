# modelo/cola.py

class Cola:
    """Implementación del TAD Cola (FIFO)."""

    def __init__(self):
        self._elementos = []

    def push(self, elemento):
        self._elementos.append(elemento)

    def pop(self):
        if self.isEmpty():
            return None
        return self._elementos.pop(0)

    def isEmpty(self):
        return len(self._elementos) == 0

    def top(self):
        if self.isEmpty():
            return None
        return self._elementos[0]

    def size(self):
        return len(self._elementos)

    def reverse(self):
        nueva = Cola()
        for elemento in reversed(self._elementos):
            nueva.push(elemento)
        return nueva
        
    def copiar(self):
        nueva = Cola()
        nueva._elementos = self._elementos[:]
        return nueva
    
    def contain_boolean(self, string):
        if string in self._elementos:
            return True
        else:
            return False

    def pushAll(self, otraCola):
        for elemento in otraCola._elementos:
            self.push(elemento)

    def __str__(self):
        return f"Cola({self._elementos})"