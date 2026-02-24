class Ejercicio4():
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.mensaje = ""

    def leerDatos(self):
        self.a = int(input("a: "))
        self.b = int(input("b: "))
        self.c = int(input("c: "))

    def analizarDatos(self):
        self.d = self.b**2 - 4 * self.a * self.c
        
        if self.d > 0:
            self.mensaje = "la gráfica es una hipérbola"
        
        elif self.d == 0:
            if self.a == 0 and self.c == 0:
                self.mensaje = "la gráfica es una recta"
            else:
                self.mensaje = "la gráfica es una parábola"
        
        else:  
            if self.a == self.c:
                self.mensaje = "la gráfica es una circunferencia"
            else:
                self.mensaje = "la gráfica es una elipse"

    def mostrarMensaje(self):
        print(self.mensaje)