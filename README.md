# Exercices d'algorithmique et programmation sur l'algèbre de Bool

## Exercice 1 :

Dans cette exercice 1, il nous a été demandé de créer un algorithme et un programme en python qui permet d'afficher la ``table de vérité`` de n'importe quel fonction logique introduite et d'afficher par la suite la ``première`` ainsi que la ``deuxième forme canonique`` de cette fonction logique.

Dans ce code une fonction nommée ``logical_function`` est la fonction logique à ``n variables``.
En effet, il suffira de modifier l'expression de cette fonction logique afin d'avoir le résultat voulu.
Dans ce code, j'ai initialisé la fonction logique en une expression particulière mais afin de le tester avec d'autres fonctions logiques :

-- Le syntaxe de cette fonction logique ``logical_function`` est la suivante :
        ------  nom : ``logical_function``
        ------ paramètres : ``*variables`` : cela signifie que la fonction logique est programmée à recevoir autant de variables logique
        (Il suffira alors d'identifier les variabes avec les index tels que ``variables[0]``, ``variables[1]``,``variables[2]``, ... et ainsi de suite )
        
    Exemple : def logical_function(*variables):
                    return (variables[0] and variables[1]) or (variables[0] and variables[2]) or (not variables[1] and (not variables[2])) or variables[3]

symilaire à ``f(a,b,c) = a.b + a.c + (non b).(non c) + d``

En fin, il y a la fonction qui permet d'executer le tout : la fonction ``table_of_truth`` qui prend en paramèter '''la fonction logique''' comme callback function et le '''nombre de variable'''
Ainsi le syntaxe de cette ``table_of_truth`` est :
        ------ nom :``table_of_truth``
        ------ paramètres :  ``logical_function`` et ``variables_number`` qui est le nombre de variables de la fonction logique
    
    Exemple d'execution : table_of_truth(logical_function, 3) 
pour la fonction logique de l'exemple ci-dessus.

## Exercice 2 :
On nous a demandé de créer un algorithme et programme en python qui va afficher le ``tableau de Karnaugh`` qui permet de simplifier les les fonctions logique et d'y tiré la foncion simplifié. En raison de difficulté conséquence du procédé avec l'algorithme de Karnaugh pour obtenir la simplification, ce code ne pourra afficher que le ``tableau de Karnaugh``:

Identique à celui de l'``exercice 1``, ce code va prendre en compte une fonction logique nommé ``logical_function(*variables)`` , la fonction qui va tout executer : ``karnaugh_table(n,q)`` surtout les _plus importants_, le _``nombre de variable en haut sur l'horizontale``_  noté ``n`` et le _``nombre de variable en bas sur la verticale`` noté ``q`` du ``tableau de Karnaugh`` :

Un exemple de la fonction logique est déjà énoncé un peu plus haut mais voici donc un exemple d'exécution du code _``après avoir pré-définie la fonction logique à utiliser``_:

    Exemple d'execution : karnaugh_table(2, 2)
avec la fonction logique que j'ai donné comme exemple un peu plus haut. Cette tableau sera alors un tableau où les ``2`` _(le premier dans le paramètre ``n=2``)_ premiers variables sera placé sur la horizontale _``ab``_ et ``2`` _(le deuxième, ``q=2``)_ variables sur la vertical _``cd``_ tel que :
    
    ab     00 | 01 | 11 | 10
    cd   || ===================
    00   || 1  | 0  | 1  | 1
    01   || 1  | 1  | 1  | 1
    11   || 1  | 1  | 1  | 1
    10   || 0  | 0  | 1  | 1


