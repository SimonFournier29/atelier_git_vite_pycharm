def calculer_coodonnees(wmanche, wouverture, wtete, ltotale):
  pm1 = (int(ltotale / 2 -wtete / 2 - ((wtete**2 - wmanche**2)**0.5)/ 2), int(-wmanche / 2))
  pm2 = (int(-ltotale / 2), int(-wmanche / 2))
  pm3 = (int(-ltotale / 2), int(wmanche / 2))
  pm4 = (int(ltotale / 2 -wtete / 2 - ((wtete**2 - wmanche**2)**0.5)/ 2), int(wmanche / 2))
  po1 = (int(ltotale / 2 -wtete / 2 + ((wtete**2 - wouverture**2)**0.5)/2), int(-wouverture / 2))
  po2 = (int(ltotale /2 - wtete / 2), int(-wouverture / 2))
  po3 = (int(ltotale /2 - wtete / 2), int(wouverture / 2))
  po4 = (int(ltotale / 2 - wtete / 2 + ((wtete**2 - wouverture**2)**0.5)/2), int(wouverture / 2))
  coordonnees = [pm1, pm2, pm3, pm4, po1, po2, po3, po4]
  return coordonnees

def obtenir_vecteur_coordonnees(coordonnees):
  vals_x = []
  vals_y = []

  for x, y in coordonnees:
    vals_x.append(x)
    vals_y.append(y)

  lx = vals_x
  ly = vals_y

  return lx, ly

