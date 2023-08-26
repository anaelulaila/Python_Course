# POO (OOP) en python

class Perro:   #Las clases en python siempre inician con Mayuscula
  def __init__(self,nombre,raza,edad,owner):      # Atributos
    self.nombre = nombre
    self.raza = raza
    self.edad = edad
    self.owner = owner

  def ladrar(self):                         #Metodos
    print("Barf Barf")


  def comer(self):
    print(f"{self.nombre} está comiendo")

  def dormir(self):
    print(f"{self.nombre} está durmiendo")



mi_perro = Perro("piloncillo", "cocker", 1, "ana")    #Objeto
otro_perro = Perro("Barbacoa", "golden", 2, "ana")

def atributos(perros):
  print(perros.raza)
  print(perros.nombre)
  print(perros.owner)
  print("\n")

#Imprimir atributos
atributos(mi_perro)

#Llamar metodos
mi_perro.ladrar()
mi_perro.comer()
mi_perro.dormir()

#Imprimir atributos del otro objeto
print("\n")
atributos(otro_perro)

#Llamar metodos del otro perro
otro_perro.ladrar()
otro_perro.comer()
otro_perro.dormir()
