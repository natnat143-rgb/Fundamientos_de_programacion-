class Alumno:
     #Agregar
    def __init__(self, nombre: str, numero_control: str, carrera=None, correo_electronico: str = None, guardar: bool = False):
        self.nombre = nombre #El atributo es "nombre" y es Str(varchar)
        self.numero_control = numero_control #El atributo Num. Control es Str(Varchar)
        self.carrera = carrera #Carrera es un objeto porque es donde el alumno esta asignado/se inscribio
        self.guardar = guardar #Nuevo atributo Bool(booleano)
        self.calificaciones = {} #Califcaciones es un diccionario

    def asignar_carrera(self, carrera):
        self.carrera = carrera

    def consulta_calificacion(self, nombre_materia: str):
        if nombre_materia in self.calificaciones:
            return self.calificaciones[nombre_materia]
        else:
            return f'No hay calificación registrada para "{nombre_materia}".'

    def __repr__(self):
        return f'Alumno("{self.nombre}", "{self.numero_control}", guardar={self.guardar})'


class Universidad:
    def __init__(self, nombre: str):
        self.nombre = nombre #El atributo nombre es Str(Varchar)
        self.carreras = [] #Aqui, carrera es una lista
        self.alumnos = [] #Al igual que alumnos. (List)
        self.profesores = [] #Y profesores. (List)

    # ------------------- Gestión de carreras -------------------
    def agregar_carrera(self, carrera):
        self.carreras.append(carrera)

    def obtener_carrera(self, nombre_carrera: str):
        for c in self.carreras:
            if c.nombre == nombre_carrera:
                return c
        return None

    # ------------------- Otros registros -------------------
    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)


class Carrera:
    def __init__(self, nombre: str):
        self.nombre = nombre #El atributo nombre es Str(Varchar)
        self.materias = [] #Lista de objetos Materia

    def agregar_materia(self, materia):
        self.materias.append(materia)

    def obtener_materia(self, nombre_materia: str):
        for m in self.materias:
            if m.nombre == nombre_materia:
                return m
        return None

    def __repr__(self):
        return f'Carrera("{self.nombre}")'


class Materia:
    def __init__(self, nombre: str, carrera: Carrera, calificacion_final: float = None):
        self.nombre = nombre #El atributo nombre es Str(Varchar)
        self.carrera = carrera #Carrera es un objeto               # Instancia de Carrera
        self.calificacion_final = calificacion_final #El atributo de calificacion_final es float (Por las calif. en decimal)

    def __repr__(self):
        return f'Materia("{self.nombre}", carrera="{self.carrera.nombre}")'


class Profesor:
    def __init__(self, nombre: str, materia: Materia):
        self.nombre = nombre #El atributo nombre es Str(Varchar)
        self.materia = materia #Aqui, materia es un objeto porque el profe la imparte.  # Materia que imparte

    def registra_calificacion(self, alumno: Alumno, calificacion: float):
        alumno.calificaciones[self.materia.nombre] = calificacion
        print(f'Calificación registrada: {alumno.nombre} -> '
              f'{self.materia.nombre}: {calificacion}')

    def __repr__(self):
        return f'Profesor("{self.nombre}", {self.materia})'


if __name__ == "__main__":

    uni = Universidad("Instituto")

    ing = Carrera("Ingeniería")
    lic = Carrera("Licenciatura en Ciencias Sociales")

    uni.agregar_carrera(ing)
    uni.agregar_carrera(lic)

    calc = Materia("Cálculo I", ing)
    fis = Materia("Física I", ing)
    sociologia = Materia("Introducción a la Sociología", lic)

    ing.agregar_materia(calc)
    ing.agregar_materia(fis)
    lic.agregar_materia(sociologia)

    juan = Alumno("Juan Pérez", "2023001", guardar=True)
    luisa = Alumno("Luisa Gómez", "2023002", guardar=False)

    juan.asignar_carrera(ing)
    luisa.asignar_carrera(ing)

    uni.agregar_alumno(juan)
    uni.agregar_alumno(luisa)

    prof_garcia = Profesor("Dr. García", calc)
    prof_rodriguez = Profesor("Mtra. Rodríguez", fis)

    uni.agregar_profesor(prof_garcia)
    uni.agregar_profesor(prof_rodriguez)

    prof_garcia.registra_calificacion(juan, 8.5)
    prof_garcia.registra_calificacion(luisa, 9.0)
    prof_rodriguez.registra_calificacion(juan, 7.5)

    print(juan.consulta_calificacion("Cálculo I"))
    print(juan.consulta_calificacion("Física I"))
    print(luisa.consulta_calificacion("Cálculo I"))
    print(luisa.consulta_calificacion("Física I"))

    print("Materias de Ingeniería:", [m.nombre for m in ing.materias])