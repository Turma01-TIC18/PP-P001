from abc import ABC, abstractmethod
from statistics import median

class Data:
    def __init__(self, dia=1, mes=1, ano=1900):
        if not (1 <= dia <= 31) or not (1 <= mes <= 12) or not (1900 <= ano <= 2100):
            raise ValueError("Data inválida")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        if not (1 <= dia <= 31):
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        if not (1 <= mes <= 12):
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        if not (1900 <= ano <= 2100):
            raise ValueError("Ano inválido")
        self.__ano = ano

    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return (
            self.__dia == outraData.__dia
            and self.__mes == outraData.__mes
            and self.__ano == outraData.__ano
        )

    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                return self.__dia < outraData.__dia
        return False

    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                return self.__dia > outraData.__dia
        return False