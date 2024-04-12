def sans_doublons(liste):
    liste_sans_doublons = []
    for element in liste:
        if element not in liste_sans_doublons:
            liste_sans_doublons.append(element)
    return liste_sans_doublons

# Exemple
liste = [1, 2, 3, 4, 3, 2, 1]
liste_final = sans_doublons(liste)
print(liste_final)