print("my name is Avit")
isValid = False

while not isValid:
    try:

        age = int(input("Give your age : "))
        if 0 < age <= 99:
            isValid = True
        else:
            print("Give a value between 1 and 99 included")

    except:
        print("Give your age in a numerical integer format")
else:
    print(f"Given age is : {age}")
