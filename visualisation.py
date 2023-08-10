# Librairies externes
import matplotlib.pyplot as plt
from copy import deepcopy

# Librairies internes
from cle_molette import (
    obtenir_vecteurs_coordonnees,
    calculer_coordonnees,
)

from image import (
    image_creer,
    trouver_contours,
)

from tracer import (
    calculer_coordonnees_droite_horizontale,
    calculer_coordonnees_droite_verticale,
    calculer_coordonnees_arc,
)

from transformations import (
    appliquer_facteur_echelle,
    appliquer_translation,
    appliquer_rotation,
)

# Constantes externes
from math import pi as PI

# Constantes internes
__NB_SEGMENTS = 300  # Résolution du tracé du contour
__FACTEUR_ECHELLE = 0.5  # Facteur d'échelle à appliquer
__DECALAGE_X = 75  # Décalage en x
__DECALAGE_Y = 75  # Décalage en y
__PIVOT_X = 0  # Coordonnée x du centre de rotation
__PIVOT_Y = 0  # Coordonnée y du centre de rotation
__ANGLE_ROTATION = -PI / 2  # Angle de rotation de la clé

__LARGEUR_MANCHE = 30  # Largeur du manche de la clé
__LARGEUR_OUVERTURE = 30  # Largeur de l'ouverture de la tête de la clé
__LARGEUR_TETE = 90  # Largeur de la tête de la clé
__LONGUEUR_TOTALE = 300  # Longueur totale de la clé

# Calculer les coordonnées des coins
__COORDS_CONTOUR = calculer_coordonnees(__LARGEUR_MANCHE,
                                        __LARGEUR_OUVERTURE,
                                        __LARGEUR_TETE,
                                        __LONGUEUR_TOTALE)

# Extraire les coordonnées des coins
__XM1, __YM1 = __COORDS_CONTOUR[0]
__XM2, __YM2 = __COORDS_CONTOUR[1]
__XM3, __YM3 = __COORDS_CONTOUR[2]
__XM4, __YM4 = __COORDS_CONTOUR[3]
__XO1, __YO1 = __COORDS_CONTOUR[4]
__XO2, __YO2 = __COORDS_CONTOUR[5]
__XO3, __YO3 = __COORDS_CONTOUR[6]
__XO4, __YO4 = __COORDS_CONTOUR[7]


def generer_contour(est_manche=False,
                    est_ouverture=False,
                    est_tete=False):
    """
    Génère le contour pour la clé utilisée dans les tests visuels.

    Arguments:
        est_manche (bool): Tracer le manche ou non.
        est_ouverture (bool): Tracer l'ouverture de la tête ou non.
        est_tete (bool): Tracer les parties circulaires de la tête ou non.

    Retourne:
        (list): Liste de tuples-coordonnées du contour de la clé.
    """

    coords_contour = deepcopy(__COORDS_CONTOUR)

    # Contour du manche
    if est_manche:
        coords_contour.extend(calculer_coordonnees_droite_verticale(__YM2, __YM3, __XM2, __NB_SEGMENTS))
        coords_contour.extend(calculer_coordonnees_droite_horizontale(__XM3, __XM4, __YM3, __NB_SEGMENTS))
        coords_contour.extend(calculer_coordonnees_droite_horizontale(__XM1, __XM2, __YM1, __NB_SEGMENTS))

    # Ouverture de la tête
    if est_ouverture:
        coords_contour.extend(calculer_coordonnees_droite_verticale(__YO2, __YO3, __XO2, __NB_SEGMENTS))
        coords_contour.extend(calculer_coordonnees_droite_horizontale(__XO3, __XO4, __YO3, __NB_SEGMENTS))
        coords_contour.extend(calculer_coordonnees_droite_horizontale(__XO1, __XO2, __YO1, __NB_SEGMENTS))

    # Tête
    if est_tete:
        coords_contour.extend(calculer_coordonnees_arc(__XO2, 0, __XM4, __YM4, __XO4, __YO4, __NB_SEGMENTS))
        coords_contour.extend(calculer_coordonnees_arc(__XO2, 0, __XM1, __YM1, __XO1, __YO1, __NB_SEGMENTS))

    return coords_contour


def visualiser_tracage_et_transformations(est_manche=True,
                                          est_ouverture=True,
                                          est_tete=False,
                                          est_rotation=False,
                                          est_translation=False,
                                          est_facteur_echelle=False):
    """
    Test visuel pour le traçage et les transformations.

    Arguments:
        est_manche (bool): Tracer le manche ou non.
        est_ouverture (bool): Tracer l'ouverture de la tête ou non.
        est_tete (bool): Tracer les parties circulaires de la tête ou non.
        est_rotation (bool): Appliquer une rotation ou non.
        est_translation (bool): Appliquer un déplacement ou non.
        est_facteur_echelle (bool): Appliquer un déplacement ou non.

    Retourne:
        Rien.
    """

    # Générer les contours
    coords_contour = generer_contour(est_manche=est_manche,
                                     est_ouverture=est_ouverture,
                                     est_tete=est_tete)

    # Extraire les vecteurs x et y des coordonnées des composants originaux
    coords_x, coords_y = obtenir_vecteurs_coordonnees(coords_contour)

    # Initialiser les coordonnées transformées
    coords_contour_transforme = deepcopy(coords_contour)

    # Appliquer la rotation
    if est_rotation:
        coords_contour_transforme = \
            appliquer_rotation(coords_contour_transforme, __ANGLE_ROTATION, __PIVOT_X, __PIVOT_Y)

    # Appliquer les déplacements
    if est_translation:
        coords_contour_transforme = appliquer_translation(coords_contour_transforme, __DECALAGE_X, __DECALAGE_Y)

    # Appliquer la mise à l'échelle
    if est_facteur_echelle:
        coords_contour_transforme = appliquer_facteur_echelle(coords_contour_transforme, __FACTEUR_ECHELLE)

    # Créer la figure et récupérer les axes
    fig, ax = plt.subplots()

    # Remplir l'aire de la clé
    aire_tete = plt.Circle((__XO2, 0), radius=__LARGEUR_TETE / 2, color='gray', alpha=0.5)
    aire_manche = plt.Rectangle((__XM2, __YM2), __XM1 - __XM2, __YM3 - __YM2, color='gray', alpha=0.5)
    aire_ouverture = plt.Rectangle((__XO2, __YO2), __LARGEUR_TETE / 2, __LARGEUR_OUVERTURE, color='w')

    ax.add_patch(aire_tete)
    ax.add_patch(aire_manche)
    ax.add_patch(aire_ouverture)

    # Tracer le contour de la clé originale
    ax.scatter(coords_x, coords_y, s=5, color='k')

    # Tracer le contour de la clé transformée
    if est_rotation or est_translation or est_facteur_echelle:
        # Extraire les vecteurs x et y des coordonnées des composants transformés
        coords_x_transforme, coords_y_transforme = obtenir_vecteurs_coordonnees(coords_contour_transforme)

        # Tracer le contour de la clé transformée
        ax.scatter(coords_x_transforme, coords_y_transforme, s=1, color='b')

    # Centrer la clé originale
    ax.set_ylim(-__LONGUEUR_TOTALE / 2, __LONGUEUR_TOTALE / 2)

    # Ajouter une grille
    ax.grid(True, linestyle='--', color='k', alpha=0.5)

    # Nommer les axes
    ax.set_xlabel('Coordonnée x')
    ax.set_ylabel('Coordonnée y')

    # Afficher
    plt.show()


def visualiser_detection_contours():
    # Générer les contours d'une première clé
    coords_contours = generer_contour(est_manche=True,
                                      est_ouverture=True,
                                      est_tete=True)

    # Propriétés des transformations à appliquer pour la deuxième clé
    translation_x = 0
    translation_y = 100
    facteur_echelle = 0.5

    # Générer les contours de la deuxième clé
    coords_contours_2 = deepcopy(coords_contours)
    coords_contours_2 = appliquer_translation(coords_contours_2, translation_x, translation_y)
    coords_contours_2 = appliquer_facteur_echelle(coords_contours_2, facteur_echelle)

    # Combiner les deux contours
    coords_contours.extend(coords_contours_2)

    # Dimensions des images à générer
    hauteur_image = 320
    largeur_image = 320

    # Générer la première image
    image_1 = image_creer(coords_contours, hauteur_image, largeur_image)

    # Extraire les vecteurs-coordonnées
    x_contour_1, y_contour_1 = obtenir_vecteurs_coordonnees(coords_contours)

    # Créer les graphes
    fig, (ax1, ax2) = plt.subplots(1, 2)

    # Tracer les contours originaux
    ax1.scatter(x_contour_1, y_contour_1, s=1, color='k')

    # Dimensionner la figure
    fig.set_figwidth(10)
    fig.set_figheight(5)

    # Ajuster les sous-graphes
    plt.tight_layout()

    # Extraire les coordonnées des contours des objets de la première image
    taille_voisinage = 1
    coords_contours_trouves = trouver_contours(image_1, taille_voisinage)

    # Afficher les contours trouvés
    legende = []
    no_objet = 1
    for coords in coords_contours_trouves:
        # Extraire les vecteurs-coordonnées de l'objet courant
        x_contour_trouve, y_contour_trouve = obtenir_vecteurs_coordonnees(coords)

        # Trace rle contour de l'objet courant
        ax2.scatter(y_contour_trouve, x_contour_trouve, s=1)

        # Ajouter l'étiquette correspondant pour la légende
        legende.append(f'Objet no.{no_objet}')

        no_objet += 1

    # Afficher la légende
    ax2.legend(legende, loc='lower center')

    # Ajuster les axes
    ax1.set_xlim((-170, 170))
    ax1.set_ylim((-170, 170))
    ax2.set_xlim((0, 320))
    ax2.set_ylim((0, 320))

    # Cacher les axes
    ax1.axis(False)
    ax2.axis(False)

    # Ajouter des titres
    ax1.set_title('Objets', y=1.0, pad=-10)
    ax2.set_title('Contours détectés', y=1.0, pad=-10)

    # Afficher
    plt.show()


if __name__ == '__main__':

    visualiser_detection_contours()


    visualiser_tracage_et_transformations(est_manche=False,
                                          est_ouverture=False,
                                          est_tete=False,
                                          est_rotation=False,
                                          est_translation=False,
                                          est_facteur_echelle=False)
