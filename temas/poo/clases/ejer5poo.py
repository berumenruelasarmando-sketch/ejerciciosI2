import math

class Ejercicio5():
    def __init__(self):
        self.x = 0
        self.tol = 0
        self.aprox = 0
        self.valorReal = 0
        self.error = 0
        self.k = 0

    def leerDatos(self):
        self.x = float(input("x: "))
        self.tol = float(input("Tolerancia: "))

    def calcularAprox(self):
        self.k = 0
        self.aprox = 0
        self.valorReal = math.atan(self.x)
        self.error = self.tol + 1

        while self.error > self.tol:
            self.aprox += (-1)**self.k * (self.x**(2*self.k+1)) / (2*self.k+1)
            
            if self.valorReal != 0:
                self.error = abs((self.valorReal - self.aprox) / self.valorReal) * 100
            else:
                self.error = abs(self.valorReal - self.aprox)

            self.k += 1

    def mostrarResultados(self):
        print("Aprox = ", self.aprox)
        print("Valor real = ", self.valorReal)
        print("Error = ", self.error)
        print("Iteraciones (k) = ", self.k)