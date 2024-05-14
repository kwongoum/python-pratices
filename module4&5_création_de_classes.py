class Message():
    def afficherMessage(self,message):
        print(message)
message1= Message()
message1.afficherMessage("bonjour tout le monde ")


class Personne():
  denomination="personne"
  def __init__(self, prenom, nom):
      self.prenom=prenom
      self.nom=nom
      print(f"creation d'un objet Personne prenom est '{prenom}' et nom est '{nom}'")
      pass
  # def __del__(self):
  #     print("Destruction de l'objet personne")
avit= Personne("Avit","Kangoum")
avit.denomination="quelquun"
print(Personne.denomination)
print("avit prenom",avit.prenom)
print("avec instance: ",avit.denomination)
# print("fin du script le destructeur sera appele et le prgramme s'arrete !")
@classmethod
def creerObjet(cls, prenom, nom):
    return cls(prenom, nom)


def sePresenter(self):
    return f"Bonjour, je m'appelle {self.prenom} {self.nom}"

# ---------- class participant -------

# Écrivez une classe Participant permettant de modéliser le participant d'une formation FAD.
#
# Un participant est caractérisé par un nom, un prénom ainsi qu'une liste de formations qu'il suit. Il faut pouvoir :
#
# Afficher les caractéristiques d'un participant :
# " Le participant s'appelle [prenom] [nom], il suit actuellement [nombre de formations] formation(s).
# Voici les formations suivies: [formations]"
# Ajouter une formation à la liste des formations que suit le participant.
# Le participant sera, au minimum, construit sur base de son nom et de son prénom.
class Participant:

    def __init__(self, nom, prenom, formations):
        self.nom =nom
        self.prenom=prenom
        self.formations=formations


    def infoParticipant(self):
        print(f"Le participant s'appelle {self.prenom} -{self.nom}"
              f", il suit actuellement {len(self.formations)} formations."
              f"Voici les formations suivies:{self.formations}")
    def ajouterUneFormation(self, formation):
        self.formations.add(formation)
participant1= Participant("Wongoum","Avit", {"Python","Java","SQL","Javascript"})
participant1.infoParticipant()
participant1.ajouterUneFormation("Angular")
participant1.infoParticipant()
class Animal:
    nombreTotal=5

animal1=Animal()
print("animal1",animal1)
#---------------
class Personne:
    total=100
    def __init__(self):
        self.nom= input("Veuillez introduire notre nom: ")
        self.prenom= input("Veuillez introduire notre prenom: ")
    def sePresenter(self):
        print(f"Cette personne s'appelle {self.prenom} {self.nom}")

personne1=Personne()
personne1.sePresenter()
print(personne1.total)

print(Personne.total)
