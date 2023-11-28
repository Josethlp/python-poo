class Persona:
    def __init__(self, nombre=None, sexo=None, fecha_nacimiento=None, ciudad=None):
        self.nombre = nombre
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento
        self.ciudad = ciudad
        self.ciudad.ciudadanos.append(self)
        self.perros = []
        self.descripcion = None
        self.coche = None

    def set_descripcion(self, descripcion='Soy un hombre especial, salúdame y te cuento'):
        self.descripcion = descripcion

    def set_coche(self, coche=None):
        self.coche = coche

    def __str__(self):
        return f'{self.nombre} ({self.sexo}) nacido el {self.fecha_nacimiento} en {self.ciudad.ciudad}'

class Perro:
    def __init__(self, nombre=None, dueno=None, fecha_nacimiento=None, ciudad=None, raza=None):
        self.nombre = nombre
        self.dueno = dueno
        self.fecha_nacimiento = fecha_nacimiento
        self.raza = raza
        ciudad.perros.append(self)
        dueno.perros.append(self)

    def __str__(self):
        return f'{self.nombre}, {self.raza}, nacido el {self.fecha_nacimiento}'

class Ciudad:
    def __init__(self, ciudad=None, codigo_postal=None, pais=None):
        self.ciudad = ciudad
        self.codigo_postal = codigo_postal
        self.pais = pais
        self.ciudadanos = []
        self.perros = []

    def __str__(self):
        return f'{self.ciudad}, {self.codigo_postal}, {self.pais}'

class Coche:
    def __init__(self, marca=None, modelo=None, ano_matricula=None):
        self.marca = marca
        self.modelo = modelo
        self.ano_matricula = ano_matricula
        self.descripcion = None

    def set_descripcion(self, descripcion=None):
        self.descripcion = descripcion

    def __str__(self):
        return f'{self.marca} - {self.modelo} ({self.ano_matricula}) - {self.descripcion}'

if __name__ == '__main__':
    palma = Ciudad(ciudad='Palma de Mallorca', codigo_postal='07001', pais='España')
    crevillente = Ciudad(ciudad='Crevillente', codigo_postal='03330', pais='España')
    madrid = Ciudad(ciudad='Madrid', codigo_postal='28001', pais='España')

    fran = Persona(nombre='Fran', sexo='Hombre', fecha_nacimiento='1990-04-04', ciudad=palma)
    maria = Persona(nombre='Maria', sexo='Mujer', fecha_nacimiento='1993-01-01', ciudad=crevillente)
    alex = Persona(nombre='Alex', sexo='Hombre', fecha_nacimiento='2000-02-29', ciudad=madrid)

    alex.set_descripcion(descripcion='Soy un hombre especial, salúdame y te cuento')

    anaconda = Perro(nombre='Anaconda', dueno=fran, fecha_nacimiento='2018-07-01', ciudad=palma, raza='Pitbull')
    sam = Perro(nombre='Sam', dueno=maria, fecha_nacimiento='2015-05-01', ciudad=crevillente, raza='Chucho')
    roy = Perro(nombre='Roy', dueno=maria, fecha_nacimiento='2016-06-05', ciudad=crevillente, raza='Chucho')

    audi_a1 = Coche(marca='Audi', modelo='A1', ano_matricula=2017)
    range_rover = Coche(marca='Range Rover', modelo='Evoque', ano_matricula=2017)

    audi_a1.set_descripcion(descripcion='Este coche está "Too guapo"')
    range_rover.set_descripcion(descripcion='Este coche está "Too chulo"')

    fran.set_coche(coche=audi_a1)
    maria.set_coche(coche=range_rover)

    # Respuestas a las preguntas
    print(f'1. ¿Qué coche tiene Fran? \n{fran.nombre} tiene un {fran.coche}')

    print(f'\n2. ¿Qué coche tiene Maria? \n{maria.nombre} tiene un {maria.coche}')

    print('\n3. ¿Qué perros son de Maria?')
    for perro in maria.perros:
        print(perro)

    print('\n4. ¿Qué perros son de Fran?')
    for perro in fran.perros:
        print(perro)

    print('\n5. ¿Que perros viven en Crevillente?')
    for perro in crevillente.perros:
        print(perro)

