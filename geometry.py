import math

def distance(x1, y1, x2, y2):
    """calcul de la distance entre deux points"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def cercle_surface(rayon):
    """calcul la surface d'un cercle"""
    return math.pi * rayon**2