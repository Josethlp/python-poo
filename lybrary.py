import datetime


# Definición de la clase persona
class Persona:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni


# Definición de la clase Usuario que hereda de Persona
class Usuario(Persona):
    def __init__(self, nombre, dni, email):
        super().__init__(nombre, dni)
        # Llamada al constructor de la clase padre
        self.email = email
        self.prestamos = []
        # Lista de objetos Préstamo asociados al Usuario
 
    def solicitar_prestamo(self, libro):
        prestamo = Prestamo(self, libro)
        # Creación de un objeto Préstamo
        self.prestamos.append(prestamo)
        # Agregación del préstamo a la lista del Usuario
        libro.disponible = False
        # Modificación del estado del libro

        print(f'El usuario {self.nombre} ha solicitado el prestamo del libro {libro.titulo}')

    def devolver_prestamo(self, prestamo):
        prestamo.libro.disponible = True
        # Modificación del estado del libro
        self.prestamos.remove(prestamo)
        # Eliminación del préstamo de la lista del usuario

        print(f'El usuario {self.nombre} ha devuelto el préstamo del libro {prestamo.libro.titulo}')


# Definicion de la clase libro
class Libro:
    def __init__(self, titulo, autor, editorial):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.disponible = True
        # Atributo que indica si el libro está disponible para préstamo

    def consultar(self):
        print(f'El libro {self.titulo} es de {self.autor} y fue publicado por {self.editorial}')

        if self.disponible:
            print('El libro está disponible para préstamo')
        else:
            print('El libro no está disponible para préstamo')


# Definición de la clase Préstamo que tiene una relación de composición con
# la clase Libro
class Prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        self.fecha_inicio = datetime.date.today()
        # Fecha actual
        self.fecha_fin = self.fecha_inicio + datetime.timedelta(days=15)
        # Fecha actual más 15 días

    def consultar(self):
        print(f'El préstamo del libro {self.libro.titulo} fue solicitado por {self.usuario.nombre} el {self.fecha_inicio} y debe ser devuelto el {self.fecha_fin}')


if __name__ == '__main__':
    # Creación de objetos e invocación de métodos
    
    persona1 = Persona('Juan', '1234567A')
    # Creación de un objeto Persona
    
    usuario1 = Usuario(persona1.nombre, persona1.dni, 'juan@gmail.com')
    # Creación de un objeto Usuario

    libro1 = Libro('El principio', 'Antoine de Saint-Exupéry', 'Salamandra')
    # Creación de un objeto Libro

    libro2 = Libro('Cien años de soledad', 'Gabriel García Márquez', 'Sudamericana')
    # Creación de otro objeto Libro


    libro1.consultar()
    # Invocación del método consultar de la clase Libro

    usuario1.solicitar_prestamo(libro1)
    # Invocación del método solicitar préstamo de la clase Usuario

    prestamo1 = usuario1.prestamos[0]
    # Acceso al primer elemento de la lista de préstamos del usuario

    prestamo1.consultar()
    # Invocación del método consultar de la clase Prestamo

    libro1.consultar()
    # Invocación del método consultar de la clase Libro

    usuario1.devolver_prestamo(prestamo1)
    # Invocación del método devolver_prestamo de la clase Usuario

    libro1.consultar()
    # Invocación del método consultar de la clase Libro