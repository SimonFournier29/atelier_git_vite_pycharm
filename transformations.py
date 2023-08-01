import math
import numpy as np
def appliquer_rotation(coordonnees, angle_rad, xp, yp):

  angle_x = math.cos(angle_rad)
  angle_y = math.sin(angle_rad)
  #matrice modelée selon MEC129
  matrice_rot = np.array([[angle_x, -angle_y], [angle_y, angle_x]])

  pivot_a_origine = np.array(coordonnees) - np.array([xp, yp])
  coordonnees_rot = np.dot(pivot_a_origine, matrice_rot)
  coordonnees_rot += np.array([xp, yp])
  resultat_rot = [tuple(i) for i in coordonnees_rot]
  return resultat_rot

def appliquer_translation(coordonnees, dx, dy):
  matrice_trans = np.array([[dx, dy]])
  coordonnees_trans = np.array(coordonnees) + matrice_trans
  resultat_trans = [tuple(i) for i in coordonnees_trans]
  return resultat_trans

def appliquer_facteur_echelle(coordonnees, k):
  matrice_scale = np.array([[k, 0], [0, k]])
  coordonnees_scale = np.dot(np.array(coordonnees), matrice_scale)
  resultat_scale = [tuple(i) for i in coordonnees_scale]
  return resultat_scale