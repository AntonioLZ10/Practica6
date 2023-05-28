import math

# Clase abstracta Figura
class Figura:
    def calcularArea(self):
        pass

    def calcularPerimetro(self):
        pass

# Clase Tri�ngulo
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

# Clase C�rculo
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

# Clase Rect�ngulo
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

# Clase Hex�gono
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

# Funci�n principal que contiene el men�
def main():
    opcion = -1

    while opcion != 0:
        print("=== Calculadora de Figuras ===")
        print("1. Calcular �rea y per�metro de un Tri�ngulo")
        print("2. Calcular �rea y per�metro de un C�rculo")
        print("3. Calcular �rea y per�metro de un Rect�ngulo")
        print("4. Calcular �rea y per�metro de un Hex�gono")
        print("0. Salir")
        opcion = int(input("Ingrese la opci�n deseada: "))

        if opcion == 1:
            base = float(input("Ingrese la base del tri�ngulo: "))
            altura = float(input("Ingrese la altura del tri�ngulo: "))

            triangulo = Triangulo()
            triangulo.setBase(base)
            triangulo.setAltura(altura)
            print("�rea del tri�ngulo:", triangulo.calcularArea())
            print("Per�metro del tri�ngulo:", triangulo.calcularPerimetro())
        elif opcion == 2:
            radio = float(input("Ingrese el radio del c�rculo: "))

            circulo = Circulo()
            circulo.setRadio(radio)
            print("�rea del c�rculo:", circulo.calcularArea())
            print("Per�metro del c�rculo:", circulo.calcularPerimetro())
        elif opcion == 3:
            base = float(input("Ingrese la base del rect�ngulo: "))
            altura = float(input("Ingrese la altura del rect�ngulo: "))

            rectangulo = Rectangulo()
            rectangulo.setBase(base)
            rectangulo.setAltura(altura)
            print("�rea del rect�ngulo:", rectangulo.calcularArea())
            print("Per�metro del rect�ngulo:", rectangulo.calcularPerimetro())
        elif opcion == 4:
            lado = float(input("Ingrese el lado del hex�gono: "))

            hexagono = Hexagono()
            hexagono.setLado(lado)
            print("�rea del hex�gono:", hexagono.calcularArea())
            print("Per�metro del hex�gono:", hexagono.calcularPerimetro())
        elif opcion == 0:
            print("�Hasta luego!")
        else:
            print("Opci�n inv�lida. Por favor, intente nuevamente.")

        print()

if __name__ == "__main__":
    main()