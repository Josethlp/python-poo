"""
Esta historia trata sobre Fran, Alex, María.

Fran vive en Palma de Mallorca y tiene un perro llamado Anaconda,
nació el 4 de abril de 1990 y en el momento en el que se escribe la historia tiene la edad de 29 años.
No es necesario definir el sexo de Fran pero para que no quede duda Fran es hombre.

Alex es de Madrid, no tiene animales y nació el 29 de febrero de 2000,
fue un año bisiesto por eso es especial. Además, Alex utiliza Tinder y
es de los que se ponen en la descripción 'Soy un hombre especial, salúdame y te cuento'.

María es de Alicante, nació el 1 de enero de 1993 y tiene 2 perros llamados Sam y Roy.

Anaconda es el perro de Fran, es un Pitbull nacido el 1 de julio de 2018.

Sam y Roy son los perros de María, son dos chuchos (sin raza) y el primero nació el 1 de mayo de 2015 y el segundo el 5 de junio de 2016.

Fran se compra un coche, un Audi A1 blanco 'too guapo' y María un Range Rover Evoque 'too chulo' matriculados los dos el 1 de enero de 2017.

Además de todo esto, a la historia hay que añadir 2 perros más que acaban de aparecer por arte de magia y no tienen dueño,
el primero es Rocky y el segundo es Cobra, además, no sabemos ni la raza ni la fecha de nacimiento.
"""



"""Definición de las clases"""

class Persona:
    nombre = None
    perros = list()
    fecha_nacimineto = None
    ciudad = None
    sexo = None
    descripcion = None
    coche = None

    def __init__(self, nombre = None, sexo = None, fecha_nacimiento = None, ciudad = None):
        self.nombre = nombre
        self.fecha_nacimineto = fecha_nacimiento
        self.ciudad = ciudad
        self.ciudad.ciudadanos.append(self)

    def get_ciudad(self):
        return self.ciudad

    def get_nombre(self):
        return self.nombre
    
    def get_perros(self):
        return self.perros
    
    def get_fecha_nacimiento(self):
        return self.fecha_nacimineto
    
    def sexo(self):
        self.sexo
    
    def set_descripcion(self, descripcion = 'Soy un hombre especial, salúdame y te cuento'):
        self.descripcion = descripcion

    def get_descripcion(self):
        return self.descripcion

    def set_coche(self, coche = None):
        self.coche = coche

    def set_coche(self):
        return self.coche


class Perro:
    nombre = None
    dueno = None
    fecha_nacimiento = None
    ciudad = None
    raza = None

    def __init__(self, nombre = None, dueno = None, fecha_nacimiento = None, ciudad = None, raza = None):
        self.nombre = nombre
        self.dueno = dueno
        self.fecha_nacimiento = fecha_nacimiento
        self.ciudad = ciudad
        self.raza = raza

        self.dueno.perros.append(self)
        self.ciudad.perros.append(self)

class Ciudad:
    ciudad = None
    codigo_postal = None
    pais = None
    ciudadanos = list()
    perros = list()

    def __init__(self, ciudad = None, codigo_postal = None, pais = None):
        self.ciudadanos.clear()

        self.ciudad = ciudad
        self.codigo_postal = codigo_postal
        self.pais = pais

    def get_ciudad(self):
        return self.ciudad

    def get_pais(self):
        return self.pais

    def get_ciudadanos(self):
        return self.ciudadanos


class Coche:
    marca = None
    modelo = None
    dueno = None
    ano_matricula = None
    descripcion = None
    
    def __init__(self, marca = None, modelo = None, ano_matricula = None):
        self.marca = marca
        self.modelo = modelo
        self.ano_matricula = ano_matricula

    def set_descripcion(self, descripcion = None):
        self.descripcion = descripcion


if __name__ == '__main__':

    """Utilizar las clases"""
    # Creación de las ciudades
    palma = Ciudad(ciudad = 'Palma de Mallorca', codigo_postal = '07001', pais = 'España')
    crevillente = Ciudad(ciudad = 'Crevillente', codigo_postal = '03330', pais = 'España')
    madrid = Ciudad(ciudad = 'Madrid', codigo_postal = '28001', pais = 'España')

    # Creación de las personas
    fran = Persona(nombre = 'Fran', sexo = 'Hombre', fecha_nacimiento = '1990-04-04', ciudad = palma)
    maria = Persona(nombre = 'Maria', sexo = 'Mujer', fecha_nacimiento = '1993-01-01', ciudad = crevillente)
    alex = Persona(nombre = 'Alex', sexo = 'Hombre', fecha_nacimiento = '2000-02-29', ciudad = madrid)

    alex.set_descripcion(descripcion = 'Soy un hombre especial, salúdame y te cuento')

    # Creación de los perros
    anaconda = Perro(nombre = 'Anaconda', dueno = fran, fecha_nacimiento = '2018-07-01', ciudad = fran.get_ciudad(), raza = 'Pitbull')
    sam = Perro(nombre = 'Sam', dueno = maria, fecha_nacimiento = '2015-05-01', ciudad = maria.get_ciudad(), raza = 'Chucho')
    roy = Perro(nombre = 'Roy', dueno = fran, fecha_nacimiento = '2016-06-05', ciudad = maria.get_ciudad(), raza = 'Chucho')

    # Creación de los coches
    audi_a1 = Coche(marca = 'Audi', modelo = 'A1', ano_matricula = 2017)
    range_rover = Coche(marca = 'Range Rover', modelo = 'Evoque', ano_matricula = 2017)

    audi_a1.set_descripcion(descripcion = 'Este coche está "Too guapo"')
    range_rover.set_descripcion(descripcion = 'Este coche está "Too chulo"')

    # Asignar los coches a Fran y Maria
    fran.set_coche(coche = audi_a1)
    maria.set_coche(coche = range_rover)

    ### Responder a las preguntas ###
    #1. ¿Qué coche tiene Fran?
    msg_fran = f'{fran.get_nombre()} tiene un {fran.get_coche().marca} - {fran.get_coche().modelo} y la descripción es: {fran.get_coche().descripcion}'

    #2. ¿Qué coche tiene Maria?
    msg_maria = f'{maria.get_nombre()} tiene un {maria.get_coche().marca} - {maria.get_coche().modelo} y la descripción es: {maria.get_coche().descripcion}'

    #3. ¿Qué perros son de Maria?
    print("\nLos perros de Maria son")
    for perro in maria.perros:
        if perro.dueno == maria:
            print(perro.nombre)

    #4. ¿Qué perros son de Fran?
    print("\nLos perros de Fran son")
    for perro in fran.perros:
        if perro.dueno == fran:
            print(perro.nombre)

    #5. ¿Que perros viven en Crevillente?
    print("\nMostrar los perros que viven en Crevillente")
    for perros in crevillente.perros:
        if perro.ciudad == crevillente:
            print(perro.nombre)
