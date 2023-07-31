# Librairies externes
import matplotlib.pyplot as plt
from copy import deepcopy
from os import startfile

# Librairies internes
from cle_molette import obtenir_vecteurs_coordonnees
from visualisation import generer_contour
from rapport import generer_rapport
from image import analyser_image

from image import (
    image_creer,
    trouver_contours,
)

from transformations import (
    appliquer_facteur_echelle,
    appliquer_translation,
    appliquer_rotation,
)

# Constantes internes
from constantes import PI


if __name__ == '__main__':
    """
    Ceci est une procédure de test qui exécute l'ensemble de vos sous-programmes.
    """

    # Générer le contour d'une première clé
    coords_contours = generer_contour(est_manche=True,
                                      est_ouverture=True,
                                      est_tete=True)

    # Clé no.2 dérivée de la première
    coords_contours_2 = deepcopy(coords_contours)
    coords_contours_2 = appliquer_rotation(coords_contours_2, - PI / 8, 0, 0)
    coords_contours_2 = appliquer_translation(coords_contours_2, 0, 150)
    coords_contours_2 = appliquer_facteur_echelle(coords_contours_2, 0.75)

    # Clé no.3 dérivée de la première
    coords_contours_3 = deepcopy(coords_contours)
    coords_contours_3 = appliquer_rotation(coords_contours_3, PI / 8, 0, 0)
    coords_contours_3 = appliquer_translation(coords_contours_3, 100, -200)
    coords_contours_3 = appliquer_facteur_echelle(coords_contours_3, 0.3)

    # Clé no.4 dérivée de la première
    coords_contours_4 = deepcopy(coords_contours)
    coords_contours_4 = appliquer_translation(coords_contours_4, -100, 100)
    coords_contours_4 = appliquer_facteur_echelle(coords_contours_4, 0.5)

    # Combiner les contours
    coords_contours.extend(coords_contours_2)
    coords_contours.extend(coords_contours_3)
    coords_contours.extend(coords_contours_4)

    # Dimensions des images à générer
    hauteur_image = 400
    largeur_image = 400

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
    coords_contours_trouves = trouver_contours(image_1, 1)

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
    ax1.set_xlim((-largeur_image // 2, largeur_image // 2))
    ax1.set_ylim((-hauteur_image // 2, hauteur_image // 2))
    ax2.set_xlim((0, largeur_image))
    ax2.set_ylim((0, hauteur_image))

    # Cacher les axes
    ax1.axis(False)
    ax2.axis(False)

    # Ajouter des titres
    ax1.set_title('Objets', y=1.0, pad=-10)
    ax2.set_title('Contours détectés', y=1.0, pad=-10)

    # Afficher
    plt.show()

    # Extraire les résultats d'analyse
    resultats_analyse = analyser_image(image_1)

    # Générer le rapport
    generer_rapport(resultats_analyse, 'rapport_analyse.txt')

    # Ouvrir le rapport
    startfile('rapport_analyse.txt', )