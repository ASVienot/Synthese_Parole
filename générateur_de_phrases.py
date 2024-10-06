#Générateur de phrase pour le projet de synthèse de la parole - Alix Sirven-Viénot

# Listes de valeurs pour les variables X, F et C
X = ["pommes", "poires", "pêches", "pastèques", "bananes", "jujubes", "cerises"]
X2 = ["pommes", "poires", "pêches", "pastèques", "bananes", "jujubes", "cerises"]
C = ["rouges", "vertes"]
F = ["ma mère", "mon père", "ma grand-mère", "mon grand-père", "ma soeur"]
M = ["janvier", "février", "mars", "mai", "juillet","août", "septembre", "novembre", "dêcembre"]
M2 = ["janvier", "février", "mars", "mai", "juillet", "août", "septembre", "novembre", "dêcembre"]

phrases = open("phrases_possibles.txt", "w")

# Boucle pour générer toutes les combinaisons phrase 1 
for Fruit in X:
    for Fruit2 in X2: 
        for Couleur in C:
            for Famille in F:
                phrase = f"J' aime les {Fruit} {Couleur} et {Famille} les {Fruit2} {Couleur} .\n"
                phrases.write(phrase)

# Boucle pour générer toutes les combinaisons phrase 2
for Fruit in X:
    for Fruit2 in X2: 
        for Couleur in C:
            for Mois in M:
                for Mois2 in M2: 
                    phrase = f"On plante les {Fruit} en {Mois} et les {Fruit2} en {Mois2} .\n"
                    phrases.write(phrase)

# Boucle pour générer toutes les combinaisons phrase 3
for Fruit in X:
    for Fruit2 in X2: 
        for Famille in F:
            phrase = f"{Famille} avait des {Fruit} et des {Fruit2} dans son jardin .\n"
            phrases.write(phrase)

# Boucle pour générer toutes les combinaisons phrase 4
for Famille in F:
    for Mois in M:
        for Mois2 in M2: 
                    phrase = f"Je suis née en {Mois} et {Famille} en {Mois2} .\n"
                    phrases.write(phrase)

# Boucle pour générer toutes les combinaisons phrase 5
for Fruit in X:
    for Fruit2 in X2: 
        phrase = f"Pour la recette , il faut mettre les {Fruit} puis les {Fruit2} .\n"
        phrases.write(phrase)

phrases.close()