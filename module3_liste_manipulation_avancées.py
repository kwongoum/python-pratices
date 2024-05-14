from functools import  reduce
list1=[1,3,4,5]
listSquare=[]
# for elt in range(len(list1)):
#     listSquare.append(list1[elt]**2)
listSquare=[elt**2 for elt in list1]
print("square",listSquare)
# -------- list comprehension ---
listnum =[20,40,60,70,80,100]
listnum.append(2)
for el in listnum:
    print(el)
listUp=[f"{elt}%" for elt in listnum if 50<=elt<=100 ]
print("up to 50",listUp)
def doubler(x):
    return x**2
sequence = [2,3,8,5,9,10]
myMap= list(map(doubler, sequence))
print("myMap",myMap)
 # --------- filter
def impaire(x):
    answer= False
    if x%2==1:
     answer=True
    return answer

filterImpaire =  list(filter(impaire, sequence))
print("impaire elt", filterImpaire)
def test(x): return x % 2 == 0

myList = [1,2,3,4,5,6,7,8,9,10]
myResult = list(filter(test, myList))

print("paire",myResult)
# ------ reduce
def custumSum(x,y):
    return x+y
theSum= reduce(custumSum,myList,2)
print("theSum",theSum)
print("theSum / sum",sum(myList))
sumLambda= reduce(lambda x,y:x+y, myList)
print("sumLambda",sumLambda)
print("ohhhh",2%2==0)

isEvenNum = lambda x: x%2==0

rep= isEvenNum(30)
print(rep)
# start = int (input("entrer un nombre:"))
# while(start>0):
#     print(start)
#     start=start-1

# else: print("END")
# def uncount(x):
#     if(x>0):
#         print(x)
#         uncount(x-1)
#     else:
#      print("END")
# start = int(input("Entrez un nombre : "))
# uncount(start)

maSequence = ["jean", "claude", "eudes", "david", "julia", "katarina"]
valueToFind = "julia"
result = None

for i, value in enumerate(maSequence):
    if value == valueToFind:
        result = i
        break;

if (result == None):
    print(f"{valueToFind} n'est pas présent dans la séquence")
else:
    print(f"{valueToFind} se trouve dans la séquence en position {result}")
    # ---- function recursive to find value ------------


# def indexOf(value, array, index=0):
#     if (index == len(array)): return None
#
#     if (array[index] == value):
#         return index
#     else:
#         index = index + 1
#         return indexOf(value, array, index)
#
#
# maSequence = ["jean", "claude", "eudes", "david", "julia", "katarina"]
# valueToFind = "julia"
#
# result = indexOf(valueToFind, maSequence)
#
# if (result == None):
#     print(f"{valueToFind} n'est pas présent dans la séquence")
# else:
#     print(f"{valueToFind} se trouve dans la séquence en position {result}")
myList=[1,2,3,4,5,6,7,8,9,10]

print("myList",myList)

# listPaire= list(filter(lambda x:x%2==0, myList))
listPaire= list(filter(lambda x:x%2==0, [1,3,5,6,7,8,9,11,12,16,17]))
print("listPairee",listPaire)
# # listSquare = map(lambda y:y**2,listPaire)
# listSquare = map(lambda y:y**2,list(filter(lambda x:x%2==0, myList)))
# print("listSquare",list(listSquare))

myList=[1,2,3,4,5,6,7,8,9,10]

print("myList",myList)

# listImpaire= list(filter(lambda x:x%2==1, myList))
# print("listImpaire",listImpaire)
#
# def factorielle(n):
#     if(n<=0): return 1
#     else: return n*factorielle(n-1)
# print("factoriel est: ",factorielle(5))

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squareValues= list(map(lambda x: x ** 2, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

print("squareValues: ",squareValues)