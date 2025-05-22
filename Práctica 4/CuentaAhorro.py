from cb import CuentaBancaria

class CuentaAhorro(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0, tasa_interes=0.001):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._tasa_interes = tasa_interes

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Se ha depositado {monto} a la cuenta de ahorro de {self._nombre_titular}, su saldo es de: {self.obtener_saldo()}")
        else:
            print("El monto a depositar debe ser mayor a 0")

    def extraer(self, monto):
        if monto <= self.obtener_saldo():
            self._saldo -= monto
            print(f"Se ha extraído {monto} de la cuenta de ahorro de {self._nombre_titular}, su saldo actual es de: {self.obtener_saldo()}")
        else:
            print("No posee saldo suficiente para esta operación")

    def calcular_interes(self):
        interes = self._saldo * self._tasa_interes
        print(f"El interés generado sobre el saldo actual es: {interes}")
        return interes
