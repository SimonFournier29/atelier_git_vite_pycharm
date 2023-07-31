from cle_molette import calculer_coordonnees
from cle_molette import obtenir_vecteurs_coordonnees
def test_calculer_coordonnees():
    assert calculer_coordonnees(30, 30, 50, 200) == [(55, -15), (-100, -15), (-100, 15), (55, 15), (95, -15), (75, -15), (75, 15), (95, 15)]

def test_obtenir_vecteur_coordonnees():
    assert obtenir_vecteurs_coordonnees([(55, -15),(-100, -15),(-100, 15),(55, 15),(95, -15),(75, -15),(75, 15),(95, 15)]) == ([55, -100, -100, 55, 95, 75, 75, 95], [-15, -15, 15, 15, -15, -15, 15, 15])