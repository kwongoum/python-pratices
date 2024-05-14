# print("my name is Avit")
# isValid = False
#
# while not isValid:
#     try:
#
#         age = int(input("Give your age : "))
#         if 0 < age <= 99:
#             isValid = True
#         else:
#             print("Give a value between 1 and 99 included")
#
#     except:
#         print("Give your age in a numerical integer format")
# else:
#     print(f"Given age is : {age}")
     #  ---------------------
def divide(n,d):
        if d==0:
            raise(ZeroDivisionError("On ne peut diviser pas Zero"))
        return n/d
def encoderInt():
        try:
            return int(input("Veuillez encoder un nobre entier"))
        except (TypeError, ValueError):
            print("type de valeur incorrect, nbre entier attendu !")
            return encoderInt()

# main code
numerator = encoderInt()
denominator= encoderInt()

try:
 result= float(divide(numerator,denominator))
 print(f"numerateur {numerator} divise par dénominateur {denominator} vaut: {result}")
except ZeroDivisionError as err:
    print(f" une erreur survenue: {err}")
except Exception as e:
    print(f"une exception est survenu: {e}")





    


