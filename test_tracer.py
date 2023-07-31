from tracer import calculer_coordonnees_droite_horizontale
from tracer import calculer_coordonnees_droite_verticale
from tracer import calculer_coordonnees_arc
def test_calculer_coordonnees_droite_horizontale():
    assert calculer_coordonnees_droite_horizontale(1, 6, 1, 5) == [(1.0, 1), (2.0, 1), (3.0, 1), (4.0, 1), (5.0, 1), (6.0, 1)]

def test_calculer_coodonnees_droite_verticale():
    assert calculer_coordonnees_droite_verticale(1, 6, 1, 5) == [(1, 1.0), (1, 2.0), (1, 3.0), (1, 4.0), (1, 5.0), (1, 6.0)]

def test_calculer_coordonnees_arc():
    assert calculer_coordonnees_arc(0, 0, -1, 0, 1, 0,4) == [(-1.0, 1.2246467991473532e-16), (-0.7071067811865475, 0.7071067811865476), (6.123233995736766e-17, 1.0), (0.7071067811865476, 0.7071067811865476), (1.0, 0.0)]
