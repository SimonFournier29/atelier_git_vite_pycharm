import numpy as np
def calculer_distance_points(x1, y1, x2, y2):
  distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
  return distance

def obtenir_x_y_max(coordonnees):
  max_x, max_y = 0, 0
#sépare les valeurs x et y pour les évaluer séparément
  for x, y in coordonnees:
    if x > max_x:
      max_x = x
    if y > max_y:
      max_y = y
  return max_x, max_y


def obtenir_x_y_min(coordonnees):
  min_x, min_y = np.inf, np.inf

  for x, y in coordonnees:
    if x < min_x:
      min_x = x
    if y < min_y:
      min_y = y
  return min_x, min_y