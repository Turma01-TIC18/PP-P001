from abc import ABC, abstractmethod
from statistics import median
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

    def mostraMediana(self):
        sorted_lista = sorted(self.__lista)
        meio = len(sorted_lista) // 2

        if len(sorted_lista) % 2 == 0:
            # Quantidade par de elementos
            if self.__tipoDeDados in (Data, str):
                # Para Data ou String, escolhe o primeiro
                print(f"Mediana: {sorted_lista[meio - 1]}")
            else:
                # Para float ou int, calcula a média
                mediana = median(sorted_lista[meio - 1:meio + 1])
                print(f"Mediana: {mediana}")
        else:
            # Quantidade ímpar de elementos
            print(f"Mediana: {sorted_lista[meio]}")

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
        for _ in range(num_elementos):
            nome = input("Digite um nome: ")
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

class ListaDatas(AnaliseDados):
    def __init__(self):
        super().__init__(Data)

    def entradaDeDados(self):
        num_elementos = int(input("Quantas datas você deseja inserir? "))
        for _ in range(num_elementos):
             while True:
                try:
                    dia = int(input("Dia: "))
                    mes = int(input("Mês: "))
                    ano = int(input("Ano: "))
                    data = Data(dia, mes, ano)
                    self._AnaliseDados__lista.append(data)
                    break  
                except ValueError as e:
                    print(f"Erro: {e}. Por favor, insira uma data válida.")

    def mostraMenor(self):
        print(f"Menor: {min(self._AnaliseDados__lista)}")

    def mostraMaior(self):
        print(f"Maior: {max(self._AnaliseDados__lista)}")

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
        for _ in range(num_elementos):
            salario = float(input("Digite um salário: "))
            self._AnaliseDados__lista.append(salario)

    def mostraMenor(self):
        print(f"Menor: {min(self._AnaliseDados__lista)}")

    def mostraMaior(self):
        print(f"Maior: {max(self._AnaliseDados__lista)}")

    def listarEmOrdem(self):
        sorted_lista = sorted(self._AnaliseDados__lista)
        print("Lista em ordem:", sorted_lista)
    def getLista(self):
        return self._AnaliseDados__lista
    
    def reajustarSalarios(self, percentual):
        self._AnaliseDados__lista = list(map(lambda salario: salario * (1 + percentual / 100), self._AnaliseDados__lista))

    def calcularCustoFolha(self):
        return sum(self._AnaliseDados__lista)

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
        sorted_lista = sorted(self._AnaliseDados__lista)
        print("Lista em ordem:", sorted_lista)
    def getLista(self):
        return self._AnaliseDados__lista

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas = [nomes, datas, salarios, idades]

    for lista in listaListas:
        lista.entradaDeDados()
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
            pass
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
            salarios.reajustarSalarios(10)
    
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