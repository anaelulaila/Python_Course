dicc = {}

diccionario = {"azul":"blue","rojo":"red","verde":"green"}


usuarios = {"Anael":123456789,"Fer":12823094,"Ema":23832438}

print(usuarios)
usuarios["Ryan"] = 1111111111     #Añadir elementos en los diccionarios
print(usuarios)


print(usuarios["Anael"])

usuarios["Anael"] = 45654575363

print(usuarios["Anael"])

print(usuarios)


#Verifica si existe la clave Ema "en" el diccionario
booleano = "Ema" in usuarios

print(booleano)

print(usuarios.keys())            #Muestra solo las llaves
print(usuarios.values())          #Muestra solo los valores de cada llave

#Clean
usuarios.clear()                  #Vacia el diccionario

print(usuarios)
