from abc import ABC, abstractmethod
from datetime import date

class CuentaBancaria(ABC):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0):
        self._nombre_titular = nombre_titular # Atributo privado 
        self._dni_titular = dni_titular # Atributo privado
        self._fecha_nacimiento = fecha_nacimiento # Atributo privado 
        self._saldo = saldo # Atributo privado

    def obtener_saldo(self): 
        return self._saldo

    @abstractmethod
    def depositar(self, monto): 
        pass

    @abstractmethod
    def extraer(self, monto):
        pass

    def obtener_edad(self):
        return self._calcular_edad()

class CuentaAhorro(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self.__tasa_de_interes = 0.001

    def depositar(self, monto): 
        if monto > 0:
            self._saldo += monto
            print(f"Se ha depositado {monto} a la cuenta de {self._nombre_titular}, su saldo actual es de : {self.obtener_saldo()}.")
        else:
            print("El monto a depositar debe ser positivo.")

    def extraer(self, monto):
        if monto <= self._saldo:
            self._saldo -= monto
            print(f"Se ha extraído {monto} de la cuenta de {self._nombre_titular}, su saldo actual es de : {self.obtener_saldo()}.")
        else:
            print("No posee saldo suficiente para realizar la operación.")

    def calcular_interes(self):
        return self._saldo * self.__tasa_de_interes
