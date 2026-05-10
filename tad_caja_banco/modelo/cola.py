# modelo/cola.py

class Cola:

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
