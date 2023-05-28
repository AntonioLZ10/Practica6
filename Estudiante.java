/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package prácticaparadigmas;

/**
 *
 * @author Comp
 */
public class Estudiante implements Persona {
    private int ID;
    private String nombre;
    private String CURP;
    private String domicilio;
    
    @Override
    public void setID(int id) {
        this.ID = id;
    }
    
    @Override
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    @Override
    public void setCURP(String curp) {
        this.CURP = curp;
    }
    
    @Override
    public void setDomicilio(String domicilio) {
        this.domicilio = domicilio;
    }
    
    @Override
    public int getID() {
        return ID;
    }
    
    @Override
    public String getNombre() {
        return nombre;
    }
    
    @Override
    public String getCURP() {
        return CURP;
    }
    
    @Override
    public String getDomicilio() {
        return domicilio;
    }
}
