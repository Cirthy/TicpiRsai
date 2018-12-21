# Ticpirsai

Réalisation d'un protocole de communication basé TCP sécurisé par RSA. Le 

## Réseau

## RSA

Au démarrage, le programme va générer les clés nécessaires à l'utilisation du chiffrement RSA :
* Les nombres premiers `p` et `q` ont respectivement 500 et entre 451 et 470 chiffres. On ne les choisit pas trop proche pour que notre `n = pq` ne devienne pas factorisable (par exemple par l'algorithme de Fermat)
* Notre deuxième clé publique `e` vaut toujours *65537*, elle doit être première avec φ(n) = (p - 1) * (q - 1) afin de pouvoir calculer son inverse modulaire.
* On finit par calculer la clé privée `d = e^(-1) mod φ(n)`

