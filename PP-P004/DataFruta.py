
from abc import ABC, abstractmethod
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
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return  self.__dia == outraData.__dia and \
                self.__mes == outraData.__mes and \
                self.__ano == outraData.__ano
    
    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False
    
    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False
    

class AnaliseDados(ABC): 

    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

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
        super().__init__(type("String"))
        self.__lista = []        

    def entradaDeDados(self):
        quantidade = int(input("Digite a quantidade de elementos da lista: "))
        for i in range(quantidade):
            nome = input(f"Digite o elemento {i + 1} da lista de strings: ")
            self.__lista.append(nome)

    def mostraMediana(self):
        if not self.__lista:
            print("Sem dados")
            return

        self.__lista.sort()

        if len(self.__lista) % 2 == 0:
            print("Mediana:", self.__lista[len(self.__lista) // 2 - 1])
        else:
            print("Mediana:", self.__lista[len(self.__lista) // 2])   

    def mostraMenor(self):
        if self.__lista:
            smallest_string = min(self.__lista)
            print("Menor string:", smallest_string)
        else:
            print("O vetor de strings está vazio.")

    def mostraMaior(self):
        if self.__lista:
            biggest_string = max(self.__lista)
            print("Maior string:", biggest_string)
        else:
            print("O vetor de strings está vazio.")
    
    def listarEmOrdem(self):
        self.__lista.sort()
        print("Imprimindo elementos em ordem crescente")
        for elemento in self.__lista:
            print(elemento)

    def __str__(self):
        return str(self.__lista)
    
    def getLista(self):
        return self.__lista 
	
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def entradaDeDados(self):
        quantidade = int(input("Digite a quantidade de elementos da lista: "))
        for i in range(quantidade):
            data_buffer = input(f"Digite o elemento {i + 1} da lista de datas no formato dd/mm/aaaa: ")
            try:
                data = datetime.strptime(data_buffer, "%d/%m/%Y").date()
                self.__lista.append(data)
            except ValueError:
                print(f"Formato de data inválido: {data_buffer}")
    
    def mostraMediana(self):
        if not self.__lista:
            print("A lista está vazia.")
            return

        self.__lista.sort()

        if len(self.__lista) % 2 == 0:
            print("Mediana:", self.__lista[len(self.__lista) // 2 - 1])
        else:
            print("Mediana:", self.__lista[len(self.__lista) // 2]) 
     
    def mostraMenor(self):
        if not self.__lista:
            print("A lista está vazia.")
            return

        menor = min(self.__lista)
        print("Menor data:", menor)
    
    def mostraMaior(self):
        if not self.__lista:
            print("A lista está vazia.")
            return

        maior = max(self.__lista)
        print("Maior data:", maior)
    
    def listarEmOrdem(self):
        self.__lista.sort()
        print("Imprimindo elementos em ordem crescente")
        for data in self.__lista:
            print(data)

    def __str__(self):
        return str(self.__lista)
    
    def alterarDatasAnteriores2019(self):
        if not self.__lista:
            print("A lista está vazia.")
            return

        
        def data_anterior_2019(data):
            return data.year < 2019
        
        datas_antigas = list(filter(data_anterior_2019, self.__lista))

       
        for i, data in enumerate(datas_antigas):
            self.__lista[self.__lista.index(data)] = data.replace(day=1)

        print("Datas alteradas (dias modificados para o primeiro dia do mês):")
        for data in self.__lista:
            print(data)
            
    def getLista(self):
        return self.__lista

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        

    def entradaDeDados(self):
        quantidade = int(input("Digite a quantidade de elementos da lista: "))
        for i in range(quantidade):
            salario = float(input(f"Digite o elemento {i + 1} da lista de salários: "))
            self.__lista.append(salario)

    def mostraMediana(self):
        if not self.__lista:
            print("Sem dados")
            return

        self.__lista.sort()

        if len(self.__lista) % 2 == 0:
            valor1 = self.__lista[len(self.__lista) // 2 - 1]
            valor2 = self.__lista[len(self.__lista) // 2]
            print("Mediana:", (valor1 + valor2) / 2.0)
        else:
            print("Mediana:", self.__lista[len(self.__lista) // 2]) 

    def mostraMenor(self):
        if self.__lista:
            smallest_salary = min(self.__lista)
            print("Menor salário:", smallest_salary)
        else:
            print("O vetor de salários está vazio.")

    def mostraMaior(self):
        if self.__lista:
            biggest_salary = max(self.__lista)
            print("Maior salário:", biggest_salary)
        else:
            print("O vetor de salários está vazio.")
    
    def listarEmOrdem(self):
        self.__lista.sort()
        print("Imprimindo elementos em ordem crescente")
        for salario in self.__lista:
            print(salario)

    def __str__(self):
        return str(self.__lista)
    
    def calcularCustoFolha(self):
        if not self.__lista:
            print("Sem dados")
            return

        salarios_reajustados = map(lambda salario: salario * 1.10, self.__lista)

        print("Salários reajustados em 10%:")
        for salario in salarios_reajustados:
            print(salario)
            
    def getLista(self):
        return self.__lista

class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        
    
    def entradaDeDados(self):
        quantidade = int(input("Digite a quantidade de elementos da lista: "))
        for i in range(quantidade):
            idade = int(input(f"Digite o elemento {i + 1} da lista de idades: "))
            self.__lista.append(idade)
    
    def mostraMediana(self):
        if not self.__lista:
            print("Sem dados")
            return

        self.__lista.sort()

        if len(self.__lista) % 2 == 0:
            idade1 = self.__lista[len(self.__lista) // 2 - 1]
            idade2 = self.__lista[len(self.__lista) // 2]
            print("Mediana:", (idade1 + idade2) // 2)
        else:
            print("Mediana:", self.__lista[len(self.__lista) // 2])    
    
    def mostraMenor(self):
        if self.__lista:
            smallest_age = min(self.__lista)
            print("Menor idade:", smallest_age)
        else:
            print("O vetor de idades está vazio.")
    
    def mostraMaior(self):
        if self.__lista:
            biggest_age = max(self.__lista)
            print("Maior idade:", biggest_age)
        else:
            print("O vetor de idades está vazio.")

    def listarEmOrdem(self):
       self.__lista.sort()
       print("Imprimindo elementos em ordem crescente")
       for idade in self.__lista:
            print(idade)

    def __str__(self):
        return str(self.__lista)
    
    def getLista(self):
        return self.__lista

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
    
    print("Mostrar nomes com salários:")
    if not nomes.getLista():
        print("A lista está vazia.")
        return
        
    for nome, salario in zip(nomes.getLista(), salarios.getLista()):
        print(f"Nome: {nome}, Salário: {salario}")

    
        print("\nCusto da folha de pagamento com reajuste de 10%:")
        salarios.calcularCustoFolha()

        if isinstance(datas, ListaDatas):
            datas.alterarDatasAnteriores2019()
            
        print("___________________")

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()
