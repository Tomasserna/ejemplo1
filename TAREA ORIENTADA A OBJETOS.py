class Celular:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} se ha encendido.")
        else:
            print(f"{self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"{self.marca} {self.modelo} se ha apagado.")
        else:
            print(f"{self.marca} {self.modelo} ya está apagado.")

    def llamar(self, numero):
        if self.encendido:
            print(f"Llamando al número {numero}...")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para llamar.")


mi_celular = Celular("iphone", "14pro", 999.99)

mi_celular.encender()

mi_celular.llamar("310-795-7439")

mi_celular.apagar()

class Celular:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} se ha encendido.")
        else:
            print(f"{self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"{self.marca} {self.modelo} se ha apagado.")
        else:
            print(f"{self.marca} {self.modelo} ya está apagado.")

    def llamar(self, numero):
        if self.encendido:
            print(f"Llamando al número {numero}...")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para llamar.")


mi_celular = Celular("iphone", "13pro", 999.99)

mi_celular.encender()

mi_celular.llamar("311-495-2239")

mi_celular.apagar()

class Celular:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} se ha encendido.")
        else:
            print(f"{self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"{self.marca} {self.modelo} se ha apagado.")
        else:
            print(f"{self.marca} {self.modelo} ya está apagado.")

    def llamar(self, numero):
        if self.encendido:
            print(f"Llamando al número {numero}...")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para llamar.")


mi_celular = Celular("samsung", "galaxy", 999.99)

mi_celular.encender()

mi_celular.llamar("300-475-2139")

mi_celular.apagar()

class Celular:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} se ha encendido.")
        else:
            print(f"{self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"{self.marca} {self.modelo} se ha apagado.")
        else:
            print(f"{self.marca} {self.modelo} ya está apagado.")

    def llamar(self, numero):
        if self.encendido:
            print(f"Llamando al número {numero}...")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para llamar.")


mi_celular = Celular("huawei", "20pro", 999.99)

mi_celular.encender()

mi_celular.llamar("330-285-1239")

mi_celular.apagar()

class Celular:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} se ha encendido.")
        else:
            print(f"{self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"{self.marca} {self.modelo} se ha apagado.")
        else:
            print(f"{self.marca} {self.modelo} ya está apagado.")

    def llamar(self, numero):
        if self.encendido:
            print(f"Llamando al número {numero}...")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para llamar.")


mi_celular = Celular("lg", "prime", 999.99)

mi_celular.encender()

mi_celular.llamar("314-535-3219")

mi_celular.apagar()


# carro
class Carro:
    def __init__(self, marca, modelo, año, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} se ha encendido.")
        else:
            print(f"{self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad_actual = 0
            print(f"{self.marca} {self.modelo} se ha apagado.")
        else:
            print(f"{self.marca} {self.modelo} ya está apagado.")

    def acelerar(self, cantidad):
        if self.encendido:
            if self.velocidad_actual + cantidad <= self.velocidad_maxima:
                self.velocidad_actual += cantidad
                print(f"{self.marca} {self.modelo} ha acelerado a {self.velocidad_actual} km/h.")
            else:
                print(f"No puedes acelerar más allá de la velocidad máxima de {self.velocidad_maxima} km/h.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para acelerar.")

    def frenar(self, cantidad):
        if self.encendido:
            if self.velocidad_actual - cantidad >= 0:
                self.velocidad_actual -= cantidad
                print(f"{self.marca} {self.modelo} ha frenado a {self.velocidad_actual} km/h.")
            else:
                print(f"{self.marca} {self.modelo} ya está detenido.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para frenar.")

#
mi_carro = Carro("Ford", "Fiesta", 2014, 180)

mi_carro.encender()

mi_carro.acelerar(60)

mi_carro.frenar(20)

mi_carro.apagar()

class Carro:
    def __init__(self, marca, modelo, año, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} se ha encendido.")
        else:
            print(f"{self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad_actual = 0
            print(f"{self.marca} {self.modelo} se ha apagado.")
        else:
            print(f"{self.marca} {self.modelo} ya está apagado.")

    def acelerar(self, cantidad):
        if self.encendido:
            if self.velocidad_actual + cantidad <= self.velocidad_maxima:
                self.velocidad_actual += cantidad
                print(f"{self.marca} {self.modelo} ha acelerado a {self.velocidad_actual} km/h.")
            else:
                print(f"No puedes acelerar más allá de la velocidad máxima de {self.velocidad_maxima} km/h.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para acelerar.")

    def frenar(self, cantidad):
        if self.encendido:
            if self.velocidad_actual - cantidad >= 0:
                self.velocidad_actual -= cantidad
                print(f"{self.marca} {self.modelo} ha frenado a {self.velocidad_actual} km/h.")
            else:
                print(f"{self.marca} {self.modelo} ya está detenido.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para frenar.")

#
mi_carro = Carro("subaru", "impreza", 2007, 180)

mi_carro.encender()

mi_carro.acelerar(80)

mi_carro.frenar(20)

mi_carro.apagar()

class Carro:
    def __init__(self, marca, modelo, año, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} se ha encendido.")
        else:
            print(f"{self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad_actual = 0
            print(f"{self.marca} {self.modelo} se ha apagado.")
        else:
            print(f"{self.marca} {self.modelo} ya está apagado.")

    def acelerar(self, cantidad):
        if self.encendido:
            if self.velocidad_actual + cantidad <= self.velocidad_maxima:
                self.velocidad_actual += cantidad
                print(f"{self.marca} {self.modelo} ha acelerado a {self.velocidad_actual} km/h.")
            else:
                print(f"No puedes acelerar más allá de la velocidad máxima de {self.velocidad_maxima} km/h.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para acelerar.")

    def frenar(self, cantidad):
        if self.encendido:
            if self.velocidad_actual - cantidad >= 0:
                self.velocidad_actual -= cantidad
                print(f"{self.marca} {self.modelo} ha frenado a {self.velocidad_actual} km/h.")
            else:
                print(f"{self.marca} {self.modelo} ya está detenido.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para frenar.")

#
mi_carro = Carro("porshe", "gt3rs", 2023, 330)

mi_carro.encender()

mi_carro.acelerar(220)

mi_carro.frenar(140)

mi_carro.apagar()


class Carro:
    def __init__(self, marca, modelo, año, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} se ha encendido.")
        else:
            print(f"{self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad_actual = 0
            print(f"{self.marca} {self.modelo} se ha apagado.")
        else:
            print(f"{self.marca} {self.modelo} ya está apagado.")

    def acelerar(self, cantidad):
        if self.encendido:
            if self.velocidad_actual + cantidad <= self.velocidad_maxima:
                self.velocidad_actual += cantidad
                print(f"{self.marca} {self.modelo} ha acelerado a {self.velocidad_actual} km/h.")
            else:
                print(f"No puedes acelerar más allá de la velocidad máxima de {self.velocidad_maxima} km/h.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para acelerar.")

    def frenar(self, cantidad):
        if self.encendido:
            if self.velocidad_actual - cantidad >= 0:
                self.velocidad_actual -= cantidad
                print(f"{self.marca} {self.modelo} ha frenado a {self.velocidad_actual} km/h.")
            else:
                print(f"{self.marca} {self.modelo} ya está detenido.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para frenar.")

#
mi_carro = Carro("bmw", "m3", 2016, 250)

mi_carro.encender()

mi_carro.acelerar(200)

mi_carro.frenar(30)

mi_carro.apagar()

class Carro:
    def __init__(self, marca, modelo, año, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} se ha encendido.")
        else:
            print(f"{self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad_actual = 0
            print(f"{self.marca} {self.modelo} se ha apagado.")
        else:
            print(f"{self.marca} {self.modelo} ya está apagado.")

    def acelerar(self, cantidad):
        if self.encendido:
            if self.velocidad_actual + cantidad <= self.velocidad_maxima:
                self.velocidad_actual += cantidad
                print(f"{self.marca} {self.modelo} ha acelerado a {self.velocidad_actual} km/h.")
            else:
                print(f"No puedes acelerar más allá de la velocidad máxima de {self.velocidad_maxima} km/h.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para acelerar.")

    def frenar(self, cantidad):
        if self.encendido:
            if self.velocidad_actual - cantidad >= 0:
                self.velocidad_actual -= cantidad
                print(f"{self.marca} {self.modelo} ha frenado a {self.velocidad_actual} km/h.")
            else:
                print(f"{self.marca} {self.modelo} ya está detenido.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para frenar.")

#
mi_carro = Carro("Ferrari", "F50", 2006, 280)

mi_carro.encender()

mi_carro.acelerar(150)

mi_carro.frenar(80)

mi_carro.apagar()


#oficina

class Oficina:
    def __init__(self, nombre, direccion, capacidad_maxima):
        self.nombre = nombre
        self.direccion = direccion
        self.capacidad_maxima = capacidad_maxima
        self.empleados = []

    def agregar_empleado(self, empleado):
        if len(self.empleados) < self.capacidad_maxima:
            self.empleados.append(empleado)
            print(f"{empleado.nombre} ha sido agregado a la oficina {self.nombre}.")
        else:
            print(f"La oficina {self.nombre} está llena. No se puede agregar más empleados.")

    def listar_empleados(self):
        print(f"Empleados en la oficina {self.nombre}:")
        for empleado in self.empleados:
            print(empleado.nombre)

class Empleado:
    def __init__(self, nombre, puesto):
        self.nombre = nombre
        self.puesto = puesto

empleado1 = Empleado("Juan Perez", "Gerente")
empleado2 = Empleado("Maria Rodriguez", "Desarrollador")
empleado3 = Empleado("Carlos Gonzalez", "Diseñador")
empleado4 = Empleado("Bernardo Dicaprio", "vendedor")
empleado5 = Empleado("Wilber Varela", "seguridad")
empleado6 = Empleado("Pedro tejada", "contador")

oficina1 = Oficina("Oficina Principal", "123 Calle Principal", 5)

oficina1.agregar_empleado(empleado1)
oficina1.agregar_empleado(empleado2)
oficina1.agregar_empleado(empleado3)
oficina1.agregar_empleado(empleado4)
oficina1.agregar_empleado(empleado5)
oficina1.agregar_empleado(empleado6)

oficina1.listar_empleados()


#mesa

class Mesa:
    def __init__(self, material, forma, capacidad):
        self.material = material
        self.forma = forma
        self.capacidad = capacidad
        self.objetos_en_la_mesa = []

    def colocar_objeto(self, objeto):
        if len(self.objetos_en_la_mesa) < self.capacidad:
            self.objetos_en_la_mesa.append(objeto)
            print(f"Se ha colocado un {objeto} en la mesa.")
        else:
            print(f"La mesa está llena. No se pueden colocar más objetos.")

    def retirar_objeto(self, objeto):
        if objeto in self.objetos_en_la_mesa:
            self.objetos_en_la_mesa.remove(objeto)
            print(f"Se ha retirado un {objeto} de la mesa.")
        else:
            print(f"No se encontró un {objeto} en la mesa.")

    def mostrar_objetos(self):
        print(f"Objetos en la mesa:")
        for objeto in self.objetos_en_la_mesa:
            print(objeto)

mi_mesa = Mesa("Madera", "Rectangular", 4)

mi_mesa.colocar_objeto("Libro")
mi_mesa.colocar_objeto("computador")
mi_mesa.colocar_objeto("pocillo")

mi_mesa.mostrar_objetos()

mi_mesa.retirar_objeto("pocillo")

mi_mesa.mostrar_objetos()

class Mesa:
    def __init__(self, material, forma, capacidad):
        self.material = material
        self.forma = forma
        self.capacidad = capacidad
        self.objetos_en_la_mesa = []

    def colocar_objeto(self, objeto):
        if len(self.objetos_en_la_mesa) < self.capacidad:
            self.objetos_en_la_mesa.append(objeto)
            print(f"Se ha colocado un {objeto} en la mesa.")
        else:
            print(f"La mesa está llena. No se pueden colocar más objetos.")

    def retirar_objeto(self, objeto):
        if objeto in self.objetos_en_la_mesa:
            self.objetos_en_la_mesa.remove(objeto)
            print(f"Se ha retirado un {objeto} de la mesa.")
        else:
            print(f"No se encontró un {objeto} en la mesa.")

    def mostrar_objetos(self):
        print(f"Objetos en la mesa:")
        for objeto in self.objetos_en_la_mesa:
            print(objeto)

mi_mesa = Mesa("Madera", "Rectangular", 4)

mi_mesa.colocar_objeto("taza")
mi_mesa.colocar_objeto("celular")
mi_mesa.colocar_objeto("lapiz")
mi_mesa.colocar_objeto("tablet")

mi_mesa.mostrar_objetos()

mi_mesa.retirar_objeto("celular")

mi_mesa.mostrar_objetos()

class Mesa:
    def __init__(self, material, forma, capacidad):
        self.material = material
        self.forma = forma
        self.capacidad = capacidad
        self.objetos_en_la_mesa = []

    def colocar_objeto(self, objeto):
        if len(self.objetos_en_la_mesa) < self.capacidad:
            self.objetos_en_la_mesa.append(objeto)
            print(f"Se ha colocado un {objeto} en la mesa.")
        else:
            print(f"La mesa está llena. No se pueden colocar más objetos.")

    def retirar_objeto(self, objeto):
        if objeto in self.objetos_en_la_mesa:
            self.objetos_en_la_mesa.remove(objeto)
            print(f"Se ha retirado un {objeto} de la mesa.")
        else:
            print(f"No se encontró un {objeto} en la mesa.")

    def mostrar_objetos(self):
        print(f"Objetos en la mesa:")
        for objeto in self.objetos_en_la_mesa:
            print(objeto)

mi_mesa = Mesa("Madera", "Rectangular", 4)

mi_mesa.colocar_objeto("vaso")
mi_mesa.colocar_objeto("celuar")
mi_mesa.colocar_objeto("cuaderno")
mi_mesa.colocar_objeto("llaves")

mi_mesa.mostrar_objetos()

mi_mesa.retirar_objeto("celular")

mi_mesa.mostrar_objetos()

class Mesa:
    def __init__(self, material, forma, capacidad):
        self.material = material
        self.forma = forma
        self.capacidad = capacidad
        self.objetos_en_la_mesa = []

    def colocar_objeto(self, objeto):
        if len(self.objetos_en_la_mesa) < self.capacidad:
            self.objetos_en_la_mesa.append(objeto)
            print(f"Se ha colocado un {objeto} en la mesa.")
        else:
            print(f"La mesa está llena. No se pueden colocar más objetos.")

    def retirar_objeto(self, objeto):
        if objeto in self.objetos_en_la_mesa:
            self.objetos_en_la_mesa.remove(objeto)
            print(f"Se ha retirado un {objeto} de la mesa.")
        else:
            print(f"No se encontró un {objeto} en la mesa.")

    def mostrar_objetos(self):
        print(f"Objetos en la mesa:")
        for objeto in self.objetos_en_la_mesa:
            print(objeto)

mi_mesa = Mesa("Madera", "Rectangular", 4)

mi_mesa.colocar_objeto("hojas")
mi_mesa.colocar_objeto("celular")
mi_mesa.colocar_objeto("grapadora")
mi_mesa.colocar_objeto("plato")

mi_mesa.mostrar_objetos()

mi_mesa.retirar_objeto("celular")

mi_mesa.mostrar_objetos()


class Mesa:
    def __init__(self, material, forma, capacidad):
        self.material = material
        self.forma = forma
        self.capacidad = capacidad
        self.objetos_en_la_mesa = []

    def colocar_objeto(self, objeto):
        if len(self.objetos_en_la_mesa) < self.capacidad:
            self.objetos_en_la_mesa.append(objeto)
            print(f"Se ha colocado un {objeto} en la mesa.")
        else:
            print(f"La mesa está llena. No se pueden colocar más objetos.")

    def retirar_objeto(self, objeto):
        if objeto in self.objetos_en_la_mesa:
            self.objetos_en_la_mesa.remove(objeto)
            print(f"Se ha retirado un {objeto} de la mesa.")
        else:
            print(f"No se encontró un {objeto} en la mesa.")

    def mostrar_objetos(self):
        print(f"Objetos en la mesa:")
        for objeto in self.objetos_en_la_mesa:
            print(objeto)

mi_mesa = Mesa("Madera", "Rectangular", 4)

mi_mesa.colocar_objeto("sombrilla")
mi_mesa.colocar_objeto("celular")
mi_mesa.colocar_objeto("borrador")
mi_mesa.colocar_objeto("control")

mi_mesa.mostrar_objetos()

mi_mesa.retirar_objeto("celular")

mi_mesa.mostrar_objetos()


#llaves

class Llaves:
    def __init__(self, marca, material, cantidad):
        self.marca = marca
        self.material = material
        self.cantidad = cantidad

    def agregar_llave(self):
        self.cantidad += 1
        print(f"Se ha agregado una llave {self.marca} a la colección.")

    def quitar_llave(self):
        if self.cantidad > 0:
            self.cantidad -= 1
            print(f"Se ha quitado una llave {self.marca} de la colección.")
        else:
            print("La colección de llaves está vacía.")

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Material: {self.material}")
        print(f"Cantidad: {self.cantidad}")

mis_llaves = Llaves("Yale", "Metal", 3)

mis_llaves.mostrar_info()

mis_llaves.agregar_llave()

mis_llaves.quitar_llave()

mis_llaves.mostrar_info()

class Llaves:
    def __init__(self, marca, material, cantidad):
        self.marca = marca
        self.material = material
        self.cantidad = cantidad

    def agregar_llave(self):
        self.cantidad += 1
        print(f"Se ha agregado una llave {self.marca} a la colección.")

    def quitar_llave(self):
        if self.cantidad > 0:
            self.cantidad -= 1
            print(f"Se ha quitado una llave {self.marca} de la colección.")
        else:
            print("La colección de llaves está vacía.")

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Material: {self.material}")
        print(f"Cantidad: {self.cantidad}")

mis_llaves = Llaves("Yes", "Metal", 4)

mis_llaves.mostrar_info()

mis_llaves.agregar_llave()

mis_llaves.quitar_llave()

mis_llaves.mostrar_info()

class Llaves:
    def __init__(self, marca, material, cantidad):
        self.marca = marca
        self.material = material
        self.cantidad = cantidad

    def agregar_llave(self):
        self.cantidad += 1
        print(f"Se ha agregado una llave {self.marca} a la colección.")

    def quitar_llave(self):
        if self.cantidad > 0:
            self.cantidad -= 1
            print(f"Se ha quitado una llave {self.marca} de la colección.")
        else:
            print("La colección de llaves está vacía.")

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Material: {self.material}")
        print(f"Cantidad: {self.cantidad}")

mis_llaves = Llaves("floodr", "Metal", 2)

mis_llaves.mostrar_info()

mis_llaves.agregar_llave()

mis_llaves.quitar_llave()

mis_llaves.mostrar_info()

class Llaves:
    def __init__(self, marca, material, cantidad):
        self.marca = marca
        self.material = material
        self.cantidad = cantidad

    def agregar_llave(self):
        self.cantidad += 1
        print(f"Se ha agregado una llave {self.marca} a la colección.")

    def quitar_llave(self):
        if self.cantidad > 0:
            self.cantidad -= 1
            print(f"Se ha quitado una llave {self.marca} de la colección.")
        else:
            print("La colección de llaves está vacía.")

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Material: {self.material}")
        print(f"Cantidad: {self.cantidad}")

mis_llaves = Llaves("RINO", "Metal", 7)

mis_llaves.mostrar_info()

mis_llaves.agregar_llave()

mis_llaves.quitar_llave()

mis_llaves.mostrar_info()

class Llaves:
    def __init__(self, marca, material, cantidad):
        self.marca = marca
        self.material = material
        self.cantidad = cantidad

    def agregar_llave(self):
        self.cantidad += 1
        print(f"Se ha agregado una llave {self.marca} a la colección.")

    def quitar_llave(self):
        if self.cantidad > 0:
            self.cantidad -= 1
            print(f"Se ha quitado una llave {self.marca} de la colección.")
        else:
            print("La colección de llaves está vacía.")

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Material: {self.material}")
        print(f"Cantidad: {self.cantidad}")

mis_llaves = Llaves("munoz", "Metal", 0)

mis_llaves.mostrar_info()

mis_llaves.agregar_llave()

mis_llaves.quitar_llave()

mis_llaves.mostrar_info()

#computador
class Computador:
    def __init__(self, marca, modelo, sistema_operativo):
        self.marca = marca
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} se ha encendido.")
        else:
            print(f"{self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"{self.marca} {self.modelo} se ha apagado.")
        else:
            print(f"{self.marca} {self.modelo} ya está apagado.")

    def abrir_aplicacion(self, aplicacion):
        if self.encendido:
            print(f"Abriendo la aplicación {aplicacion} en {self.sistema_operativo}.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para abrir aplicaciones.")


mi_computador = Computador("Dell", "XPS 15", "Windows 10")

mi_computador.encender()

mi_computador.abrir_aplicacion("Editor de Texto")

mi_computador.apagar()

class Computador:
    def __init__(self, marca, modelo, sistema_operativo):
        self.marca = marca
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} se ha encendido.")
        else:
            print(f"{self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"{self.marca} {self.modelo} se ha apagado.")
        else:
            print(f"{self.marca} {self.modelo} ya está apagado.")

    def abrir_aplicacion(self, aplicacion):
        if self.encendido:
            print(f"Abriendo la aplicación {aplicacion} en {self.sistema_operativo}.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para abrir aplicaciones.")


mi_computador = Computador("hp", "240 g9", "Windows 11")

mi_computador.encender()

mi_computador.abrir_aplicacion("paint")

mi_computador.apagar()

class Computador:
    def __init__(self, marca, modelo, sistema_operativo):
        self.marca = marca
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} se ha encendido.")
        else:
            print(f"{self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"{self.marca} {self.modelo} se ha apagado.")
        else:
            print(f"{self.marca} {self.modelo} ya está apagado.")

    def abrir_aplicacion(self, aplicacion):
        if self.encendido:
            print(f"Abriendo la aplicación {aplicacion} en {self.sistema_operativo}.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para abrir aplicaciones.")


mi_computador = Computador("ASUS", "vivobook 15", "Windows 10")

mi_computador.encender()

mi_computador.abrir_aplicacion("virtual studio")

mi_computador.apagar()

class Computador:
    def __init__(self, marca, modelo, sistema_operativo):
        self.marca = marca
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} se ha encendido.")
        else:
            print(f"{self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"{self.marca} {self.modelo} se ha apagado.")
        else:
            print(f"{self.marca} {self.modelo} ya está apagado.")

    def abrir_aplicacion(self, aplicacion):
        if self.encendido:
            print(f"Abriendo la aplicación {aplicacion} en {self.sistema_operativo}.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para abrir aplicaciones.")


mi_computador = Computador("mac", "macbook pro", "OS X 10.9.5")

mi_computador.encender()

mi_computador.abrir_aplicacion("safari")

mi_computador.apagar()
class Computador:
    def __init__(self, marca, modelo, sistema_operativo):
        self.marca = marca
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} se ha encendido.")
        else:
            print(f"{self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"{self.marca} {self.modelo} se ha apagado.")
        else:
            print(f"{self.marca} {self.modelo} ya está apagado.")

    def abrir_aplicacion(self, aplicacion):
        if self.encendido:
            print(f"Abriendo la aplicación {aplicacion} en {self.sistema_operativo}.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para abrir aplicaciones.")


mi_computador = Computador("lenovo", "ideapad", "Windows 12")

mi_computador.encender()

mi_computador.abrir_aplicacion("excel")

mi_computador.apagar()


#televisor

class Televisor:
    def __init__(self, marca, modelo, pulgadas):
        self.marca = marca
        self.modelo = modelo
        self.pulgadas = pulgadas
        self.encendido = False
        self.canal_actual = 1
        self.volumen = 50

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} se ha encendido.")
        else:
            print(f"{self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"{self.marca} {self.modelo} se ha apagado.")
        else:
            print(f"{self.marca} {self.modelo} ya está apagado.")

    def cambiar_canal(self, canal):
        if self.encendido:
            self.canal_actual = canal
            print(f"Cambiando al canal {canal}.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para cambiar de canal.")

    def ajustar_volumen(self, cantidad):
        if self.encendido:
            if 0 <= self.volumen + cantidad <= 100:
                self.volumen += cantidad
                print(f"Volumen ajustado a {self.volumen}.")
            else:
                print("El volumen está fuera del rango permitido.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para ajustar el volumen.")

    def mostrar_estado(self):
        estado = "encendido" if self.encendido else "apagado"
        print(f"{self.marca} {self.modelo} - Estado: {estado}, Canal: {self.canal_actual}, Volumen: {self.volumen}")

mi_televisor = Televisor("Sony", "Bravia", 55)

mi_televisor.encender()

mi_televisor.cambiar_canal(5)

mi_televisor.ajustar_volumen(10)

mi_televisor.mostrar_estado()

mi_televisor.apagar()

class Televisor:
    def __init__(self, marca, modelo, pulgadas):
        self.marca = marca
        self.modelo = modelo
        self.pulgadas = pulgadas
        self.encendido = False
        self.canal_actual = 1
        self.volumen = 50

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} se ha encendido.")
        else:
            print(f"{self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"{self.marca} {self.modelo} se ha apagado.")
        else:
            print(f"{self.marca} {self.modelo} ya está apagado.")

    def cambiar_canal(self, canal):
        if self.encendido:
            self.canal_actual = canal
            print(f"Cambiando al canal {canal}.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para cambiar de canal.")

    def ajustar_volumen(self, cantidad):
        if self.encendido:
            if 0 <= self.volumen + cantidad <= 100:
                self.volumen += cantidad
                print(f"Volumen ajustado a {self.volumen}.")
            else:
                print("El volumen está fuera del rango permitido.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para ajustar el volumen.")

    def mostrar_estado(self):
        estado = "encendido" if self.encendido else "apagado"
        print(f"{self.marca} {self.modelo} - Estado: {estado}, Canal: {self.canal_actual}, Volumen: {self.volumen}")

mi_televisor = Televisor("LG", "formi", 50)

mi_televisor.encender()

mi_televisor.cambiar_canal(12)

mi_televisor.ajustar_volumen(30)

mi_televisor.mostrar_estado()

mi_televisor.apagar()

class Televisor:
    def __init__(self, marca, modelo, pulgadas):
        self.marca = marca
        self.modelo = modelo
        self.pulgadas = pulgadas
        self.encendido = False
        self.canal_actual = 1
        self.volumen = 50

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} se ha encendido.")
        else:
            print(f"{self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"{self.marca} {self.modelo} se ha apagado.")
        else:
            print(f"{self.marca} {self.modelo} ya está apagado.")

    def cambiar_canal(self, canal):
        if self.encendido:
            self.canal_actual = canal
            print(f"Cambiando al canal {canal}.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para cambiar de canal.")

    def ajustar_volumen(self, cantidad):
        if self.encendido:
            if 0 <= self.volumen + cantidad <= 100:
                self.volumen += cantidad
                print(f"Volumen ajustado a {self.volumen}.")
            else:
                print("El volumen está fuera del rango permitido.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para ajustar el volumen.")

    def mostrar_estado(self):
        estado = "encendido" if self.encendido else "apagado"
        print(f"{self.marca} {self.modelo} - Estado: {estado}, Canal: {self.canal_actual}, Volumen: {self.volumen}")

mi_televisor = Televisor("samnsung", "vive", 32)

mi_televisor.encender()

mi_televisor.cambiar_canal(7)

mi_televisor.ajustar_volumen(15)

mi_televisor.mostrar_estado()

mi_televisor.apagar()
class Televisor:
    def __init__(self, marca, modelo, pulgadas):
        self.marca = marca
        self.modelo = modelo
        self.pulgadas = pulgadas
        self.encendido = False
        self.canal_actual = 1
        self.volumen = 50

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} se ha encendido.")
        else:
            print(f"{self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"{self.marca} {self.modelo} se ha apagado.")
        else:
            print(f"{self.marca} {self.modelo} ya está apagado.")

    def cambiar_canal(self, canal):
        if self.encendido:
            self.canal_actual = canal
            print(f"Cambiando al canal {canal}.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para cambiar de canal.")

    def ajustar_volumen(self, cantidad):
        if self.encendido:
            if 0 <= self.volumen + cantidad <= 100:
                self.volumen += cantidad
                print(f"Volumen ajustado a {self.volumen}.")
            else:
                print("El volumen está fuera del rango permitido.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para ajustar el volumen.")

    def mostrar_estado(self):
        estado = "encendido" if self.encendido else "apagado"
        print(f"{self.marca} {self.modelo} - Estado: {estado}, Canal: {self.canal_actual}, Volumen: {self.volumen}")

mi_televisor = Televisor("hyundai", "brabus", 70)

mi_televisor.encender()

mi_televisor.cambiar_canal(1)

mi_televisor.ajustar_volumen(40)

mi_televisor.mostrar_estado()

mi_televisor.apagar()

class Televisor:
    def __init__(self, marca, modelo, pulgadas):
        self.marca = marca
        self.modelo = modelo
        self.pulgadas = pulgadas
        self.encendido = False
        self.canal_actual = 1
        self.volumen = 50

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} se ha encendido.")
        else:
            print(f"{self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"{self.marca} {self.modelo} se ha apagado.")
        else:
            print(f"{self.marca} {self.modelo} ya está apagado.")

    def cambiar_canal(self, canal):
        if self.encendido:
            self.canal_actual = canal
            print(f"Cambiando al canal {canal}.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para cambiar de canal.")

    def ajustar_volumen(self, cantidad):
        if self.encendido:
            if 0 <= self.volumen + cantidad <= 100:
                self.volumen += cantidad
                print(f"Volumen ajustado a {self.volumen}.")
            else:
                print("El volumen está fuera del rango permitido.")
        else:
            print(f"{self.marca} {self.modelo} está apagado. Enciéndelo para ajustar el volumen.")

    def mostrar_estado(self):
        estado = "encendido" if self.encendido else "apagado"
        print(f"{self.marca} {self.modelo} - Estado: {estado}, Canal: {self.canal_actual}, Volumen: {self.volumen}")

mi_televisor = Televisor("challenger", "pros", 45)

mi_televisor.encender()

mi_televisor.cambiar_canal(30)

mi_televisor.ajustar_volumen(60)

mi_televisor.mostrar_estado()

mi_televisor.apagar()



#lapiz
class Lapiz:
    def __init__(self, marca, color, longitud):
        self.marca = marca
        self.color = color
        self.longitud = longitud

    def escribir(self, texto):
        if self.longitud > 0:
            print(f"Escribiendo en color {self.color}: {texto}")
            self.longitud -= len(texto)
        else:
            print("El lápiz se quedó sin punta. Debes afilarlo.")

    def afilar(self):
        print("Afilando el lápiz...")
        self.longitud = 100  # Reinicia la longitud del lápiz

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Longitud: {self.longitud}%")

mi_lapiz = Lapiz("Faber-Castell", "Azul", 80)

mi_lapiz.escribir("ganare programacion")

mi_lapiz.mostrar_info()

mi_lapiz.afilar()

mi_lapiz.mostrar_info()

class Lapiz:
    def __init__(self, marca, color, longitud):
        self.marca = marca
        self.color = color
        self.longitud = longitud

    def escribir(self, texto):
        if self.longitud > 0:
            print(f"Escribiendo en color {self.color}: {texto}")
            self.longitud -= len(texto)
        else:
            print("El lápiz se quedó sin punta. Debes afilarlo.")

    def afilar(self):
        print("Afilando el lápiz...")
        self.longitud = 100  # Reinicia la longitud del lápiz

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Longitud: {self.longitud}%")

mi_lapiz = Lapiz("pilot", "Amarillo", 0)

mi_lapiz.escribir("ganare programacion")

mi_lapiz.mostrar_info()

mi_lapiz.afilar()

mi_lapiz.mostrar_info()

class Lapiz:
    def __init__(self, marca, color, longitud):
        self.marca = marca
        self.color = color
        self.longitud = longitud

    def escribir(self, texto):
        if self.longitud > 0:
            print(f"Escribiendo en color {self.color}: {texto}")
            self.longitud -= len(texto)
        else:
            print("El lápiz se quedó sin punta. Debes afilarlo.")

    def afilar(self):
        print("Afilando el lápiz...")
        self.longitud = 100  # Reinicia la longitud del lápiz

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Longitud: {self.longitud}%")

mi_lapiz = Lapiz("prismacolor", "rojo", 100)

mi_lapiz.escribir("programacion ahi voy")

mi_lapiz.mostrar_info()

mi_lapiz.afilar()

mi_lapiz.mostrar_info()

class Lapiz:
    def __init__(self, marca, color, longitud):
        self.marca = marca
        self.color = color
        self.longitud = longitud

    def escribir(self, texto):
        if self.longitud > 0:
            print(f"Escribiendo en color {self.color}: {texto}")
            self.longitud -= len(texto)
        else:
            print("El lápiz se quedó sin punta. Debes afilarlo.")

    def afilar(self):
        print("Afilando el lápiz...")
        self.longitud = 100  # Reinicia la longitud del lápiz

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Longitud: {self.longitud}%")

mi_lapiz = Lapiz("norma", "blanco", 50)

mi_lapiz.escribir("programar es lo mio")

mi_lapiz.mostrar_info()

mi_lapiz.afilar()

mi_lapiz.mostrar_info()

class Lapiz:
    def __init__(self, marca, color, longitud):
        self.marca = marca
        self.color = color
        self.longitud = longitud

    def escribir(self, texto):
        if self.longitud > 0:
            print(f"Escribiendo en color {self.color}: {texto}")
            self.longitud -= len(texto)
        else:
            print("El lápiz se quedó sin punta. Debes afilarlo.")

    def afilar(self):
        print("Afilando el lápiz...")
        self.longitud = 100  # Reinicia la longitud del lápiz

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Longitud: {self.longitud}%")

mi_lapiz = Lapiz("graffit", "negro", 90)

mi_lapiz.escribir("i love programar")

mi_lapiz.mostrar_info()

mi_lapiz.afilar()

mi_lapiz.mostrar_info()

#calculadora

class Calculadora:
    def __init__(self):
        self.resultado = 0

    def sumar(self, numero):
        self.resultado += numero

    def restar(self, numero):
        self.resultado -= numero

    def multiplicar(self, numero):
        self.resultado *= numero

    def dividir(self, numero):
        if numero != 0:
            self.resultado /= numero
        else:
            print("Error: No se puede dividir por cero.")

    def mostrar_resultado(self):
        print(f"Resultado: {self.resultado}")

mi_calculadora = Calculadora()

mi_calculadora.sumar(5)
mi_calculadora.multiplicar(3)
mi_calculadora.restar(2)
mi_calculadora.dividir(4)

mi_calculadora.mostrar_resultado()


#maletin

class Maletin:
    def __init__(self, marca, capacidad_maxima):
        self.marca = marca
        self.capacidad_maxima = capacidad_maxima
        self.contenido = []

    def agregar_item(self, item):
        if len(self.contenido) < self.capacidad_maxima:
            self.contenido.append(item)
            print(f"Se ha agregado un {item} al maletín.")
        else:
            print(f"El maletín está lleno. No se pueden agregar más elementos.")

    def quitar_item(self, item):
        if item in self.contenido:
            self.contenido.remove(item)
            print(f"Se ha quitado un {item} del maletín.")
        else:
            print(f"No se encontró un {item} en el maletín.")

    def mostrar_contenido(self):
        print(f"Contenido del maletín {self.marca}:")
        for item in self.contenido:
            print(item)

mi_maletin = Maletin("elementos", 5)

mi_maletin.agregar_item("computador")
mi_maletin.agregar_item("Libros")
mi_maletin.agregar_item("Ropa")

mi_maletin.mostrar_contenido()

mi_maletin.quitar_item("ropa")

mi_maletin.mostrar_contenido()

class Maletin:
    def __init__(self, marca, capacidad_maxima):
        self.marca = marca
        self.capacidad_maxima = capacidad_maxima
        self.contenido = []
    def agregar_item(self, item):
        if len(self.contenido) < self.capacidad_maxima:
            self.contenido.append(item)
            print(f"Se ha agregado un {item} al maletín.")
        else:
            print(f"El maletín está lleno. No se pueden agregar más elementos.")

    def quitar_item(self, item):
        if item in self.contenido:
            self.contenido.remove(item)
            print(f"Se ha quitado un {item} del maletín.")
        else:
            print(f"No se encontró un {item} en el maletín.")

    def mostrar_contenido(self):
        print(f"Contenido del maletín {self.marca}:")
        for item in self.contenido:
            print(item)

mi_maletin = Maletin("elementos", 6)

mi_maletin.agregar_item("celular")
mi_maletin.agregar_item("sombrilla")
mi_maletin.agregar_item("llaves")
mi_maletin.agregar_item("cuaderno")

mi_maletin.mostrar_contenido()

mi_maletin.quitar_item("llaves")

mi_maletin.mostrar_contenido()


class Maletin:
    def __init__(self, marca, capacidad_maxima):
        self.marca = marca
        self.capacidad_maxima = capacidad_maxima
        self.contenido = []
    def agregar_item(self, item):
        if len(self.contenido) < self.capacidad_maxima:
            self.contenido.append(item)
            print(f"Se ha agregado un {item} al maletín.")
        else:
            print(f"El maletín está lleno. No se pueden agregar más elementos.")

    def quitar_item(self, item):
        if item in self.contenido:
            self.contenido.remove(item)
            print(f"Se ha quitado un {item} del maletín.")
        else:
            print(f"No se encontró un {item} en el maletín.")

    def mostrar_contenido(self):
        print(f"Contenido del maletín {self.marca}:")
        for item in self.contenido:
            print(item)

mi_maletin = Maletin("elementos", 4)

mi_maletin.agregar_item("locion")
mi_maletin.agregar_item("cartuchera")
mi_maletin.agregar_item("calculadora")
mi_maletin.agregar_item("locion")

mi_maletin.mostrar_contenido()

mi_maletin.quitar_item("locion")

mi_maletin.mostrar_contenido()

class Maletin:
    def __init__(self, marca, capacidad_maxima):
        self.marca = marca
        self.capacidad_maxima = capacidad_maxima
        self.contenido = []
    def agregar_item(self, item):
        if len(self.contenido) < self.capacidad_maxima:
            self.contenido.append(item)
            print(f"Se ha agregado un {item} al maletín.")
        else:
            print(f"El maletín está lleno. No se pueden agregar más elementos.")

    def quitar_item(self, item):
        if item in self.contenido:
            self.contenido.remove(item)
            print(f"Se ha quitado un {item} del maletín.")
        else:
            print(f"No se encontró un {item} en el maletín.")

    def mostrar_contenido(self):
        print(f"Contenido del maletín {self.marca}:")
        for item in self.contenido:
            print(item)

mi_maletin = Maletin("elementos", 9)

mi_maletin.agregar_item("botella")
mi_maletin.agregar_item("coca")
mi_maletin.agregar_item("monedas")
mi_maletin.agregar_item("alcohol")

mi_maletin.mostrar_contenido()

mi_maletin.quitar_item("alcohol")

mi_maletin.mostrar_contenido()

#archivador
class Archivador:
    def __init__(self, marca, capacidad_maxima):
        self.marca = marca
        self.capacidad_maxima = capacidad_maxima
        self.documentos = []

    def agregar_documento(self, documento):
        if len(self.documentos) < self.capacidad_maxima:
            self.documentos.append(documento)
            print(f"Se ha agregado el documento '{documento}' al archivador.")
        else:
            print(f"El archivador está lleno. No se pueden agregar más documentos.")

    def quitar_documento(self, documento):
        if documento in self.documentos:
            self.documentos.remove(documento)
            print(f"Se ha quitado el documento '{documento}' del archivador.")
        else:
            print(f"No se encontró el documento '{documento}' en el archivador.")

    def mostrar_documentos(self):
        print(f"Documentos en el archivador {self.marca}:")
        for documento in self.documentos:
            print(documento)

mi_archivador = Archivador("OfficeMax", 20)

mi_archivador.agregar_documento("Contrato de venta")
mi_archivador.agregar_documento("Informe trimestral")
mi_archivador.agregar_documento("Facturas")

mi_archivador.mostrar_documentos()

mi_archivador.quitar_documento("Informe trimestral")

mi_archivador.mostrar_documentos()

class Archivador:
    def __init__(self, marca, capacidad_maxima):
        self.marca = marca
        self.capacidad_maxima = capacidad_maxima
        self.documentos = []

    def agregar_documento(self, documento):
        if len(self.documentos) < self.capacidad_maxima:
            self.documentos.append(documento)
            print(f"Se ha agregado el documento '{documento}' al archivador.")
        else:
            print(f"El archivador está lleno. No se pueden agregar más documentos.")

    def quitar_documento(self, documento):
        if documento in self.documentos:
            self.documentos.remove(documento)
            print(f"Se ha quitado el documento '{documento}' del archivador.")
        else:
            print(f"No se encontró el documento '{documento}' en el archivador.")

    def mostrar_documentos(self):
        print(f"Documentos en el archivador {self.marca}:")
        for documento in self.documentos:
            print(documento)

mi_archivador = Archivador("Officio", 30)

mi_archivador.agregar_documento("Contrato de arriendo")
mi_archivador.agregar_documento("Informe anual")
mi_archivador.agregar_documento("recibos")

mi_archivador.mostrar_documentos()

mi_archivador.quitar_documento("recibos")

mi_archivador.mostrar_documentos()

class Archivador:
    def __init__(self, marca, capacidad_maxima):
        self.marca = marca
        self.capacidad_maxima = capacidad_maxima
        self.documentos = []

    def agregar_documento(self, documento):
        if len(self.documentos) < self.capacidad_maxima:
            self.documentos.append(documento)
            print(f"Se ha agregado el documento '{documento}' al archivador.")
        else:
            print(f"El archivador está lleno. No se pueden agregar más documentos.")

    def quitar_documento(self, documento):
        if documento in self.documentos:
            self.documentos.remove(documento)
            print(f"Se ha quitado el documento '{documento}' del archivador.")
        else:
            print(f"No se encontró el documento '{documento}' en el archivador.")

    def mostrar_documentos(self):
        print(f"Documentos en el archivador {self.marca}:")
        for documento in self.documentos:
            print(documento)

mi_archivador = Archivador("cartaMax", 40)

mi_archivador.agregar_documento("Contrato de seguro")
mi_archivador.agregar_documento("Informe diario")
mi_archivador.agregar_documento("seguro")

mi_archivador.mostrar_documentos()

mi_archivador.quitar_documento("seguro")

mi_archivador.mostrar_documentos()

class Archivador:
    def __init__(self, marca, capacidad_maxima):
        self.marca = marca
        self.capacidad_maxima = capacidad_maxima
        self.documentos = []

    def agregar_documento(self, documento):
        if len(self.documentos) < self.capacidad_maxima:
            self.documentos.append(documento)
            print(f"Se ha agregado el documento '{documento}' al archivador.")
        else:
            print(f"El archivador está lleno. No se pueden agregar más documentos.")

    def quitar_documento(self, documento):
        if documento in self.documentos:
            self.documentos.remove(documento)
            print(f"Se ha quitado el documento '{documento}' del archivador.")
        else:
            print(f"No se encontró el documento '{documento}' en el archivador.")

    def mostrar_documentos(self):
        print(f"Documentos en el archivador {self.marca}:")
        for documento in self.documentos:
            print(documento)

mi_archivador = Archivador("Officeplus", 22)

mi_archivador.agregar_documento("recibo de venta")
mi_archivador.agregar_documento("Informe semanal")
mi_archivador.agregar_documento("contratos")

mi_archivador.mostrar_documentos()

mi_archivador.quitar_documento("Informe semanal")

mi_archivador.mostrar_documentos()


class Archivador:
    def __init__(self, marca, capacidad_maxima):
        self.marca = marca
        self.capacidad_maxima = capacidad_maxima
        self.documentos = []

    def agregar_documento(self, documento):
        if len(self.documentos) < self.capacidad_maxima:
            self.documentos.append(documento)
            print(f"Se ha agregado el documento '{documento}' al archivador.")
        else:
            print(f"El archivador está lleno. No se pueden agregar más documentos.")

    def quitar_documento(self, documento):
        if documento in self.documentos:
            self.documentos.remove(documento)
            print(f"Se ha quitado el documento '{documento}' del archivador.")
        else:
            print(f"No se encontró el documento '{documento}' en el archivador.")

    def mostrar_documentos(self):
        print(f"Documentos en el archivador {self.marca}:")
        for documento in self.documentos:
            print(documento)

mi_archivador = Archivador("OfficeMax", 15)

mi_archivador.agregar_documento("hojas de vida")
mi_archivador.agregar_documento("Informe avances")
mi_archivador.agregar_documento("carta de renuncia")

mi_archivador.mostrar_documentos()

mi_archivador.quitar_documento("Informe avances")

mi_archivador.mostrar_documentos()
