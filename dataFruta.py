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

    @property
    def mes(self):
        return self.__mes

    @property
    def ano(self):
        return self.__ano

    def __str__(self):
        return f"{self.__dia}/{self.__mes}/{self.__ano}"

    def __eq__(self, outraData):
        return (
            self.__dia == outraData.__dia
            and self.__mes == outraData.__mes
            and self.__ano == outraData.__ano
        )

    def __lt__(self, outraData):
        return (self.__ano, self.__mes, self.__dia) < (outraData.__ano, outraData.__mes, outraData.__dia)

    def __gt__(self, outraData):
        return (self.__ano, self.__mes, self.__dia) > (outraData.__ano, outraData.__mes, outraData.__dia)


class AnaliseDados(ABC):
    @abstractmethod
    def __init__(self, tipo_de_dados):
        self.__tipo_de_dados = tipo_de_dados
        self.__lista = []

    @abstractmethod
    def entrada_de_dados(self):
        pass

    @abstractmethod
    def listar_em_ordem(self):
        pass

    def mostra_mediana(self):
        sorted_lista = sorted(self.__lista)
        meio = len(sorted_lista) // 2

        if len(sorted_lista) % 2 == 0:
            mediana = median(sorted_lista[meio - 1:meio + 1]) if self.__tipo_de_dados not in (Data, str) else sorted_lista[meio - 1]
            print(f"Mediana: {mediana}")
        else:
            print(f"Mediana: {sorted_lista[meio]}")

    @abstractmethod
    def mostra_menor(self):
        pass

    @abstractmethod
    def mostra_maior(self):
        pass


class ListaNomes(AnaliseDados):
    def __init__(self, lista_salarios, tipo_de_dado=str):
        super().__init__(tipo_de_dado)
        self.lista_salarios = lista_salarios

    def entrada_de_dados(self):
        nome = input("Digite um nome: ")
        self._AnaliseDados__lista.append(nome)

    def mostra_menor(self):
        print(f"Menor: {min(self._AnaliseDados__lista)}")

    def mostra_maior(self):
        print(f"Maior: {max(self._AnaliseDados__lista)}")

    def listar_em_ordem(self):
        print("_____________________________________")
        print("Lista em ordem alfabética")
        for nome in sorted(self._AnaliseDados__lista):
            print(nome)

    def listar_nomes_salarios(self):
        print("Nomes e Salários:")
        for nome, salario in zip(self._AnaliseDados__lista, self.lista_salarios._AnaliseDados__lista):
            print(f"Nome: {nome}, Salário: {salario}")


class ListaDatas(AnaliseDados):
    def __init__(self):
        super().__init__(Data)

    def entrada_de_dados(self):
        dia = int(input("Dia: "))
        mes = int(input("Mês: "))
        ano = int(input("Ano: "))
        data = Data(dia, mes, ano)
        self._AnaliseDados__lista.append(data)

    def mostra_menor(self):
        print(f"Menor: {min(self._AnaliseDados__lista)}")

    def mostra_maior(self):
        print(f"Maior: {max(self._AnaliseDados__lista)}")

    def listar_em_ordem(self):
        print("_____________________________________")
        print("Lista em ordem cronológica:")
        for data in sorted(self._AnaliseDados__lista):
            print(data)

    def ajustar_datas_anteriores_2019(self):
        self._AnaliseDados__lista = [Data(1, data.mes, data.ano) if data.ano < 2019 else data for data in self._AnaliseDados__lista]

    def mostrar_datas_ajustadas(self):
        print("Datas Ajustadas:")
        for data in self._AnaliseDados__lista:
            print(f"Data: {data}")


class ListaSalarios(AnaliseDados):
    def __init__(self):
        super().__init__(float)

    def entrada_de_dados(self):
        salario = float(input("Digite um salário: "))
        self._AnaliseDados__lista.append(salario)

    def mostra_menor(self):
        print(f"Menor: {min(self._AnaliseDados__lista)}")

    def mostra_maior(self):
        print(f"Maior: {max(self._AnaliseDados__lista)}")

    def listar_em_ordem(self):
        print("_____________________________________")
        print("Lista em ordem crescente:")
        for salario in sorted(self._AnaliseDados__lista):
            print(salario)

    def reajustar_salarios(self):
        self._AnaliseDados__lista = [salario * 1.1 for salario in self._AnaliseDados__lista]

    def mostrar_salarios_reajustados(self):
        print("Salários Reajustados:")
        for salario in self._AnaliseDados__lista:
            print(f"Salário: {salario}")


class ListaIdades(AnaliseDados):
    def __init__(self):
        super().__init__(int)

    def entrada_de_dados(self):
        idade = int(input("Digite uma idade: "))
        self._AnaliseDados__lista.append(idade)

    def mostra_menor(self):
        print(f"Menor: {min(self._AnaliseDados__lista)}")

    def mostra_maior(self):
        print(f"Maior: {max(self._AnaliseDados__lista)}")

    def listar_em_ordem(self):
        print("_____________________________________")
        print("Lista em ordem crescente:")
        for idade in sorted(self._AnaliseDados__lista):
            print(idade)


def menu():
    print("\n\n")
    print("DATAFRUTA")
    print("\nMenu de Opções:")
    print("\n1. Incluir um nome na lista de nomes")
    print("2. Incluir um salário na lista de salários")
    print("3. Incluir uma data na lista de datas")
    print("4. Incluir uma idade na lista de idades")
    print("5. Percorrer as listas de nomes e salários")
    print("6. Calcular o valor da folha com um reajuste de 10%")
    print("7. Modificar o dia das datas anteriores a 2019")
    print("8. Sair")


def main():
    salarios = ListaSalarios()
    nomes = ListaNomes(salarios, tipo_de_dado=str)
    datas = ListaDatas()
    idades = ListaIdades()

    while True:
        menu()
        opcao = int(input("\nEscolha uma opção (1-8): "))

        if opcao == 1:
            nomes.entrada_de_dados()
        elif opcao == 2:
            salarios.entrada_de_dados()
        elif opcao == 3:
            datas.entrada_de_dados()
        elif opcao == 4:
            idades.entrada_de_dados()
        elif opcao == 5:
            nomes.listar_nomes_salarios()
        elif opcao == 6:
            salarios.reajustar_salarios()
            salarios.mostrar_salarios_reajustados()
        elif opcao == 7:
            datas.ajustar_datas_anteriores_2019()
            datas.mostrar_datas_ajustadas()
        elif opcao == 8:
            print("Saindo do programa.\n")
            break
        else:
            print("Opção inválida. Escolha um número de 1 a 8.")


if __name__ == "__main__":
    main()