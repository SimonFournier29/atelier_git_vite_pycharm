def calculer_coordonnees(w_manche, w_ouverture, w_tete, l_totale):
  #coordonnés manche
  pm1 = (int(l_totale / 2 -w_tete / 2 - ((w_tete**2 - w_manche**2)**0.5)/ 2), int(-w_manche / 2))
  pm2 = (int(-l_totale / 2), int(-w_manche / 2))
  pm3 = (int(-l_totale / 2), int(w_manche / 2))
  pm4 = (int(l_totale / 2 -w_tete / 2 - ((w_tete**2 - w_manche**2)**0.5)/ 2), int(w_manche / 2))
  #coordonnés outil.
  po1 = (int(l_totale / 2 -w_tete / 2 + ((w_tete**2 - w_ouverture**2)**0.5)/2), int(-w_ouverture / 2))
  po2 = (int(l_totale /2 - w_tete / 2), int(-w_ouverture / 2))
  po3 = (int(l_totale /2 - w_tete / 2), int(w_ouverture / 2))
  po4 = (int(l_totale / 2 - w_tete / 2 + ((w_tete**2 - w_ouverture**2)**0.5)/2), int(w_ouverture / 2))
  coordonnees = [pm1, pm2, pm3, pm4, po1, po2, po3, po4]

  return coordonnees

def obtenir_vecteurs_coordonnees(coordonnees):
  vals_x = []
  vals_y = []
#séparer les valeurs x et y dans leur liste respective
  for x, y in coordonnees:
    vals_x.append(x)
    vals_y.append(y)

  lx = vals_x
  ly = vals_y

  return lx, ly

