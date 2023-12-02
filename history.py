from typing import List, Optional

class Persona:
    def __init__(self, nombre: Optional[str] = None, sexo: Optional[str] = None,
                 fecha_nacimiento: Optional[str] = None, ciudad: Optional["Ciudad"] = None) -> None:
        """
        Inicializa una nueva instancia de la clase Persona.

        Args:
        - nombre (str): Nombre de la persona.
        - sexo (str): Género de la persona.
        - fecha_nacimiento (str): Fecha de nacimiento de la persona.
        - ciudad (Ciudad): Objeto Ciudad al que pertenece la persona.
        """
        self.nombre: Optional[str] = nombre
        self.sexo: Optional[str] = sexo
        self.fecha_nacimiento: Optional[str] = fecha_nacimiento
        self.ciudad: Optional["Ciudad"] = ciudad

        self.ciudad.ciudadanos.append(self) if self.ciudad else None
        # Agrega a la persona a la lista de ciudadanos de la ciudad.
        self.perros: List["Perro"] = []
        # Lista de perros que posee la persona.
        self.descripcion: Optional[str] = None
        # Descripción personal de la persona.
        self.coche: Optional["Coche"] = None
        # Coche de la persona.

    def set_descripcion(self, descripcion: Optional[str] = 'Soy un hombre especial, salúdame y te cuento') -> None:
        """
        Establece la descripción personal de la persona.

        Args:
        - descripcion (str): Descripción personal de la persona.
        """
        self.descripcion: Optional[str] = descripcion

    def set_coche(self, coche: Optional["Coche"] = None) -> None:
        """
        Asigna un coche a la persona.

        Args:
        - coche (Coche): Objeto Coche asignado a la persona.
        """
        self.coche: Optional["Coche"] = coche

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena de la persona.

        Returns:
        - str: Representación en cadena de la persona.
        """
        return f'{self.nombre} ({self.sexo}) nacido el {self.fecha_nacimiento} en {self.ciudad.ciudad}' if self.nombre and self.sexo and self.fecha_nacimiento and self.ciudad else ""

class Perro:
    def __init__(self, nombre: Optional[str] = None, dueno: Optional["Persona"] = None,
                 fecha_nacimiento: Optional[str] = None, ciudad: Optional["Ciudad"] = None, raza: Optional[str] = None) -> None:
        """
        Inicializa una nueva instancia de la clase Perro

        Args:
        - nombre (str): Nombre del perro.
        - dueno (Persona): Dueno del perro.
        - fecha_nacimiento (str): Fecha de nacimiento del perro.
        - ciudad (Ciudad): Ciudad de residencia del perro.
        - raza (str): Raza del perro.
        """
        self.nombre: Optional[str]  = nombre
        self.dueno: Optional["Persona"] = dueno
        self.fecha_nacimiento: Optional[str]  = fecha_nacimiento
        self.raza: Optional[str]  = raza

        ciudad.perros.append(self) if ciudad else None
        # Agrega al perro a la lista de perros de la ciudad.
        dueno.perros.append(self) if dueno else None
        # Agrega al perro a la lista de perros del dueno.

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena del perro.

        Returns:
        - str: Representación en cadena del perro.
        """
        return f'{self.nombre}, {self.raza}, nacido el {self.fecha_nacimiento}' if self.nombre and self.raza and self.fecha_nacimiento else ""

class Ciudad:
    def __init__(self, ciudad: Optional[str] = None, codigo_postal: Optional[str] = None,
                 pais: Optional[str] = None) -> None:
        """
        Inicializa una nueva instancia de la clase Ciudad.

        Args:
        - ciudad (str): Nombre de la ciudad.
        - codigo_postal (str): Código postal de la ciudad.
        - pais (str): País al que pertenece la ciudad.
        """
        self.ciudad: Optional[str] = ciudad
        self.codigo_postal: Optional[str] = codigo_postal
        self.pais: Optional[str] = pais

        self.ciudadanos: List["Persona"] = []
        # Lista de ciudadanos de la ciudad.
        self.perros: List["Perro"] = []
        # Lista de perros que residen en la ciudad.

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena de la ciudad.

        Returns:
        - str: Representación en cadena de la ciudad.
        """
        return f'{self.ciudad}, {self.codigo_postal}, {self.pais}' if self.ciudad and self.codigo_postal and self.pais else ""

class Coche:
    def __init__(self, marca: Optional[str] = None, modelo: Optional[str] = None,
                 ano_matricula: Optional[int] = None) -> None:
        """
        Inicializa una nueva instancia de la clase Coche.

        Args:
        - marca (str): Marca del coche.
        - modelo (str): Modelo del coche.
        - ano_matricula (int): Año de matriculación del coche.
        """
        self.marca: Optional[str] = marca
        self.modelo: Optional[str] = modelo
        self.ano_matricula: Optional[int] = ano_matricula

        self.descripcion: Optional[str] = None
        # Descripción del coche.

    def set_descripcion(self, descripcion: Optional[str] = None) -> None:
        """
        Establece la descripción del coche.

        Args:
        - descripcion (str): Descripción del coche.
        """
        self.descripcion: Optional[str] = descripcion

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena del coche.

        Returns:
        - str: Representación en cadena del coche.
        """
        return f'{self.marca} - {self.modelo} ({self.ano_matricula}) - {self.descripcion}' if self.marca and self.modelo and self.ano_matricula else ""

if __name__ == '__main__':
    # Creación de instancias de Ciudad
    palma = Ciudad(ciudad='Palma de Mallorca', codigo_postal='07001', pais='España')
    crevillente = Ciudad(ciudad='Crevillente', codigo_postal='03330', pais='España')
    madrid = Ciudad(ciudad='Madrid', codigo_postal='28001', pais='España')

    # Creación de instancias de Persona
    fran = Persona(nombre='Fran', sexo='Hombre', fecha_nacimiento='1990-04-04', ciudad=palma)
    maria = Persona(nombre='Maria', sexo='Mujer', fecha_nacimiento='1993-01-01', ciudad=crevillente)
    alex = Persona(nombre='Alex', sexo='Hombre', fecha_nacimiento='2000-02-29', ciudad=madrid)

    # Configuración de descripciones personales
    alex.set_descripcion(descripcion='Soy un hombre especial, salúdame y te cuento')

    # Creación de instancias de Perro
    anaconda = Perro(nombre='Anaconda', dueno=fran, fecha_nacimiento='2018-07-01', ciudad=palma, raza='Pitbull')
    sam = Perro(nombre='Sam', dueno=maria, fecha_nacimiento='2015-05-01', ciudad=crevillente, raza='Chucho')
    roy = Perro(nombre='Roy', dueno=maria, fecha_nacimiento='2016-06-05', ciudad=crevillente, raza='Chucho')

    # Creación de instancias de Coche
    audi_a1 = Coche(marca='Audi', modelo='A1', ano_matricula=2017)
    range_rover = Coche(marca='Range Rover', modelo='Evoque', ano_matricula=2017)

    # Configuración de descripciones de coches
    audi_a1.set_descripcion(descripcion='Este coche está "Too guapo"')
    range_rover.set_descripcion(descripcion='Este coche está "Too chulo"')

    # Asignación de coches a personas
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

