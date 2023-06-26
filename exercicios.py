class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.Cor = cor
        self.Placa = placa
        self.NumRodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave,valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.Carregado = carregado

    def esta_carregado(self):
        print(f"{'Está' if self.Carregado else 'Não está'} carregado")


moto = Motocicleta("preta", "abc-1234", 2)
moto.ligar_motor()

carro = Carro("branco", "def-1234", 4)
carro.ligar_motor()

caminhao = Caminhao("roxo", "ghi-1234", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()

print(carro)
print(moto)
print(caminhao)