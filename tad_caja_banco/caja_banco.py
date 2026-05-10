# caja_banco.py

from modelo.cola import Cola


class CajaBanco:

    def __init__(self):
        self._cola = Cola()

    def agregar_persona(self, persona):
        self._cola.push(persona)

    def atender(self):
        return self._cola.pop()

    def esta_vacia(self):
        return self._cola.isEmpty()

    def persona_abandona(self, nombre: str) -> bool:
        encontrado = False
        cola_temporal = Cola()

        while not self._cola.isEmpty():
            persona = self._cola.pop()
            if not encontrado and persona.nombre == nombre:
                encontrado = True
            else:
                cola_temporal.push(persona)

        while not cola_temporal.isEmpty():
            self._cola.push(cola_temporal.pop())

        return encontrado
