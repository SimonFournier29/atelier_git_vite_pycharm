from transformations import appliquer_rotation
from transformations import appliquer_translation
from transformations import appliquer_facteur_echelle
import math
def test_appliquer_rotation():
    assert appliquer_rotation([(-1, -1), (1, 1)], math.pi/2, 0, 0) == [(-1.0, 0.9999999999999999), (1.0, -0.9999999999999999)]

def test_appliquer_translation():
    assert appliquer_translation([(-1, -1), (1, 1)], -1, 2) == [(-2, 1), (0, 3)]

def test_appliquer_facteur_echelle():
    assert appliquer_facteur_echelle([(-1, -1), (1, 1)], 2) == [(-2, -2), (2, 2)]



