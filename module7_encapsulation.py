# class Personne:
#     def __init__(self, nom,prenom):
#         self._nom=nom
#         self.__prenom=prenom
#
#     def __str__(self):
#         return f"Cette personne s'appelle {self.__prenom} {self._nom}"
#
#     def setNom(self,nom):
#         self._nom=nom
#     def getNom(self):
#         return self._nom
#
#
#
# personne1=Personne("Wongoum","Avit")
# print(personne1)
# # personne1.__nom="Kangoum"
# print("access private property/attribute", personne1._nom)
# print("after set value",personne1)
# personne1.setNom("kangoum")
# print("after set value",personne1)
# =====================


# class Employe:
#     def __init__(self, nom="", prenom="",age=0):
#         if nom: self.nom=nom
#         if prenom: self.prenom=prenom
#         if age: self.set_age(age)
#
#         # getter with property
#     @property
#     def age(self):
#             return self.__age
#     # setter with property
#     @age.setter
#     def age(self,age):
#             if 0 < age < 100:
#                 self.__age = age
#             else:
#                 raise Exception("Age doit etre compris entre 0 et 100")
#
#     def set_age(self, age):
#         self.__age=0
#         if 0<age<100:
#             self.__age = age
#         else: raise Exception("Age doit etre compris entre 0 et 100")
#
#     # def get_age(self):
#     #     return self.__age
#
#
#
#     def __str__(self):
#         return f"classe object est {type(self).__name__}. Cet employe est: {self.prenom} {self.nom} et agé de {self.__age}"
#
# nom = input("Entrer le nom: ")
# prenom = input("Entrer le prenom: ")
# age=0
# ageValide= False
#
#
# employe1=Employe()
# while ageValide==False:
#   try:
#     ageEntre= int(input("Entrer l'age: "))
#     if 0<ageEntre<100:
#         age =ageEntre
#         ageValide=True
#         employe1.set_age(age)
#     else:
#         raise Exception("Age doit etre comprise entre 0 ET 100")
#   except Exception as err: print(err)
# else:
#     employe1.prenom=prenom
#     employe1.nom=nom
# print(employe1)
# class Personne:
#     def __init__(self, nom="", prenom="", age=0):
#         if nom: self.nom = nom
#         if prenom: self.prenom = prenom
#         if age: self.set_age(age)
#
#     def __str__(self):
#         return f"""Objet {type(self).__name__}
# Valeur de l'attribut nom: {self.nom}
# Valeur de l'attribut prénom: {self.prenom}
# Valeur de l'attribut âge: {self.__age}"""
#
#     # méthode de modification (ou SETTER)
#     def set_age(self, age):
#         if 0 < age < 100:
#             self.__age = age
#         else:
#             raise Exception("L'âge doit être compris entre 1 et 99, réessayez")
#
#         # méthode d'accès (ou GETTER)
#
#     def get_age(self):
#         return self.__age




# # définition d'une variable de contrôle de boucle
# encodagePending = True
# # création d'un objet Personne
# unePersonne = Personne()
#
# nom = input("Encode ton nom : ")
# prenom = input("Encode ton prénom : ")
# age = 0
#
# # Boucle d'encodage de l'âge
# while encodagePending:
#     try:
#         age = int(input("Encode ton âge : "))
#         unePersonne.set_age(age)
#         encodagePending = False
#     except Exception as err:
#         print(err)
# else:
#     unePersonne.nom = nom
#     unePersonne.prenom = prenom
#     # affichage des informations de l'objet
#     print(unePersonne)

#
# class Personne:
#
#     def __init__(self, nom, prenom):
#         self.nom = nom
#         self.prenom = prenom
#
#     @property
#     def nom(self):
#         return self.__nom
#
#     @nom.setter
#     def nom(self, nom):
#         print(f"nom will be set : {nom}")
#         self.__nom = nom
#
#     @property
#     def prenom(self):
#         return self.__prenom
#
#     @prenom.setter
#     def prenom(self, prenom):
#         print(f"prenom will be set : {prenom}")
#         self.__prenom = prenom
#
#     def __str__(self):
#         return f"La personne s'appelle {self.__prenom} {self.__nom}"
#
#
# pers1 = Personne("Claude", "Jean")
# print(pers1)
#
# pers1.prenom = "Marie"
# print(pers1)
#
# pers1.nom = "Vandenhoudenaert"
# print(pers1)

class Personne:
    def __init__(self,prenom="",nom=""):
        self.__prenom=prenom
        self.__nom=nom


    @property
    def prenom(self):
       return  self.__prenom

    @prenom.setter
    def prenom(self, prenom):
        self.__prenom = prenom

    @property
    def nom(self):
        return  self.prenom

    @nom.setter
    def nom(self,nom):
        self.__nom=nom

    def  __str__(self):
        return (f" class type:{type(self).__name__} \n "
                f"prenom: {self.prenom}\n"
                f"nom : {self.__nom}")


# main execution

objPersonne= Personne("Jean-Eudes","Delamare d'acoté")
print(objPersonne)
