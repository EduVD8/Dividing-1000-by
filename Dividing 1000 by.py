x = "a"
cont = 0
while (type(x) != int or x == 0):
    try: 
        x = int(input("Enter an integer to divide 1000 by: "))
        y = 1000 / x
    except ValueError:
        print("It must be an integer.")
        cont += 1
    except ZeroDivisionError:
        print("0 not allowed!")
        cont += 1
        x = "a" #
print("The result is", round(y), "with", cont, "failures")