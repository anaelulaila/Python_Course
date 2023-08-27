#SIMPLE ORDER TRACKING SYSTEM 

#DICTIONARY 
pedidos = {"A123":"En proceso", "B456":"Entregado", "C789":"Pendiente", "D012":"En camino"}  #Ordering dictionary

#FUNCTIONS
def Verificar_Estado(numero_seguimiento):
    if numero_seguimiento in pedidos:
        print("El estado del pedido es: ", pedidos[numero_seguimiento])
    else:
        print("Número de seguimiento no encontrado.")

def Crear_Pedido(numero_seguimiento, estado):
    pedidos[numero_seguimiento] = estado
    print("Se ha creado un pedido con el número de seguimiento y estado proporcionados.")
    print("Num. de seguimiento: ", numero_seguimiento)
    print("Estado actual del pedido: ", estado)
         
#TESTING
num_seguimiento = input("Ingrese la clave del pedido: ")
estado_pedido = input("Ingrese el estado del pedido: ")
Verificar_Estado(num_seguimiento)
Crear_Pedido(num_seguimiento, estado_pedido)

#DISPLAY ALL TRACKING NUMBERS
for i in pedidos:
    print (i)
