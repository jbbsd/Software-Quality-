
#!/usr/bin/env python3


def main(): 
    #Récupération des données
    a = input("1ere valeur: ")
    operator = input("Opérateur: ")
    b = input("2eme valeur: ")
    #Calculatrice avec les opérateurs
    if (operator == ('+')):
        x = int(a) + int(b) 
        print("a + b = ", x)
    elif (operator == ('-')):
        x = int(a) - int(b) 
        print("a - b = ", x)
    elif (operator == ('/')):
        x = int(a) / int(b) 
        print("a / b = ", x)
    elif (operator == ('*')):
        x = int(a) * int(b) 
        print("a * b = ", x)
    else:
        print("Mauvais opérateur")






main()