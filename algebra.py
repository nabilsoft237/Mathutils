import numpy as np

def resourdre_equation(a, b, c):
    """resourdre une equation lineaire"""
    return (-b + np.sqrt(b**2 -  4*a*c)) / (2*a)

def determinant(matrice):
    """calcul le determnant d'une matrice"""
    return np.linalg.det(matrice)   