from temas.basicos.ejercicio1 import ejercicio_1
from temas.basicos.ejercicio2 import ejercicio_2
from temas.listas.ejercicio3 import ejercicio_3
from temas.condicionales.ejercicio4 import ejercicio_4
from temas.ciclos.ejercicio5 import ejercicio_5
#   carpeta.carpeta.archivo          función
#Referenciamos la clase
from temas.poo.clases.ejer1poo import Ejercicio1
from temas.poo.clases.ejer2poo import Ejercicio2
from temas.poo.clases.ejer3poo import Ejercicio3
from temas.poo.clases.ejer4poo import Ejercicio4
from temas.poo.clases.ejer5poo import Ejercicio5

#            carpetas archivo          clase

def menuPrincipal():
    while True:
        print(" \n\n :: Menú principal :: ")
        print("1.- Ejercicio 1")
        print("2.- Ejercicio 2")
        print("3.- Ejercicio 3")
        print("4.- Ejercicio 4")
        print("5.- Ejercicio 5")
        print("6.- Salir")
        
        op = int(input("Elija la opción deseada: "))
        print()
        match(op):
            case 1:
                #ejercicio_1()
                #crear el objeto de la clase
                e1 = Ejercicio1()
                #llamar al método a través del objeto
                e1.leerDatos()
                e1.calcularX()
                e1.mostrarResultado()
                print()
            case 2:
                e2 = Ejercicio2()
                e2.leerDatos()
                e2.calcularFn()
                e2.mostrarResultado
                print()
            case 3:
                e3 = Ejercicio3()
                e3.mostrarIndices()
                print()
            case 4:
                e4 = Ejercicio4()
                e4.leerDatos()
                e4.analizarDatos()
                e4.mostrarMensaje()
                print()
            case 5:
                e5 = Ejercicio5()
                e5.leerDatos()
                e5.calcularAprox()
                e5.mostrarResultados()
                ejercicio_5()
            case 6:
                print("Hasta pronto")
                break
            case _:
                print("opción no válida")
            
        