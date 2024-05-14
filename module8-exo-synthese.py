import random
import string

class Personne:
    def __init__(self, nom, prenom, adresse):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse


class Employe(Personne):
    def __init__(self, nom, prenom, adresse, fonction):
        super().__init__(nom, prenom, adresse)
        self.fonction = fonction

    def afficher(self):
        print(f"Nom: {self.nom}, Prénom: {self.prenom}, Adresse: {self.adresse}, Fonction: {self.fonction}")


class Etudiant(Personne):
    def __init__(self, nom, prenom, adresse):
        super().__init__(nom, prenom, adresse)
        self.matricule = self.generer_matricule()
        self.cours = []

    def generer_matricule(self):
        deux_lettres_prenom = self.prenom[:2].upper()
        deux_lettres_nom = self.nom[:2].upper()
        chiffres = ''.join(random.choices(string.digits, k=4))
        return deux_lettres_prenom + deux_lettres_nom + chiffres

    def afficher(self):
        print(f"Nom: {self.nom}, Prénom: {self.prenom}, Adresse: {self.adresse}, Matricule: {self.matricule}")
        print(" Cours fréquentés:")
        for cours in self.cours:
            print(" - " + cours)


# Fonction pour encoder un employé
def encoder_employe():
    nom = input("Entrez le nom de l'employé : ")
    prenom = input("Entrez le prénom de l'employé : ")
    adresse = input("Entrez l'adresse de l'employé : ")
    fonction = input("Entrez la fonction de l'employé : ")
    employes.append(Employe(nom, prenom, adresse, fonction))


# Fonction pour encoder un étudiant
def encoder_etudiant():
    nom = input("Entrez le nom de l'étudiant : ")
    prenom = input("Entrez le prénom de l'étudiant : ")
    adresse = input("Entrez l'adresse de l'étudiant : ")
    etudiant = Etudiant(nom, prenom, adresse)
    while True:
        choix = input("Voulez-vous ajouter un cours pour cet étudiant ? (O/N) : ").upper()
        if choix == 'O':
            cours = input("Entrez le nom du cours : ")
            etudiant.cours.append(cours)
        elif choix == 'N':
            break
        else:
            print("Veuillez entrer 'O' pour oui ou 'N' pour non.")
    etudiants.append(etudiant)


# Liste pour stocker les employés et les étudiants encodés
employes = []
etudiants = []

while True:
    print("\nMenu:")
    print("1. Entrer le chiffre 1 pour encoder un employé")
    print("2. Entrer le chiffre 2 pour encoder un étudiant")
    print("0. Entrer le chiffre 0 pour quitter le programme")
    choix = input("Votre choix : ")

    if choix == '1':
        encoder_employe()
    elif choix == '2':
        encoder_etudiant()
    elif choix == '0':
        print("\nPersonnes encodées :")
        print("Employés :")
        for employe in employes:
            employe.afficher()
        print("\nÉtudiants :")
        for etudiant in etudiants:
            etudiant.afficher()
        break
    else:
        print("Choix invalide. Veuillez saisir 1, 2 ou 0.")
