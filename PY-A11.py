'''[PY-A11]Desenvolva um exemplo de aplicação de polimorfismo utilizando super classe.
Crie uma classe pai que defina um método genérico, e em seguida crie duas ou mais classes
filhas que herdem essa super classe e sobrescrevam o método de acordo com suas necessidades.'''

# Classe pai
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False

# Funções
    def ligar(self):
        self.ligado = True
        print("Carro ligado!\n")

    def desligar(self):
        self.ligado = False
        print("Carro desligado!\n")

    def tipoVeiculo(self): #Função que exercerá o polimorfismo, alterando o resultado de acordo com a classe filha
        pass

    def exibirInformacoes(self):
        print("\n---- INFORMAÇÕES TÉCNICAS ----")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Condição do carro: {'Ligado' if self.ligado == True else 'Desligado'}") # Estrutura condicional para checar se o carro está ligado ou não

# Classe filha 1
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano) # Para puxar as características da Classe pai
        self.portas = portas # Característica exclusiva dessa função filha
    def exibirInformacoes(self):
        super().exibirInformacoes() # Aproveitar a função da Classe pai
        print(f"Número de portas: {self.portas} portas") # Somente para incluir a característica da Classe filha
    def tipoVeiculo(self):
        print(f"Tipo do veículo: Carro")

# Classe fiha 2
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano) # Para puxar as características da Classe pai
        self.cilindradas = cilindradas # Característica exclusiva dessa função filha
    def exibirInformacoes(self):
        super().exibirInformacoes() # Aproveitar a função da Classe pai
        print(f"Cilindradas: {self.cilindradas} cilindradas") # Somente para incluir a característica da Classe filha
    def tipoVeiculo(self):
        print(f"Tipo do veículo: Moto")

# Classe filha 3
class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, eixo):
        super().__init__(marca, modelo, ano) # Para puxar as características da Classe pai
        self.eixo = eixo # Característica exclusiva dessa função filha
    def exibirInformacoes(self):
        super().exibirInformacoes() # Aproveitar a função da Classe pai
        print(f"Capacidade do eixo: {self.eixo} toneladas") # Somente para incluir a característica da Classe filha
    def tipoVeiculo(self):
        print(f"Tipo do veículo: Caminhão")

carro1 = Carro("Fiat", "Palio", 2020, "4")
moto1 = Moto("Honda", "Bros", 2023, 150)
caminhao1 = Caminhao("Scania", "770", 2022, 33)

carro1.exibirInformacoes()
carro1.tipoVeiculo()
moto1.exibirInformacoes()
moto1.tipoVeiculo()
caminhao1.exibirInformacoes()
caminhao1.tipoVeiculo()
carro1.ligar()
carro1.exibirInformacoes()