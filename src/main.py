
from matplotlib import pyplot as plt
from matplotlib_venn import venn2

def main():

    print("Union")
    print(union_conjuntos([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
    venn2(([1, 2, 3, 4, 5], union_conjuntos([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])))
    plt.show()

    """print("Interseccion")
    print(interseccion_conjuntos([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
    print("Diferencia")
    print(diferencia_conjuntos([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
    print("Complemento")
    print(complemento_conjuntos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [3, 4, 5, 6, 7]))
    print("Combinacion")
    print(combinacion_conjuntos([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))"""

def interseccion_conjuntos(conjunto1, conjunto2):
    conjunto_interseccion = []
    for elemento in conjunto1:
        if elemento in conjunto2:
            conjunto_interseccion.append(elemento)
    return conjunto_interseccion


def union_conjuntos(conjunto1, conjunto2):
    conjunto_union = []
    for elemento in conjunto1:
        conjunto_union.append(elemento)
    for elemento in conjunto2:
        if elemento not in conjunto_union:
            conjunto_union.append(elemento)
    return conjunto_union

def diferencia_conjuntos(conjunto1, conjunto2):
    conjunto_diferencia = []
    for elemento in conjunto1:
        if elemento not in conjunto2:
            conjunto_diferencia.append(elemento)
    return conjunto_diferencia

def complemento_conjuntos(conjunto_universal, conjunto):
    conjunto_complemento = []
    for elemento in conjunto_universal:
        if elemento not in conjunto:
            conjunto_complemento.append(elemento)
    return conjunto_complemento

def combinacion_conjuntos(conjunto1, conjunto2):
    conjunto_combinacion = []
    for elemento in conjunto1:
        conjunto_combinacion.append(elemento)
    for elemento in conjunto2:
        conjunto_combinacion.append(elemento)
    return conjunto_combinacion

main()
