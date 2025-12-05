nombre1 = input("saisir un nombre : ")
nombre2 = input("saisir un autre nombre  : ")

if not nombre1.isnumeric() or not nombre2.isnumeric():
    print ("erreur: les nombre saisie no sont des entier")
    raise SystemExit("Fin du programme")

nombre1 = int(nombre1)
nombre2 = int(nombre2)

operation = input("saisir une operation entre [ + , - , *, /] : ")

if operation not in ["+", "-", "*", "/" ]:
    print("l;operateur saisie n'est pas compris dans la liste ")
    raise SystemExit("Fin du programme")

if operation == "+":
    resultat = (nombre1) + (nombre2)
elif operation == "-":
    resultat = (nombre1) - (nombre2)
elif operation == "*":
    resultat =(nombre1) *  (nombre2)
elif operation == "/":
    if nombre2 == 0 :
        print("Erreur : un nombre ne peut pas etre diviser par 0")
        raise("Fin du programme")
    resultat = round(nombre1 / nombre2, 2)

print (f"le resultat de l'operation est: {round(resultat, 2)}" )
