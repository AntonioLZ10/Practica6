import math

# Clase abstracta Figura
class Figura:
    def calcularArea(self):
        pass

    def calcularPerimetro(self):
        pass

# Clase Triángulo
class Triangulo(Figura):
    def _init_(self):
        self.base = 0
        self.altura = 0

    def setBase(self, base):
        self.base = base

    def setAltura(self, altura):
        self.altura = altura

    def getBase(self):
        return self.base

    def getAltura(self):
        return self.altura

    def calcularArea(self):
        return (self.base * self.altura) / 2

    def calcularPerimetro(self):
        return self.base * 3

# Clase Círculo
class Circulo(Figura):
    def _init_(self):
        self.radio = 0

    def setRadio(self, radio):
        self.radio = radio

    def getRadio(self):
        return self.radio

    def calcularArea(self):
        return math.pi * self.radio * self.radio

    def calcularPerimetro(self):
        return 2 * math.pi * self.radio

# Clase Rectángulo
class Rectangulo(Figura):
    def _init_(self):
        self.base = 0
        self.altura = 0

    def setBase(self, base):
        self.base = base

    def setAltura(self, altura):
        self.altura = altura

    def getBase(self):
        return self.base

    def getAltura(self):
        return self.altura

    def calcularArea(self):
        return self.base * self.altura

    def calcularPerimetro(self):
        return 2 * (self.base + self.altura)

# Clase Hexágono
class Hexagono(Figura):
    def _init_(self):
        self.lado = 0

    def setLado(self, lado):
        self.lado = lado

    def getLado(self):
        return self.lado

    def calcularArea(self):
        return (3 * math.sqrt(3) * self.lado * self.lado) / 2

    def calcularPerimetro(self):
        return 6 * self.lado

# Función principal que contiene el menú
def main():
    opcion = -1

    while opcion != 0:
        print("=== Calculadora de Figuras ===")
        print("1. Calcular área y perímetro de un Triángulo")
        print("2. Calcular área y perímetro de un Círculo")
        print("3. Calcular área y perímetro de un Rectángulo")
        print("4. Calcular área y perímetro de un Hexágono")
        print("0. Salir")
        opcion = int(input("Ingrese la opción deseada: "))

        if opcion == 1:
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))

            triangulo = Triangulo()
            triangulo.setBase(base)
            triangulo.setAltura(altura)
            print("Área del triángulo:", triangulo.calcularArea())
            print("Perímetro del triángulo:", triangulo.calcularPerimetro())
        elif opcion == 2:
            radio = float(input("Ingrese el radio del círculo: "))

            circulo = Circulo()
            circulo.setRadio(radio)
            print("Área del círculo:", circulo.calcularArea())
            print("Perímetro del círculo:", circulo.calcularPerimetro())
        elif opcion == 3:
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))

            rectangulo = Rectangulo()
            rectangulo.setBase(base)
            rectangulo.setAltura(altura)
            print("Área del rectángulo:", rectangulo.calcularArea())
            print("Perímetro del rectángulo:", rectangulo.calcularPerimetro())
        elif opcion == 4:
            lado = float(input("Ingrese el lado del hexágono: "))

            hexagono = Hexagono()
            hexagono.setLado(lado)
            print("Área del hexágono:", hexagono.calcularArea())
            print("Perímetro del hexágono:", hexagono.calcularPerimetro())
        elif opcion == 0:
            print("¡Hasta luego!")
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

        print()

if __name__ == "__main__":
    main()