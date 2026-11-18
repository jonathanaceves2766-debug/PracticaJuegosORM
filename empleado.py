class Empleado:
    def __init__(self, nombre, apellido, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario

    @property
    def email(self):
        return f"{self.nombre.lower()}.{self.apellido.lower()}@empresa.com"

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def aplicar_aumento(self, porcentaje=0.05):
        if porcentaje < 0:
            raise ValueError("El porcentaje de aumento no puede ser negativo.")
        self.salario = int(self.salario * (1 + porcentaje))
        return self.salario
