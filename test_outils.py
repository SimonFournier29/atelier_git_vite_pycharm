from outils import calculer_distance_points
from outils import obtenir_x_y_max
from outils import obtenir_x_y_min
def test_calculer_distance_points():
    assert calculer_distance_points(0, 0, 5, 12) == 13

def test_obtenir_x_y_max():
    assert obtenir_x_y_max([(-1, 2), (1, -1)]) == (1,2)

def test_obtenir_x_y_min():
    assert obtenir_x_y_min([(-1, 2), (1, -1)]) == (-1, -1)


