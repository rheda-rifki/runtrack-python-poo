class Operation:
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        result = self.nombre1 + self.nombre2
        print(f"Résultat de l'addition : {result}")

# Instancier la classe
operation_instance = Operation()

# Appeler la méthode addition et imprimer le résultat en console
operation_instance.addition()
