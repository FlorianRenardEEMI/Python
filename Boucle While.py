nb = 7 # On garde la variable contenant le nombre dont on veut la table de multiplication
i = 0 # C'est notre variable compteur que nous allons incrémenter dans la boucle

while i < 10: # Tant que i est strictement inférieure à 10
    print(i + 1, "*", nb, "=", (i + 1) * nb)
    i += 1 # On incrémente i de 1 à chaque tour de boucle

# resultat
# 1 * 7 = 7
# 2 * 7 = 14
# 3 * 7 = 21
# 4 * 7 = 28
# 5 * 7 = 35
# 6 * 7 = 42
# 7 * 7 = 49
# 8 * 7 = 56
# 9 * 7 = 63
# 10 * 7 = 70
# on remarque la multiplication 0*7 ne s'affiche pas.
