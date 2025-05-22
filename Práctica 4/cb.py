from abc import ABC, abstractmethod
from datetime import date, datetime

class CuentaBancaria(ABC):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0):
        self._nombre_titular = nombre_titular       # atributo privado
        self._dni_titular = dni_titular             # atributo privado
        self._fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y/%m/%d').date()
        self._saldo = saldo                         # atributo privado

    def obtener_saldo(self):
        return self._saldo

    @abstractmethod
    def depositar(self, monto):
        pass

    @abstractmethod
    def extraer(self, monto):
        pass

    def _caclular_edad(self):
        fecha_actual = date.today()
        edad = fecha_actual - self._fecha_nacimiento
        return edad.days // 365

    def obtener_edad(self):
        return self._caclular_edad()