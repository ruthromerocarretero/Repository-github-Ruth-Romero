def validarnom(nom):
    while not nom.isalpha():
        print(f"El nom {nom} no es correcte")
        nom = input("Digues el teu nom: ")
    print(f"El nom {nom} es correcte")
nom = input("Digues el teu nom: ")
validarnom(nom)