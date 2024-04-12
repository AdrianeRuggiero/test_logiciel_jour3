"""def sans_doublons(liste):
    liste_sans_doublons = []
    for element in liste:
        if element not in liste_sans_doublons:
            liste_sans_doublons.append(element)
    return liste_sans_doublons

# Exemple
liste = [1, 2, 3, 4, 3, 2, 1]
liste_final = sans_doublons(liste)
print(liste_final)"""


def rotation_gauche(liste):
    premier_element = liste[0]  # Stocke le premier élément
    for i in range(len(liste) - 1): 
        liste[i] = liste[i +1]  
    liste[-1] = premier_element  
    return liste

# Exemple d'utilisation :
liste = [1, 2, 3, 4]
nouvelle_liste = rotation_gauche(liste)
print(nouvelle_liste)
