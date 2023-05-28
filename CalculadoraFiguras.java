/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package prácticaparadigmas;

import java.util.Scanner;

// Clase abstracta Figura
abstract class Figura {
    abstract double calcularArea();
    abstract double calcularPerimetro();
}

// Clase Triángulo
class Triangulo extends Figura {
    private double base;
    private double altura;

    public void setBase(double base) {
        this.base = base;
    }

    public void setAltura(double altura) {
        this.altura = altura;
    }

    public double getBase() {
        return base;
    }

    public double getAltura() {
        return altura;
    }

    @Override
    public double calcularArea() {
        return (base * altura) / 2;
    }

    @Override
    public double calcularPerimetro() {
        return base * 3;
    }
}

// Clase Círculo
class Circulo extends Figura {
    private double radio;

    public void setRadio(double radio) {
        this.radio = radio;
    }

    public double getRadio() {
        return radio;
    }

    @Override
    public double calcularArea() {
        return Math.PI * radio * radio;
    }

    @Override
    public double calcularPerimetro() {
        return 2 * Math.PI * radio;
    }
}

// Clase Rectángulo
class Rectangulo extends Figura {
    private double base;
    private double altura;

    public void setBase(double base) {
        this.base = base;
    }

    public void setAltura(double altura) {
        this.altura = altura;
    }

    public double getBase() {
        return base;
    }

    public double getAltura() {
        return altura;
    }

    @Override
    public double calcularArea() {
        return base * altura;
    }

    @Override
    public double calcularPerimetro() {
        return 2 * (base + altura);
    }
}

// Clase Hexágono
class Hexagono extends Figura {
    private double lado;

    public void setLado(double lado) {
        this.lado = lado;
    }

    public double getLado() {
        return lado;
    }

    @Override
    public double calcularArea() {
        return (3 * Math.sqrt(3) * lado * lado) / 2;
    }

    @Override
    public double calcularPerimetro() {
        return 6 * lado;
    }
}

// Clase principal que contiene el menú
public class CalculadoraFiguras {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("=== Calculadora de Figuras ===");
            System.out.println("1. Calcular área y perímetro de un Triángulo");
            System.out.println("2. Calcular área y perímetro de un Círculo");
            System.out.println("3. Calcular área y perímetro de un Rectángulo");
            System.out.println("4. Calcular área y perímetro de un Hexágono");
            System.out.println("0. Salir");
            System.out.print("Ingrese la opción deseada: ");
            opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    double base, altura;
                    System.out.print("Ingrese la base del triángulo: ");
                    base = scanner.nextDouble();
                    System.out.print("Ingrese la altura del triángulo: ");
                    altura = scanner.nextDouble();

                    Triangulo triangulo = new Triangulo();
                    triangulo.setBase(base);
                    triangulo.setAltura(altura);
                    System.out.println("Área del triángulo: " + triangulo.calcularArea());
                    System.out.println("Perímetro del triángulo: " + triangulo.calcularPerimetro());
                    break;
                case 2:
                    double radio;
                    System.out.print("Ingrese el radio del círculo: ");
                    radio = scanner.nextDouble();

                    Circulo circulo = new Circulo();
                    circulo.setRadio(radio);
                    System.out.println("Área del círculo: " + circulo.calcularArea());
                    System.out.println("Perímetro del círculo: " + circulo.calcularPerimetro());
                    break;
                case 3:
                    double baseRect, alturaRect;
                    System.out.print("Ingrese la base del rectángulo: ");
                    baseRect = scanner.nextDouble();
                    System.out.print("Ingrese la altura del rectángulo: ");
                    alturaRect = scanner.nextDouble();

                    Rectangulo rectangulo = new Rectangulo();
                    rectangulo.setBase(baseRect);
                    rectangulo.setAltura(alturaRect);
                    System.out.println("Área del rectángulo: " + rectangulo.calcularArea());
                    System.out.println("Perímetro del rectángulo: " + rectangulo.calcularPerimetro());
                    break;
                case 4:
                    double ladoHex;
                    System.out.print("Ingrese el lado del hexágono: ");
                    ladoHex = scanner.nextDouble();

                    Hexagono hexagono = new Hexagono();
                    hexagono.setLado(ladoHex);
                    System.out.println("Área del hexágono: " + hexagono.calcularArea());
                    System.out.println("Perímetro del hexágono: " + hexagono.calcularPerimetro());
                    break;
                case 0:
                    System.out.println("¡Hasta luego!");
                    break;
                default:
                    System.out.println("Opción inválida. Por favor, intente nuevamente.");
                    break;
            }

            System.out.println();
        } while (opcion != 0);

        scanner.close();
    }
}

