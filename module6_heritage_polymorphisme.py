from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self,nom):
        self.nom=nom
    def faireBruit(self, intensite=None):
        if intensite == None:
            print(f"l'animal ne fait pas de bruit")
        else:
            print(f"fait du bruit avec une intensite:{intensite}")
    @abstractmethod
    def crier(self): pass
class Chien(Animal):
    def __init__(self, nom, race):
        super().__init__(nom)
        self.race=race

    def aboyer(self):
        print(f"chien aboie et s'appelle, {self.nom} et est de race {self.race}")

    def __str__(self):
        return f"object de la classe Chien, de race {self.race}"
    def crier(self):
        print("un chien crie avec ouaouuuuuu")

class Chat(Animal):
    def crier(self):
        print("un chat crie Miaouuuuuuuuu")

chat1= Chat("zavaro")
chat1.crier()
chien1= Chien("Bobby","Caniche")
chien1.aboyer()
chien1.faireBruit(5)
print(chien1)
print("1A ",isinstance(chat1,object))
# ------------
# class Animal:
#     pass
# class Carnivore(Animal):
#     pass
# class Chien(Carnivore):
#     pass
# class Chat(Carnivore):
#  pass
#
# chien1= Chien()
# print("Mon objet chien est de type Chien : ", isinstance(chien1,Chien))
# print("Mon objet chien est de type Chat : ", isinstance(chien1,Chat))
# print("Mon objet chien est de type Carnivore : ", isinstance(chien1,Carnivore))
# print("Mon objet chien est de type Animal : ", isinstance(chien1,object))