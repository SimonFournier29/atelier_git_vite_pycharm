# Librairies externes
from deepdiff import DeepDiff
import numpy as np

# Libraries internes
from image import analyser_image
from image import trouver_contours

def test_trouver_contours():
    # L'image attendue
    image = np.array([[0, 0, 1, 0, 0],
                      [0, 0, 1, 0, 0],
                      [1, 1, 1, 1, 1],
                      [1, 0, 0, 0, 1],
                      [1, 0, 0, 0, 1]])

    # La taille du voisinage
    taille_voisinage = 1

    # Extraire les contours
    contours_obtenus = trouver_contours(image, taille_voisinage)

    # Les contours attendus
    contours_attendus = [[(1, 1), (0, 0), (0, 1), (1, 0)],
                         [(1, 4), (0, 3), (1, 3), (0, 4)],
                         [(3, 1), (4, 2), (4, 3), (3, 2), (3, 3), (4, 1)]]

    # Transformer en ensembles
    contours_obtenus = [set(c) for c in contours_obtenus]
    contours_attendus = [set(c) for c in contours_attendus]

    # Valider que le bon nombre de contours furent trouvés
    assert len(contours_attendus) == len(contours_attendus) == 3

    # Valider les contours obtenus
    assert all([c in contours_attendus for c in contours_obtenus])


def test_analyser_image():
    # L'image de test
    image = np.array([[1, 0, 1, 0, 1],
                      [0, 1, 1, 1, 0],
                      [1, 1, 1, 1, 1],
                      [1, 1, 0, 1, 1],
                      [1, 1, 0, 1, 1]])

    # Les résultats attendus
    resultats_attendus = [{'coords': [(1, 0), (0, 1)],
                           'x_min': 0,
                           'x_max': 1,
                           'y_min': 0,
                           'y_max': 1,
                           'hauteur': 2,
                           'largeur': 2,
                           'angle': -0.7853981633974483},
                          {'coords': [(1, 4), (0, 3)],
                           'x_min': 0,
                           'x_max': 1,
                           'y_min': 3,
                           'y_max': 4,
                           'hauteur': 2,
                           'largeur': 2,
                           'angle': 0.7853981633974483},
                          {'coords': [(3, 2), (4, 2)],
                           'x_min': 3,
                           'x_max': 4,
                           'y_min': 2,
                           'y_max': 2,
                           'hauteur': 2,
                           'largeur': 1,
                           'angle': 0.0}]

    # Analyser l'image
    resultats_obtenus = analyser_image(image)

    assert not DeepDiff(resultats_obtenus, resultats_attendus, ignore_order=True, significant_digits=6)
