import numpy as np
from scipy.ndimage import label

def image_creer(coordonnees, hauteur, largeur):
    # Créer une image vide
    image = np.ones((hauteur, largeur))

    # Trouver les coordonnées maximales pour déterminer la taille de l'objet
    max_x, max_y = np.max(coordonnees, axis=0)
    min_x, min_y = np.min(coordonnees, axis=0)

    # Calculer le décalage pour centrer l'objet dans l'image
    offset_x = (largeur - max_x) // 2
    offset_y = (hauteur - max_y) // 2
    vrai_offset_y = hauteur - offset_y

    # Dessiner l'objet en utilisant les coordonnées fournies
    for coord in coordonnees:
        x, y = coord
        image[vrai_offset_y - (y+1), offset_x + x] = 0 # Selon l'ordre des offsets, l'orientation de l'image change

    return image

import numpy as np

def trouver_contours(image, taille_voisinage=1):
    hauteur, largeur = image.shape
    visitees = np.zeros_like(image, dtype=np.bool)
    contours = []

    directions = [(i, j) for i in range(-taille_voisinage, taille_voisinage + 1)
                         for j in range(-taille_voisinage, taille_voisinage + 1)
                         if (i, j) != (0, 0)]

    def est_valide(x, y):
        return 0 <= x < largeur and 0 <= y < hauteur and not visitees[y, x] and image[y, x] == 0

    for i in range(hauteur):
        for j in range(largeur):
            if est_valide(j, i):
                contour = []
                pile = [(j, i)]
                while pile:
                    x, y = pile.pop()
                    visitees[y, x] = True
                    contour.append((x, y))
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if est_valide(nx, ny):
                            pile.append((nx, ny))
                            visitees[ny, nx] = True
                contours.append(contour)
    return contours


def analyser_image(image):
    # Étiquetage des régions connexes dans l'image binaire
    labeled_image, num_labels = label(image)

    # Initialiser la liste pour stocker les informations sur les objets détectés
    info_objets = []

    for i in range(1, num_labels + 1):
        # Obtenir les coordonnées des points de l'objet (région) étiqueté
        indice_objet = np.argwhere(labeled_image == i)

        # Calculer les coordonnées min et max pour le rectangle englobant
        y_min, x_min = indice_objet.min(axis=0)
        y_max, x_max = indice_objet.max(axis=0)

        # Calculer la hauteur et la largeur du rectangle englobant
        hauteur = y_max - y_min + 1
        largeur = x_max - x_min + 1

        # Calculer le centre du rectangle englobant
        center_x = x_min + largeur // 2
        center_y = y_min + hauteur // 2

        # Ajouter les informations sur l'objet à la liste
        dictionnaire = {
            'coords': indice_objet.tolist(),  # Coordonnées des points de l'objet
            'x_min': x_min,
            'x_max': x_max,
            'y_min': y_min,
            'y_max': y_max,
            'hauteur': hauteur,
            'largeur': largeur,
            'angle': 0  # Pour cette approche, l'angle sera toujours 0 car nous n'utilisons pas cv2.minAreaRect
        }
        info_objets.append(dictionnaire)

    return info_objets


