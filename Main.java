/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package prácticaparadigmas;

import java.util.Scanner;


/**
 *
 * @author Comp
 */
// Definición de la interfaz Persona
public interface Persona {
    void setID(int id);
    void setNombre(String nombre);
    void setCURP(String curp);
    void setDomicilio(String domicilio);
    int getID();
    String getNombre();
    String getCURP();
    String getDomicilio();
}

// Clase principal que muestra el menú y realiza la interacción con el usuario

public class Main {
    // Variables estáticas para las instancias de Estudiante, Docente y PAAE
    private static Estudiante estudiante;
    private static Docente docente;
    private static PAAE paae;
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Crear instancias de las clases
        estudiante = new Estudiante();
        docente = new Docente();
        paae = new PAAE();
        
        // Bucle do-while para repetir el menú
        int opcion;
        do {
            // Mostrar el menú
            System.out.println("Bienvenido al sistema de información de personas");
            System.out.println("1. Estudiante");
            System.out.println("2. Docente");
            System.out.println("3. PAAE");
            System.out.println("0. Salir");
            System.out.print("Seleccione una opción: ");
            
            opcion = scanner.nextInt();
            
            if (opcion != 0) {
                // Capturar los datos de la persona seleccionada
                System.out.print("Ingrese el ID: ");
                int id = scanner.nextInt();
                System.out.print("Ingrese el nombre: ");
                String nombre = scanner.next();
                System.out.print("Ingrese el CURP: ");
                String curp = scanner.next();
                System.out.print("Ingrese el domicilio: ");
                String domicilio = scanner.next();
                
                // Establecer los datos en la instancia adecuada
                if (opcion == 1) {
                    estudiante.setID(id);
                    estudiante.setNombre(nombre);
                    estudiante.setCURP(curp);
                    estudiante.setDomicilio(domicilio);
                } else if (opcion == 2) {
                    docente.setID(id);
                    docente.setNombre(nombre);
                    docente.setCURP(curp);
                    docente.setDomicilio(domicilio);
                } else if (opcion == 3) {
                    paae.setID(id);
                    paae.setNombre(nombre);
                    paae.setCURP(curp);
                    paae.setDomicilio(domicilio);
                }
                
                // Mostrar los datos de la persona seleccionada
                System.out.println("Datos de la persona:");
                System.out.println("ID: " + obtenerID(opcion));
                System.out.println("Nombre: " + obtenerNombre(opcion));
                System.out.println("CURP: " + obtenerCURP(opcion));
                System.out.println("Domicilio: " + obtenerDomicilio(opcion));
                System.out.println();
            }
        } while (opcion != 0);

        System.out.println("¡Hasta luego!");
    }
    
    // Métodos auxiliares para obtener los datos de la persona seleccionada
    public static int obtenerID(int opcion) {
        if (opcion == 1) {
            return estudiante.getID();
        } else if (opcion == 2) {
            return docente.getID();
        } else if (opcion == 3) {
            return paae.getID();
        }
        return 0;
    }
    
    public static String obtenerNombre(int opcion) {
        if (opcion == 1) {
            return estudiante.getNombre();
        } else if (opcion == 2) {
            return docente.getNombre();
        } else if (opcion == 3) {
            return paae.getNombre();
        }
        return "";
    }
    
    public static String obtenerCURP(int opcion) {
        if (opcion == 1) {
            return estudiante.getCURP();
        } else if (opcion == 2) {
            return docente.getCURP();
        } else if (opcion == 3) {
            return paae.getCURP();
        }
        return "";
    }
    
    public static String obtenerDomicilio(int opcion) {
        if (opcion == 1) {
            return estudiante.getDomicilio();
        } else if (opcion == 2) {
            return docente.getDomicilio();
        } else if (opcion == 3) {
            return paae.getDomicilio();
        }
        return "";
    }
}

