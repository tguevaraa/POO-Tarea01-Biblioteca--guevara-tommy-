# modelo/persona.py

class Persona:
    contador_turnos = 0

    def __init__(self, nombre):
        self._nombre = nombre
        Persona.contador_turnos += 1
        self._turno = Persona.contador_turnos

    @property
    def nombre(self):
        return self._nombre
        
    @property
    def turno(self):
        return self._turno

    def __str__(self):
        return self._nombre
