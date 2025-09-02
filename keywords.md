# Mots clés chi fou mi
Les développeurs ont développé cette bibliothèque de mots-clés ROBOT FRAMEWORK à l'attention des testeurs, afin de manipuler les objets et le moteur du jeu sans passer par le webservice.

## Reference de bibliothèque
La bibliothèque peut être utilisée en la plaçant dans la partie **settings** d'une test suite de la façon suivante

```
*** settings ***
Library           test_library/ChiFouMiKeyWords.py
```

## mot clé ***clear game***
Pas de paramètres. Remet à zéro l'ensemble des défis et des joueurs contenus dans le système du jeu

***usage:***
```
clear game
```

## mot clé ***create player***
Crée un nouveau joueur dans le système du jeu

2 paramètres:
- Le pseudo du joueur
- L'email du joueur

Renvoie:
- L'ID unique du joueur créé en jeu


***usage:***
```
${ID}=  create player Vincent vincentraout27@gmail.com
```

## mot clé: ***check player exists in system***
Vérifie l'existence d'un joueur dans le système du jeu

1 paramètres:
- un ID unique de joueur

Renvoie:
- True ou False

***usage:***
```
${Existence}=  check player exists in system  aaa01bcfe5cc75fb
```

## mot clé: ***get player characteristic***
Ramène une caractéristique d'un joueur existant dans le système du jeu

2 paramètres:
- un ID unique de joueur
- le nom d'une caractéristique de joueur parmi les suivantes: *name, email, handsignal, ranking*

Renvoie:
- La caractériqtique voulue

***usage:***
```
${handSignal}=  get player characteristic  aaa01bcfe5cc75fb  handSignal
```
## mot clé: ***player plays***
Permet à un joueur existant dans le système du jeu de jouer un signe de la main

2 paramètres:
- un ID unique de joueur
- un signal de la main parmi les suivantes: *Paper, Stone, Scissors*

***usage:***
```
player plays  aaa01bcfe5cc75fb  Stone
```
## mot clé: ***player initiates challenge in rounds***
Permet à un joueur existant dans le système du jeu de lancer un challenge en précisant le nombre de manches

2 paramètres:
- un ID unique de joueur
- le nombre de rounds du challenge à créer

Renvoie:
- un ID unique de challenge

***usage:***
```
${AB_CHALLENGE}=  player initiates challenge in rounds   aaa01bcfe5cc75fb  3
```

## mot clé: ***player joins challenge***
Permet à un joueur existant dans le système du jeu de répondre à un challenge existant dans le système du jeu

2 paramètres:
- un ID unique de joueur
- un ID unique de challenge

***usage:***
```
Player Joins Challenge  aaa01bcfe5cc75fb  a314f1592e
```

## mot clé: ***player cancels challenge***
Permet à un joueur d'annuler un challenge existant dans le système du jeu

2 paramètres:
- un ID unique de joueur
- un ID unique de challenge

***usage:***
```
player cancels challenge  aaa01bcfe5cc75fb  a314f1592e
```
## mot clé: ***get challenge characteristic***
Ramène une caractéristique d'un challenge existant dans le système du jeu

2 paramètres:
- un ID unique de challenge
- le nom d'une caractéristique de challenge parmi les suivantes: *champion, challenger, winner, status, currentRound*

Renvoie:
- La caractériqtique voulue

***usage:***
```
${winner}=  get challenge characteristic  a314f1592e  winner
```
## mot clé: ***play a round of***
Permet de jouer une manche d'un challenge existant dans le système de jeu

1 paramètres:
- un ID unique de challenge

***usage:***
```
play a round of  a314f1592e
```