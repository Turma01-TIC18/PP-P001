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


class AnaliseDados(ABC):
    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados
        self.__lista = []

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def listarEmOrdem():
        pass

    def mostraMediana(self):
        sorted_lista = sorted(self.__lista)
        meio = len(sorted_lista) // 2

        if len(sorted_lista) % 2 == 0:
            
            if self.__tipoDeDados in (Data, str):
                
                print(f"Mediana: {sorted_lista[meio - 1]}")
            else:
                
                mediana = median(sorted_lista[meio - 1:meio + 1])
                print(f"Mediana: {mediana}")
        else:
            
            print(f"Mediana: {sorted_lista[meio]}")

    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass

class ListaNomes(AnaliseDados):
    def __init__(self, listaSalarios, tipoDeDado=str):
        super().__init__(tipoDeDado)
        self.listaSalarios = listaSalarios

    def entradaDeDados(self):
        num_elementos = int(input("Quantos nomes você deseja inserir? "))
        for _ in range(num_elementos):
            nome = input("Digite um nome: ")
            self._AnaliseDados__lista.append(nome)
    

    def mostraMenor(self):
        print(f"Menor: {min(self._AnaliseDados__lista)}")

    def mostraMaior(self):
        print(f"Maior: {max(self._AnaliseDados__lista)}")
    
    def listarEmOrdem(self):
        print("_____________________________________")
        print("Lista em ordem alfabética")
        for nome in sorted(self._AnaliseDados__lista):
            print(nome)    

    def listarNomesSalarios(self):
        print("Nomes e Salários:")
        for nome, salario in zip(self._AnaliseDados__lista, self.listaSalarios._AnaliseDados__lista):
            print(f"Nome: {nome}, Salário: {salario}")

class ListaDatas(AnaliseDados):
    def __init__(self):
        super().__init__(Data)

    def entradaDeDados(self):
        num_elementos = int(input("Quantas datas você deseja inserir? "))
        for _ in range(num_elementos):
            dia = int(input("Dia: "))
            mes = int(input("Mês: "))
            ano = int(input("Ano: "))
            data = Data(dia, mes, ano)
            self._AnaliseDados__lista.append(data)
    

    def mostraMenor(self):
        print(f"Menor: {min(self._AnaliseDados__lista)}")

    def mostraMaior(self):
        print(f"Maior: {max(self._AnaliseDados__lista)}")    
    
    def listarEmOrdem(self):
        print("_____________________________________")
        print("Lista em ordem cronológica:")
        for data in sorted(self._AnaliseDados__lista):
            print(data)

    def ajustarDatasAnteriores2019(self):
        self._AnaliseDados__lista = list(
            map(
                lambda data: Data(1, data.mes, data.ano) if data.ano < 2019 else data,
                self._AnaliseDados__lista
            )
        )

    def mostrarDatasAjustadas(self):
        print("Datas Ajustadas:")
        for data in self._AnaliseDados__lista:
            print(f"Data: {data}")


class ListaSalarios(AnaliseDados):
    def __init__(self):
        super().__init__(float)

    def entradaDeDados(self):
        num_elementos = int(input("Quantos salários você deseja inserir? "))
        for _ in range(num_elementos):
            salario = float(input("Digite um salário: "))
            self._AnaliseDados__lista.append(salario)

    def mostraMenor(self):
        print(f"Menor: {min(self._AnaliseDados__lista)}")

    def mostraMaior(self):
        print(f"Maior: {max(self._AnaliseDados__lista)}")
    
    def listarEmOrdem(self):
        print("_____________________________________")
        print("Lista em ordem crescente:")
        for salario in sorted(self._AnaliseDados__lista):
            print(salario)

    def reajustarSalarios(self):
        self._AnaliseDados__lista = list(map(lambda salario: salario * 1.1, self._AnaliseDados__lista))

    def mostrarSalariosReajustados(self):
        print("Salários Reajustados:")
        for salario in self._AnaliseDados__lista:
            print(f"Salário: {salario}")

class ListaIdades(AnaliseDados):
    def __init__(self):
        super().__init__(int)

    def entradaDeDados(self):
        num_elementos = int(input("Quantas idades você deseja inserir? "))
        for _ in range(num_elementos):
            idade = int(input("Digite uma idade: "))
            self._AnaliseDados__lista.append(idade)
        
    def mostraMenor(self):
        print(f"Menor: {min(self._AnaliseDados__lista)}")

    def mostraMaior(self):
        print(f"Maior: {max(self._AnaliseDados__lista)}")

    def listarEmOrdem(self):
        print("_____________________________________")
        print("Lista em ordem crescente:")
        for idade in sorted(self._AnaliseDados__lista):
            print(idade)

def main():
    salarios = ListaSalarios()
    nomes = ListaNomes(salarios, tipoDeDado=str)
    datas = ListaDatas()
    idades = ListaIdades()

    

    listaListas = [nomes, datas, salarios, idades]

    for lista in listaListas:
        lista.entradaDeDados()
        lista.mostraMediana()
        lista.mostraMenor()
        lista.mostraMaior()
        lista.listarEmOrdem()
        print("___________________")
        
    nomes.listarNomesSalarios();
    print("___________________")
    datas.ajustarDatasAnteriores2019();
    datas.mostrarDatasAjustadas();
    print("___________________")
    salarios.reajustarSalarios();
    salarios.mostrarSalariosReajustados();



    print("Fim do teste!!!")


if __name__ == "__main__":
    main()