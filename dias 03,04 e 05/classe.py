from abc import ABC, abstractmethod

class IAnimal(ABC):

    @abstractmethod
    def falar(self):
        '''Defina na classe filha'''

    @abstractmethod
    def andar(self):
        '''Defina na classe filha'''

class Cachorro(IAnimal):
    def falar(self):
        print("Auau")

    def andar(self):
        print("Ando com 4 patas")

class Pessoa:

    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
        self.__humano = True

    def fala_pessoa(self):
        print("Falando")

cachorrochupetao = Cachorro()
cachorrochupetao.falar()
cachorrochupetao.andar()