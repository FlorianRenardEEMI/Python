def table(nb, max): # definition d'une fonction
    i = 0
    while i < max: # Tant que i est strictement inférieure à la variable max,
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1


# table (6,20) <= syntaxe pour appeler et executer la fonction