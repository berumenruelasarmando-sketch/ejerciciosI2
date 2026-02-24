import math
class Ejercicio2():
  def __init__(self):
          self.n = 0
          self.aprox = 0

  def leerDatos(self):
    self.n = int(input("n: "))
    
  def calcularFn(sefl):
    sefl.aprox = math.sqrt(2*math.pi)*math.exp(-sefl.n)*sefl.n**(sefl.n+1/2)

  def mostrarResultado(self):
    print("Aproximación de n!= ",self.aprox)


