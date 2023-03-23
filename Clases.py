from dataclasses import dataclass


@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre


class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento):
        return any(elem.nombre == elemento.nombre for elem in self.elementos)

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        for elemento in otro_conjunto.elementos:
            self.agregar_elemento(elemento)

    def __add__(self, otro_conjunto):
        resultado = Conjunto(f"{self.nombre} + {otro_conjunto.nombre}")
        resultado.unir(self)
        resultado.unir(otro_conjunto)
        return resultado

    def intersectar(cls, conjunto1, conjunto2):
        resultado = Conjunto(f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}")
        for elemento in conjunto1.elementos:
            if conjunto2.contiene(elemento):
                resultado.agregar_elemento(elemento)
        return resultado

    def __str__(self):
        elementos_str = ", ".join(elem.nombre for elem in self.elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"
