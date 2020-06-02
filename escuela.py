# Una escuela tiene alumnos, cuyas características son:
# *Nombre
# *Apellido
# *Nota Matematica
# *Nota Lengua
# *Nota geografía
# *Promedio
# Los alumnos pueden dar exámenes.

# La escuela también tiene profesores que tienen las siguientes características:
# *Nombre
# *Apellido
# *Materia que enseña
# -Los profesores toman exámenes y le dan al alumno una nota.
# Se deben cargar distintos alumnos y profesores, que los alumnos den exámenes que toman los profesores y que el resultado
# sea una nota. El alumno siempre debe tener un promedio (al principio las tres notas son 0).

class Persona():
    def __init__(self, nombre, apellido):
        self.apellido = apellido
        self.nombre = nombre


class Alumno(Persona):
    def __init__(self, nombre, apellido):
        Persona.__init__(self,nombre,apellido)
        self.nota_geo = 0
        self.nota_lengua = 0
        self.nota_mate = 0

    def promedio(self):
        return (self.nota_lengua + self.nota_geo + self.nota_mate) / 3


class Profesor(Persona):
    def __init__(self, nombre, apellido, materia):
        Persona.__init__(self, nombre, apellido)
        self.materia = materia


    def tomar_examen(self, alumno):
        nota = int(input('Ingrese una nota: '))
        if self.materia == 'Matematica':
            alumno.nota_mate = nota
        elif self.materia == 'Geografia':
            alumno.nota_geo = nota
        else:
            alumno.nota_lengua = nota


nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')

alumno = Alumno(nombre, apellido)

profesor1 = Profesor('Carlitos', 'Mou', 'Matematica')
profesor2 = Profesor('Victor', 'Sueiro', 'Lengua')
profesor3 = Profesor('Geronimo', 'Benegas', 'Geografia')

profesor1.tomar_examen(alumno)
profesor2.tomar_examen(alumno)
profesor3.tomar_examen(alumno)

print(alumno.nota_geo)
print(alumno.nota_mate)
print(alumno.nota_lengua)
print(alumno.promedio())
