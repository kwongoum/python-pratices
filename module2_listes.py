# maList= ["je", "suis","un","camerounais","bams"]
# print(maList)
#
# for i in maList:
#     print(i)
    #----------------
# maChaine = "une phrase donnée"
# it = iter(maChaine)  # iterable
# index=0
# while(index< len(maChaine)):
#     print(next(it))
#     index=index+1
# else:
#     print("fin du traitement")
    # ------------ set -----------

aSet = {'pomme', 'banane','poire','banane','ananas'}
print(aSet)

# --- liste to set ---------
list =["Avit","Laurine","Gwladys","Bertrand"]
mySet= set(list)
mySet.add("Boris")
print("my new set is: ",mySet)
mySet.add("Boris")
print("my new set after addd same value is: ",mySet)
mySet.discard("Boris")
print("my new set is3: ",mySet)
mySet.discard("Boris")
if "Avit" in mySet:
    print("Avit existe")
else:
    print("Avit n'existe pas")

monSetToAdd = {'mandarine', 'pêche','Avit'}
allSet = monSetToAdd.union(mySet)
print(allSet)
allSet = monSetToAdd| mySet
print(allSet)

myInter = mySet.intersection(monSetToAdd)
myInter = mySet&(monSetToAdd)

print("myInter : ")
print(myInter)
monSet = {'pomme', 'orange', 'banane', 'kiwi'}
monSetToAdd = {'pomme', 'banane'}
result1= monSet.difference(monSetToAdd)
result2= monSet - monSetToAdd
print(result1)
print("result2: ",result2)
# -------- tuple -----------
monTuple = ("pomme","banane")
monTuple2 = ("orange",)

resultat = monTuple + monTuple2

print("Le resultat est tu :", resultat)
for value in resultat:
    print("la valeur est",value)
    # --------- Dictionnaire ----------------
myDict = dict(nom="Wongoum",prenom="Avit")
print(myDict)
myDict2={"nom":"Wogoum","prenom":"Avit"}
print("2eme methode",myDict2)
myDict2["nom"]="Kangoum" #modification de la valeur associée à une clé
myDict2["age"]=23 # ajouter une cle valeur
print("avant suppression",myDict2)
del myDict2["age"]# -- suppression  d'une cle valeur
print("apres suppression",myDict2)
if 'nom' in myDict2: # verification de l'existance d'une cle
    print("la cle nom existe")
if 'pays' not in myDict2:
    print("Le pays n'existe pas dans le dictionnaire comme cle ")
myDict2["pays"]="Belgique"
for k in myDict2:
    print("une des cle du dictionnaire est:", k)
for v in myDict2.values():
    print("Une valeur du dic est", v)
for k,v in myDict2.items():
   # print("une cle valeur est :", k,v)
    print(f"valeur du dictionnaire pour la clé {k}: {v}")
monSet={1,2,5,6}
monSet2= {3,4,5,6}
monSet3 ={5,6}
print("UNIR monSet et monSet2", monSet.union(monSet2))
print("DIFFERENCE monSet2 et monSet3", monSet2.difference(monSet3))
print("INTERSECTION monSet et monSet3", monSet.intersection(monSet3))
#-- exercices
mesCours=("Python3","Perfectionnement au langage Python 3","Python 3 for DataScientists")
print(mesCours)
for value in mesCours:
    print("Je suis le cours de ",value)