import math

def calculer_coordonnees_droite_horizontale(xa, xb, y, nbsegmentx):
  liste_points = []
  delta_x = (xb - xa)/nbsegmentx

  for i in range (0, nbsegmentx + 1, 1):
    x_inter = xa + i*delta_x
    liste_points.append((x_inter, y))
  return liste_points

def calculer_coordonnees_droite_verticale(ya, yb, x, nbsegmenty):
  liste_points = []
  delta_y = (yb - ya)/nbsegmenty

  for i in range (0, nbsegmenty + 1, 1):
    y_inter = ya + i*delta_y
    liste_points.append((x, y_inter))
  return liste_points

def calculer_coordonnees_arc(xc, yc, xa, ya, xb, yb, n):
  liste_points = []
  r = ((xa - xc)**2 + (ya - yc)**2)**0.5
  teta_1 = math.atan2((ya - yc), (xa - xc))
  teta_2 = math.atan2((yb - yc), (xb - xc))
  delta_teta =(teta_2 - teta_1) / n

  for i in range (0, n + 1, 1):
    x_inter = r * math.cos(teta_1 + (delta_teta * i))
    y_inter = r * math.sin(teta_1 + (delta_teta * i))
    liste_points.append((x_inter, y_inter))
  return liste_points