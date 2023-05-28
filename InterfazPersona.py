class Persona:
    def setID(self, id):
        pass

    def setNombre(self, nombre):
        pass

    def setCURP(self, curp):
        pass

    def setDomicilio(self, domicilio):
        pass

    def getID(self):
        pass

    def getNombre(self):
        pass

    def getCURP(self):
        pass

    def getDomicilio(self):
        pass


class Estudiante(Persona):
    def _init_(self):
        self.ID = 0
        self.nombre = ""
        self.CURP = ""
        self.domicilio = ""

    def setID(self, id):
        self.ID = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setCURP(self, curp):
        self.CURP = curp

    def setDomicilio(self, domicilio):
        self.domicilio = domicilio

    def getID(self):
        return self.ID

    def getNombre(self):
        return self.nombre

    def getCURP(self):
        return self.CURP

    def getDomicilio(self):
        return self.domicilio


class Docente(Persona):
    def _init_(self):
        self.ID = 0
        self.nombre = ""
        self.CURP = ""
        self.domicilio = ""

    def setID(self, id):
        self.ID = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setCURP(self, curp):
        self.CURP = curp

    def setDomicilio(self, domicilio):
        self.domicilio = domicilio

    def getID(self):
        return self.ID

    def getNombre(self):
        return self.nombre

    def getCURP(self):
        return self.CURP

    def getDomicilio(self):
        return self.domicilio


class PAAE(Persona):
    def _init_(self):
        self.ID = 0
        self.nombre = ""
        self.CURP = ""
        self.domicilio = ""

    def setID(self, id):
        self.ID = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setCURP(self, curp):
        self.CURP = curp

    def setDomicilio(self, domicilio):
        self.domicilio = domicilio

    def getID(self):
        return self.ID

    def getNombre(self):
        return self.nombre

    def getCURP(self):
        return self.CURP

    def getDomicilio(self):
        return self.domicilio


def main():
    estudiante = Estudiante()
    docente = Docente()
    paae = PAAE()

    opcion = None
    while opcion != 0:
        print("Bienvenido al sistema de información de personas")
        print("1. Estudiante")
        print("2. Docente")
        print("3. PAAE")
        print("0. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion != 0:
            id = int(input("Ingrese el ID: "))
            nombre = input("Ingrese el nombre: ")
            curp = input("Ingrese el CURP: ")
            domicilio = input("Ingrese el domicilio: ")

            if opcion == 1:
                estudiante.setID(id)
                estudiante.setNombre(nombre)
                estudiante.setCURP(curp)
                estudiante.setDomicilio(domicilio)
            elif opcion == 2:
                docente.setID(id)
                docente.setNombre(nombre)
                docente.setCURP(curp)
                docente.setDomicilio(domicilio)
            elif opcion == 3:
                paae.setID(id)
                paae.setNombre(nombre)
                paae.setCURP(curp)
                paae.setDomicilio(domicilio)

            print("Datos de la persona:")
            print("ID:", obtenerID(opcion, estudiante, docente, paae))
            print("Nombre:", obtenerNombre(opcion, estudiante, docente, paae))
            print("CURP:", obtenerCURP(opcion, estudiante, docente, paae))
            print("Domicilio:", obtenerDomicilio(opcion, estudiante, docente, paae))
            print()


def obtenerID(opcion, estudiante, docente, paae):
    if opcion == 1:
        return estudiante.getID()
    elif opcion == 2:
        return docente.getID()
    elif opcion == 3:
        return paae.getID()
    return 0


def obtenerNombre(opcion, estudiante, docente, paae):
    if opcion == 1:
        return estudiante.getNombre()
    elif opcion == 2:
        return docente.getNombre()
    elif opcion == 3:
        return paae.getNombre()
    return ""


def obtenerCURP(opcion, estudiante, docente, paae):
    if opcion == 1:
        return estudiante.getCURP()
    elif opcion == 2:
        return docente.getCURP()
    elif opcion == 3:
        return paae.getCURP()
    return ""


def obtenerDomicilio(opcion, estudiante, docente, paae):
    if opcion == 1:
        return estudiante.getDomicilio()
    elif opcion == 2:
        return docente.getDomicilio()
    elif opcion == 3:
        return paae.getDomicilio()
    return ""


if __name__ == "__main__":
    main()