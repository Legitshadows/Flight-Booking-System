# Un codigo que me avente el fin de semana, ocupa ser refinado y mas definido para que sea mas complejo

class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, capacidad):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.capacidad = capacidad
        self.asientos_disponibles = capacidad

class Pasajero:
    def __init__(self, nombre, apellido, pasaporte):
        self.nombre = nombre
        self.apellido = apellido
        self.pasaporte = pasaporte

def hacer_reserva(vuelo, pasajero):
    if vuelo.asientos_disponibles > 0:
        vuelo.asientos_disponibles -= 1
        return True
    else:
        return False

# Aqui se crea el "vuelo" que haremos del usuario
numero_vuelo = input("Ingrese el número de vuelo: ")
origen = input("Ingrese la ciudad de origen: ")
destino = input("Ingrese la ciudad de destino: ")
capacidad = int(input("Ingrese la capacidad de asientos: "))

# Aqui ya se confirma el vuelo que podemos usar para imprimir en un print
vuelo1 = Vuelo(numero_vuelo, origen, destino, capacidad)

# Aqui solicitamos los datos del usuario
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
pasaporte = input("Ingrese su número de pasaporte: ")

# Aqui se crea el pasajero para el print
pasajero1 = Pasajero(nombre, apellido, pasaporte)

# Y finalmente hacemos la reserva del vuelo
if hacer_reserva(vuelo1, pasajero1):
    print("Reserva exitosa para {} {} en el vuelo {}.".format(pasajero1.nombre, pasajero1.apellido, vuelo1.numero_vuelo))
else:
    print("Lo siento, no hay asientos disponibles en el vuelo {}.".format(vuelo1.numero_vuelo))
