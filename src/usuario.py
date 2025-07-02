class Usuario:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso

    # (paso inicial)
    # def actualizar_peso(self, nuevo_peso):
        # ERROR: En lugar de asignar nuevo_peso, resta 1 kg
       # self.peso -= 1

    #correción código, para asignar el nuevo peso
    def actualizar_peso(self, nuevo_peso):
        self.peso = nuevo_peso

    def mostrar_informacion(self):
        print(f"Usuario: {self.nombre}, Peso Actual: {self.peso} kg")