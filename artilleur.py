from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtCore import QPoint
from PySide6.QtGui import QPixmap
from random import randint
import math


class Artilleur(QMainWindow):

    def __init__(self):
        super().__init__()


class Jeu:

    HAUTEUR = 600
    LARGEUR = 800

    def __init__(self, vue: Artilleur):
        self.en_tir = False
        self.termine = False
        self.canon = Canon()
        self.vue = vue
        self.nb_essais = 0
        self.cible = Cible()
        self.projectile = None
        self.angle_precedent = 0
        self.puissance_precedente = 0

    def feu(self, angle_deg: int, puissance: int):
        pass

    def boucle_jeu(self):

        if self.termine:
            self.dessiner_ecran_fin()
            return

        if self.en_tir:
            pass
        else:
            pass

        # Réassigner le canevas sur le QLabel


    def dessiner(self, canevas: QPixmap):
        pass

    def dessiner_ecran_fin(self):
        pass


# <a href="https://www.freepik.com/free-psd/ramadan-cannon_24588035.htm#query=cannon&position=22&from_view=search&track=sph">Image by qalebstudio</a> on Freepik
class Canon:

    def __init__(self):
        pass

    def dessiner(self, canevas: QPixmap):
        pass


class Projectile:

    def __init__(self, position: QPoint, angle_rad: float, puissance: int):
        pass

    def avancer(self):
        pass

    def verifier_collision(self, position_cible: QPoint):
        pass

    def dessiner(self, canevas: QPixmap):
        pass


class Cible:

    def __init__(self):
        pass

    def dessiner(self, canevas: QPixmap):
        pass


class Utilitaires:

    @staticmethod
    def convertir_coord(coord: QPoint) -> QPoint:
        return QPoint(coord.x(), Jeu.HAUTEUR - coord.y())

    @staticmethod
    def generer_position_depart(x) -> QPoint():
        hauteur = randint(35, 350)
        return QPoint(x, hauteur)

    @staticmethod
    def print_position(nom: str, position: QPoint):
        print(nom + f": ({position.x()}, {position.y()})")


app = QApplication()
artilleur = Artilleur()
artilleur.show()
app.exec()