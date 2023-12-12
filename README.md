# Présentation Technique du Projet Snake
Bonjour tout le monde ! Je suis ravi de partager avec vous quelques détails techniques sur le projet Snake que j'ai développé lors d'un atelier à une école d'informatique. Plongeons dans les aspects techniques clés du code Python.

## Gestion des Collisions
L'une des parties délicates de ce projet était la gestion des collisions. J'ai implémenté des mécanismes pour détecter les collisions avec les bords de l'écran, la nourriture, et le corps du serpent. La condition if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290 permet de détecter les collisions avec les bords, tandis que if head.distance(food) < 20 gère les collisions avec la nourriture. Enfin, la vérification de la collision avec le corps du serpent est réalisée dans la boucle for segment in segments.

## Structure du Code
Le code est structuré de manière à rendre la gestion du serpent modulaire. J'utilise des fonctions distinctes pour le déplacement (move()), les différentes directions (go_up(), go_down(), go_left(), go_right()), et la mise à jour de l'écran (wn.update()). Les segments du serpent sont gérés via une liste (segments), simplifiant l'ajout et le retrait des segments lorsqu'il grandit ou en cas de collision.

## Gestion du Score
La gestion du score est une composante essentielle. À chaque collision avec la nourriture, le score augmente de 10 points. Le meilleur score (high_score) est également mis à jour en conséquence. La partie du code if score > high_score garantit que le meilleur score est toujours à jour, et ces informations sont affichées à l'écran grâce à pen.write().

## Imports et Utilisation de Turtle
Le module turtle est utilisé pour créer l'interface graphique du jeu. J'ai importé les fonctions nécessaires, telles que Turtle(), Screen(), et time pour gérer les délais. Les contrôles clavier sont gérés par wn.listen() et wn.onkeypress(). Les classes Turtle sont utilisées pour représenter la tête, la nourriture, les segments du serpent, et le panneau d'affichage du score.

## Optimisation de la Vitesse
Afin d'ajuster la vitesse du jeu, j'ai utilisé une variable delay qui régule le temps d'attente entre chaque mouvement du serpent. En fonction de certains événements, comme la collision avec la nourriture, le délai est ajusté pour rendre le jeu plus difficile à mesure que le serpent grandit.

## Image du jeu 

![image](https://github.com/MathisCastell/Jeu_Snake/assets/148212506/a0e5e1f3-d6f4-4c1b-b5bf-a584d3a8f6f4)
