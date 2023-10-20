# Artilleur
## Dessin sur canevas

Vous devrez créer un jeu d'artilleur. Le but du jeu est d'essayer de toucher la cible avec un canon.

## Critères d'évaluation

Ce TP compte pour 20% de la note finale.

La répartition des critères d'évaluation est comme suit:  

- 6% pour le fonctionnement de l'interface utilisateur et le respect de la disposition.    
- 10% pour le fonctionnement du jeu 
- 4% pour le respect des normes Python et la documentation

### Interface
1) L'interface utilisateur sera composée d'une aire de jeu et d'une zone pour les contrôles
2) La fenêtre devra se nommer "Artilleur"

![Interface utilisateur](/images/capture.png "Interface Utilisateur")

### Aire de de jeu
1) L'aire de jeu sera d'une grandeur de 800*600
2) C'est le canevas à utiliser pour dessiner
3) La couleur devra être le bleu

### Zone de contrôles
1) Cette zone comprendra les widgets permettant au joueur de sélectionner l'angle et la puissance de tir
2) L'angle de tir
   1) L'angle de tir sera affiché par un QLabel
   2) Un QSlider horizontal sera utilisé pour choisir l'angle de tir
   3) L'angle minimum est de 0, maximum de 75 et par défaut 30
   4) Tout changement de la valeur devra se refléter dans le QLabel
3) Puissance de tir
   1) La puissance de tir sera affiché par un QLabel
   2) Un QSlider horizontal sera utilisé pour choisir la puissance de tir
   3) La puissance minimum est de 50, maximum de 150 et par défaut 50  
   4) Tout changement de la valeur devra se refléter dans le QLabel
4) Le bouton de tir servira à faire feu
   1) La couleur du bouton devra être rouge

### Jeu
La classe Jeu représente l'état du jeu et sert à effectuer la logique générale du jeu.
- La méthode boucle_jeu()
  - Sert à appeler les diverses méthodes selon l'état du jeu (en tir ou terminé)
  - Devra être déclenché par un QTimer. 
  - Elle va rouler jusqu'à ce l'application soit fermée.
- La méthode feu()
  - Permet de changer l'état à "en tir"
  - Incrémenter le nombre d'essais
  - Créer le Projectile
  - Mettre à jour l'angle et la puissance de tir précédente
- La méthode dessiner(canevas: QPixmap) sert à dessiner les diverses informations nécessaires
  - Le nombre d'essais
    - La grandeur de la police du texte doit être de 15pts
    - Doit être situé à 50 pixels du haut de l'écran
  - L'angle en degré du tir précédent
    - La grandeur de la police du texte doit être de 15pts
    - Doit être situé à 75 pixels du haut de l'écran
  - La puissance du tir précédent
    - La grandeur de la police du texte doit être de 15pts
    - Doit être situé à 100 pixels du haut de l'écran
- La méthode dessiner_ecran_fin(canevas: QPixmap)
  - Dessiner l'écran de fin de jeu

### Canon
1) Le canon sera à une distance de 10 pixels du côté gauche de l'aire de jeu
2) La hauteur de départ du canon sera aléatoire (voir Utilitaires.generer_position_depart(x))
3) Le canon sera représenté par l'image canon.jpg d'une grandeur de 50*50
4) La méthode dessiner(canevas: QPixmap) sert à dessiner le canon

### Cible
1) La cible se trouvera à 50 pixel du côté droit de l'aire de jeu
2) La cible sera représenté par un rectangle d'une largeur de 25 et d'une hauteur de 75
3) La hauteur de départ de la cible sera aléatoire (voir Utilitaires.generer_position_depart(x))

### Projectile
1) Le projectile sera créé au moment de faire feu
2) Il devra être créé juste à la droite du canon
3) La méthode avancer() sert à calculer la position du projectile après avoir avancé de 20 pixels
   1) Pour calculer la position, vous devrez utiliser une formule de balistique de base 
   [Trajectoire d'un projectile](https://fr.wikipedia.org/wiki/Trajectoire_d%27un_projectile#%C3%89quations_horaires_et_cart%C3%A9siennes)

### Tir
Lors du tir, le projectile devra vérifier s'il fait collision avec la cible ou sort de l'écran.
- S'il fait une collision avec la cible, le joueur a gagné.
  - Un écran de fin de jeu devra afficher "Bravo" et le nombre d'essais nécessaire. 
- Effectuer un tir incrémentera le nombre d'essais. 
- Si le projectile sort de l'écran, on devra changer l'état pour ne plus être en tir.

### Coordonnées
Pour les positions du canon, de la cible et du projectile, il est conseillé de les considérer dans un axe standard 
(x de bas en haut, y de gauche vers la droite) et d'utiliser l'utilitaire au moment de dessiner pour convertir
dans les coordonnées de l'écran (x de haut vers le bas)
Pour les coordonnées, utilisez un QPoint.




