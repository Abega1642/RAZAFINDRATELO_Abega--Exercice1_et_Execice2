# Exercices d'algorithmique et programmation sur l'algèbre de Boole

## Exercice 1 :

Dans cette exercice 1, il nous a été demandé de créer un algorithme et un programme en python qui permet d'afficher la ``table de vérité`` de n'importe quel fonction logique saisi par l'utilisateur et d'afficher par la suite la ``première`` ainsi que la ``deuxième forme canonique`` de cette fonction logique.

Le programme vous demandera d'abord le nombre de variable qui sera dans votre fonction logique. 

    How many variables is your function ? →

Ensuite, il vous demandera de nommer un par un vos variables (par exemple : a, b ou x, y ou x1, x2 ou v1,v2 ou var1,var2... comme vous vous voudrez)

    Please, enter the variable number 1: "le nom de votre variable"
    Please, enter the variable number 2: "le nom de votre variable"
    Please, enter the variable number 3: "le nom de votre variable"
    ...

Le programme va ensuite vous demander de faire enter l'expression de votre fonction logique en respectant les syntaxes tels que ``not`` ou ``not_``, ``and`` et ``or``

``Attention !: un espace après chaque variable ou connecteur logique mais jamais au début ni à la fin de la fonction logique``

Exemple :

    Please enter your logical function. ('not' or 'not_' : negation, 'and', 'or')
        ==> f(a,b,c,d) = a and b and not_c or not c and d
    
symilaire à ``f(a,b,c,d) = a.b.(non c) + (non c).d``

Il suffit d'appeler la fonction ``table_of_truth`` pour lancer le programme.

## Exercice 2 :
On nous a demandé de créer un algorithme et programme en python qui va afficher le ``tableau de Karnaugh`` qui permet de simplifier les les fonctions logique et d'y tiré la foncion simplifié. En raison de difficulté conséquente du procédé avec l'algorithme de Karnaugh pour obtenir la simplification, ce code ne pourra afficher que le ``tableau de Karnaugh``:

Identique à celui de l'``exercice 1``, le programe va vous demander le nombre de variables de votre fonction logique, ensuite les nommenclatures des variables et enfin l'expression de la fonction logique.

A la différence, ce programme vous demandera combien de variables souhaiter vous mettre dans en ligne dans le tableau de karnaugh

Dans l'exemple ci-dessous par exemple c'est égal à 2

Il suffira d'appeler la fonction ``karnaugh_table`` pour executer le programme

Voila un exemple de output du fonction
    
    ab     00 | 01 | 11 | 10
    cd   || ===================
    00   || 1  | 0  | 1  | 1
    01   || 1  | 1  | 1  | 1
    11   || 1  | 1  | 1  | 1
    10   || 0  | 0  | 1  | 1


