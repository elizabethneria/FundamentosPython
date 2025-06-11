class Alumno:
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def lista(self):
        print(f"{ self.name } Presente!")

alumno1 = Alumno('jose', 20)
print(alumno1.lista())
alumno2 = Alumno('pedro', 20)
print(alumno2.lista())
alumno3 = Alumno('mike', 20)
alumno3.lista()

