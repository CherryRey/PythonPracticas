class Alumno:
    student = str(input("nombre del alumno: "))
    nota = float(input("nota: "))

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def __str__(self):
        return f"El alumno {self.nombre} ha sacado una nota de {self.nota}"
        

    def aprobado(self): 
        if self.nota >= 5:
            print (f"{self.nombre} ha aprobado")
        else:
            print (f"{self.nombre} no ha aprobado")


alumno1 = Alumno(Alumno.student, Alumno.nota)
print(alumno1)
alumno1.aprobado()

