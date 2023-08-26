#Herencia

# Crea una clase que se llame Animal, que contenga como atributo el nombre del animal y un método llamado comer

class Animal:
  def __init__(self, nombre, color):
    self.nombre = nombre
    self.__color  =  color                 #Encapsulamiento

  def __comer(self):
    print(f"{self.nombre} está comiendo")


class Gatito(Animal):
  def maullar(self):
    print("miaw")


mi_gato = Gatito("Chicken","Gris")
#print(mi_gato.color)

mi_gato.comer()
#mi_gato.maullar()
