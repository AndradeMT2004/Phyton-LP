from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    cpf: str

@dataclass
class Pet:
    nome: str
    idade: int
    peso: float

pessoa1 = Pessoa("Bob", 50, "143.244.354-95")
pet1 = Pet("Marley", 2, 32)

print(f"Nome: {pessoa1.nome} \nidade: {pessoa1.idade} \nCPF: {pessoa1.cpf}")
print(f"Nome do pet: {pet1.nome} \nidade: {pet1.idade} \npeso: {pet1.peso}")