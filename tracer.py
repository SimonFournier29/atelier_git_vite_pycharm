def calculer_coodonnees_droite_horizontale(xa, xb, y, nbsegmentx):
  liste_points = []
  delta_x = (xb - xa)/nbsegmentx

  for i in range (0, nbsegmentx + 1, 1):
    x_inter = xa + i*delta_x
    liste_points.append((x_inter, y))
  return liste_points

def calculer_coodonnees_droite_verticale(ya, yb, x, nbsegmenty):
  liste_points = []
  delta_y = (yb - ya)/nbsegmenty

  for i in range (0, nbsegmenty + 1, 1):
    y_inter = ya + i*delta_y
    liste_points.append((x, y_inter))
  return liste_points