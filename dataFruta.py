from abc import ABC, abstractmethod
from statistics import median
from datetime import datetime
class Data: 
    def __init__(self, dia = 1, mes = 1, ano = 2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
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
    def mostraMediana(self):
        pass

    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass
    @abstractmethod
    def listarEmOrdem(self):
        pass
    @abstractmethod
    def getLista(self):
        pass

class ListaNomes(AnaliseDados):
    def __init__(self):
        super().__init__(str)

    def entradaDeDados(self):
        num_elementos = int(input("Quantos nomes você deseja inserir? "))
        for i in range(num_elementos):
            nome = input(f"Digite o elemento {i + 1} da lista de nomes: ")
            self._AnaliseDados__lista.append(nome)

    def mostraMenor(self):
        print(f"Menor: {min(self._AnaliseDados__lista)}")

    def mostraMaior(self):
        print(f"Maior: {max(self._AnaliseDados__lista)}")
    
    def listarEmOrdem(self):
        sorted_lista = sorted(self._AnaliseDados__lista)
        print("Lista em ordem:", sorted_lista)
        
    def getLista(self):
        return self._AnaliseDados__lista
    
    def mostraMediana(self):
        self._AnaliseDados__lista.sort()

        if len(self._AnaliseDados__lista) % 2 == 0:
            print("Mediana:", self._AnaliseDados__lista[len(self._AnaliseDados__lista) // 2 - 1])
        else:
            print("Mediana:", self._AnaliseDados__lista[len(self._AnaliseDados__lista) // 2])   

class ListaDatas(AnaliseDados):
    def __init__(self):
        super().__init__(Data)

    def entradaDeDados(self):
        num_elementos = int(input("Quantas datas você deseja inserir? "))
        
        for i in range(num_elementos):
             while True:
                data_buffer = input(f"Digite o elemento {i + 1} da lista de datas no formato dd/mm/aaaa: ")
                try:
                    data = datetime.strptime(data_buffer, "%d/%m/%Y").date()
                    self._AnaliseDados__lista.append(data)
                    break
                except ValueError:
                    print(f"Formato de data inválido: {data_buffer}")
    def mostraMenor(self):
        print(f"Menor: {min(self._AnaliseDados__lista)}")

    def mostraMaior(self):
        print(f"Maior: {max(self._AnaliseDados__lista)}")

    def mostraMediana(self):
        self._AnaliseDados__lista.sort()

        if len(self._AnaliseDados__lista) % 2 == 0:
            print("Mediana:", self._AnaliseDados__lista[len(self._AnaliseDados__lista) // 2 - 1])
        else:
            print("Mediana:", self._AnaliseDados__lista[len(self._AnaliseDados__lista) // 2]) 
    def listarEmOrdem(self):
        sorted_lista = sorted(self._AnaliseDados__lista)
        print("Lista em ordem: ")
        for data in sorted_lista:
            print(data)
    def getLista(self):
        return self._AnaliseDados__lista
    def modificarDatasAnteriores2019(self):
        self._AnaliseDados__lista = list(map(lambda data: Data(1, data.mes, data.ano) if data.ano < 2019 else data, self._AnaliseDados__lista))

class ListaSalarios(AnaliseDados):
    def __init__(self):
        super().__init__(float)

    def entradaDeDados(self):
        num_elementos = int(input("Quantos salários você deseja inserir? "))
        for i in range(num_elementos):
            while True:
                try:
                    salario = float(input(f"Digite o elemento {i + 1} da lista de salários: "))
                    self._AnaliseDados__lista.append(salario)
                    break
                except ValueError:
                    print("Erro: Por favor, insira um valor numérico válido.")

    def mostraMediana(self):
        self._AnaliseDados__lista.sort()

        if len(self._AnaliseDados__lista) % 2 == 0:
            valor1 = self._AnaliseDados__lista[len(self._AnaliseDados__lista) // 2 - 1]
            valor2 = self._AnaliseDados__lista[len(self._AnaliseDados__lista) // 2]
            print("Mediana:", (valor1 + valor2) / 2.0)
        else:
            print("Mediana:", self._AnaliseDados__lista[len(self._AnaliseDados__lista) // 2]) 

    def mostraMenor(self):
        print(f"Menor: {min(self._AnaliseDados__lista)}")

    def mostraMaior(self):
        print(f"Maior: {max(self._AnaliseDados__lista)}")

    def listarEmOrdem(self):
        sorted_lista = sorted(self._AnaliseDados__lista)
        print("Lista em ordem:", sorted_lista)
    def getLista(self):
        return self._AnaliseDados__lista
    
    def reajustarSalarios(self):
        if not self._AnaliseDados__lista:
            print("Lista de salarios vazia")
            return

        self._AnaliseDados__lista  = map(lambda salario: salario * 1.10, self._AnaliseDados__lista)


    def calcularCustoFolha(self):
        return sum(self._AnaliseDados__lista)

class ListaIdades(AnaliseDados):
    def __init__(self):
        super().__init__(int)

    def entradaDeDados(self):
        num_elementos = int(input("Quantas idades você deseja inserir? "))
        for i in range(num_elementos):
            idade = input(f"Digite o elemento {i + 1} da lista de idades: ")
            self._AnaliseDados__lista.append(idade)

    def mostraMenor(self):
        print(f"Menor: {min(self._AnaliseDados__lista)}")

    def mostraMaior(self):
        print(f"Maior: {max(self._AnaliseDados__lista)}")

    def listarEmOrdem(self):
        sorted_lista = sorted(self._AnaliseDados__lista)
        print("Lista em ordem:", sorted_lista)
    def getLista(self):
        return self._AnaliseDados__lista
    def mostraMediana(self):
        if not self._AnaliseDados__lista:
            print("A lista está vazia.")
            return
        self._AnaliseDados__lista.sort()

        if len(self._AnaliseDados__lista) % 2 == 0:
            print("Mediana:", self._AnaliseDados__lista[len(self._AnaliseDados__lista) // 2 - 1])
        else:
            print("Mediana:", self._AnaliseDados__lista[len(self._AnaliseDados__lista) // 2])   

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas = [nomes, datas, salarios, idades]

    for lista in listaListas:
        lista.entradaDeDados()
        
        if not lista.getLista():
            print("Lista Vazia")
        else:
            lista.mostraMediana()
            lista.mostraMenor()
            lista.mostraMaior()
            lista.listarEmOrdem()
        print("___________________")

    while True:
        print("1. Incluir um nome na lista de nomes")
        print("2. Incluir um salário na lista de salários")
        print("3. Incluir uma data na lista de datas")
        print("4. Incluir uma idade na lista de idades")
        print("5. Percorrer as listas de nomes e salários")
        print("6. Calcular o valor da folha com um reajuste de 10%")
        print("7. Modificar o dia das datas anteriores a 2019")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nomes.entradaDeDados()
        elif opcao == "2":
            pass
        elif opcao == "3":
            pass
        elif opcao == "4":
            pass
        elif opcao == "5":
            nomeSalario = zip(nomes.getLista(), salarios.getLista())
            for nome, salario in nomeSalario:
                print(f"Nome: {nome}, Salário: {salario}")
            print()
        elif opcao == "6":
             # Reajuste de salários em 10%
            salarios.reajustarSalarios()
    
            # Cálculo do custo da folha de pagamento após reajuste
            print(f"Custo da folha de pagamento após reajuste: {salarios.calcularCustoFolha()}")
            
            print()
        elif opcao == "7":
            datas.modificarDatasAnteriores2019()
            print("Datas apos metodo: modificarDatasAnteriores2019()")
            datas.listarEmOrdem()
            
            print()
        elif opcao == "8":
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()