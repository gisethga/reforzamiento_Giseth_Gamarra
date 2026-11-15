"""
Ejercicio 05. Sistema de figuras geométricas
Desarrollar un programa que permita calcular las áreas y perímetros de diferentes figuras geométricas
utilizando herencia.
Requisitos:
• Crear una clase Figura con un atributo nombre, inicializado mediante un constructor, y un
método para mostrarlo.
• Crear una clase Rectangulo que herede de Figura, con los atributos base y altura, y métodos
para calcular su área y perímetro.
• Crear una clase Circulo que también herede de Figura, con el atributo radio y métodos para
calcular su área y perímetro.
• Validar que las dimensiones ingresadas sean valores numéricos mayores que cero.
• Crear al menos dos objetos de Rectangulo y dos de Circulo, utilizando dimensiones diferentes
• Mostrar el nombre, las dimensiones, el área y el perímetro de cada figura
Utilizar π = 3.1416 y mostrar los resultados con dos decimales
"""

class figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print(f"La figura es un: {self.nombre}")

class rectangulo(figura):
    nombre = "rectángulo"
    def __init__(self, base, altura):

        if base < 0 or altura < 0:
                raise ValueError(f"La base es {base} y la altura {altura}, ambos deben ser mayores a cero. No se admiten negativos.")

        super().__init__(self.nombre)
        self.base = base
        self.altura = altura

    def area(self):
        print(f"La base es {self.base} y la altura es {self.altura}")
        arear = self.base * self.altura
        print("El área del {} es {:.2f}".format(self.nombre, arear))

    def perimetro(self):
        perimetror = 2 * (self.base + self.altura)
        print("El perimetro del {} es {:.2f}".format(self.nombre, perimetror))

class circulo(figura):
    nombre = "círculo"
    pi = 3.1416
    def __init__(self, radio):

        if radio < 0:
            raise ValueError(f"El radio es {radio}, debe ser mayor a cero. No se admiten negativos.")

        super().__init__(self.nombre)
        self.radio = radio

    def area(self):
        print(f"La valor de pi es {self.pi} y el radio es {self.radio}")
        areac = self.pi * self.radio ** 2
        print("El área de {} es {:.2f}". format(self.nombre, areac))

    def perimetro(self):
        perimetroc = 2 * self.pi * self.radio
        print("El perimetro del {} es {:.2f}".format(self.nombre, perimetroc))



print("\n---Rectangulo 1---")
try:
    rect_1 = rectangulo(-10, 5)
    rect_1.mostrar()
    rect_1.area()
    rect_1.perimetro()
except ValueError as e:
    print("Error:", e)

print("\n---Rectangulo 2---")
try:
    rect_2 = rectangulo(10, 5)
    rect_2.mostrar()
    rect_2.area()
    rect_2.perimetro()
except ValueError as e:
    print("Error:", e)

print("\n---Circulo 1---")
try:
    circ_1 = circulo(5)
    circ_1.mostrar()
    circ_1.area()
    circ_1.perimetro()
except ValueError as e:
    print("Error:", e)

print("\n---Circulo 2---")
try:
    circ_2 = circulo(-9)
    circ_2.mostrar()
    circ_2.area()
    circ_2.perimetro()
except ValueError as e:
    print("Error:", e)