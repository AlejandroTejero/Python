class Empleado:
    def __init__(self,nombre,salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_salario(self):
        #print(f"Salario de {self.nombre} (Empleado) = {self.salario}")
        return self.salario


class Gerente(Empleado):
    def __init__(self,nombre,salario,bono):
        super().__init__(nombre,salario)
        self.bono = bono

    def calcular_salario(self):
        #print(f"Salario de {self.nombre} (Gerente) = {self.salario + self.bono}")
        return self.salario + self.bono


class Empresa:
    def __init__(self):
        self.asalariados = []

    def anadir_empleado(self,empleado):
        self.asalariados.append(empleado)

    def calcular_masa_salarial(self):
        total = 0
        for empleado in self.asalariados:
            total += empleado.salario
        print(f"El total del salario de la empresa sin contar los bonos es: {total}")

    def calcular_masa_salarial_con_bonos(self):
        total = 0
        for empleado in self.asalariados:
            total += empleado.calcular_salario()
        print(f"El total del salario de la empresa es: {total}")


empresa = Empresa()
empleado1 = Empleado('Juan',50000)
empleado1.calcular_salario()
empleado2 = Empleado('Carlos',55000)
empleado1.calcular_salario()
gerente1 = Gerente('Ana',60000,10000)
gerente1.calcular_salario()
gerente2 = Gerente('Carmen',62000,12000)
gerente1.calcular_salario()

empresa.anadir_empleado(empleado1)
empresa.anadir_empleado(gerente1)
empresa.anadir_empleado(empleado2)
empresa.anadir_empleado(gerente2)


empresa.calcular_masa_salarial()
empresa.calcular_masa_salarial_con_bonos()

