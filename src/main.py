from matplotlib import pyplot as plt

def main():

    # print(union_conjuntos([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))

    # print(interseccion_conjuntos([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))

    # print(diferencia_conjuntos([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))

    # print(complemento_conjuntos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [3, 4, 5, 6, 7]))

    # print(combinacion_conjuntos([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))

    # print(cardinalidad_conjuntos([1, 2, 3, 4, 5], [3, 4, 5, 6]))

    # print(es_subconjunto([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))

    print(disjuntos_conjuntos([1, 2, 3], [4, 5, 6, 7]))

    # diagrama_venn([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])
    # diagrama_venn_interseccion([1, 2, 3, 4, 5 ], [3, 4, 5, 6, 7])
    # diagrama_venn_interseccion_3([1, 2, 3, 4, 5], [3, 4, 5, 6, 7], [5, 6, 7, 8, 9, 10])
    # diagrama_venn_diferencia([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])
    # diagrama_venn_complemento([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [3, 4, 5, 6, 7])
    # diagrama_venn_combinacion([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])
    # diagrama_venn_cardinalidad([1, 2, 3, 4, 5], [3, 4, 5, 6])
    # diagrama_venn_subconjunto([1, 2, 3], [1, 2, 3, 4, 5])
    diagrama_venn_disjuntos([1, 2, 3], [4, 5, 6, 7])


#funcion para union de conjuntos de n cantidad
def union_conjuntos(*conjuntos):
    conjunto_union = []
    for conjunto in conjuntos:
        for elemento in conjunto:
            if elemento not in conjunto_union:
                conjunto_union.append(elemento)
    return conjunto_union

#funcion para interseccion de conjuntos de n cantidad
def interseccion_conjuntos(*conjuntos):
    if len(conjuntos) < 2:
        return "Se necesitan al menos dos conjuntos para realizar una intersección."

    conjunto_interseccion = list(conjuntos[0])
    for conjunto in conjuntos[1:]:
        conjunto_interseccion = [elemento for elemento in conjunto_interseccion if elemento in conjunto]
    return conjunto_interseccion

#funcion para diferencia de conjuntos de n cantidad
def diferencia_conjuntos(*conjuntos):
    if len(conjuntos) < 2:
        return "Se necesitan al menos dos conjuntos para realizar una diferencia."

    conjunto_diferencia = list(conjuntos[0])
    for conjunto in conjuntos[1:]:
        conjunto_diferencia = [elemento for elemento in conjunto_diferencia if elemento not in conjunto]
    return conjunto_diferencia

#funcion para complemento de conjuntos de n cantidad
def complemento_conjuntos(conjunto_universo, conjunto):
    conjunto_complemento = []
    for elemento in conjunto_universo:
        if elemento not in conjunto:
            conjunto_complemento.append(elemento)
    return conjunto_complemento

#funcion para combinacion de conjuntos de n cantidad
def combinacion_conjuntos(conjunto1, conjunto2):
    conjunto_combinacion = []
    for elemento in conjunto1:
        if elemento not in conjunto_combinacion:
            conjunto_combinacion.append(elemento)
    for elemento in conjunto2:
        if elemento not in conjunto_combinacion:
            conjunto_combinacion.append(elemento)
    return conjunto_combinacion

#funcion para cardinalidad de conjuntos de n cantidad
def cardinalidad_conjuntos(*conjuntos):
    resultados = []
    for conjunto in conjuntos:
        count = 0
        for _ in conjunto:
            count += 1
        resultados.append(count)
    return resultados

#funcion para saber si un conjunto es subconjunto de otro
def es_subconjunto(conjunto1, conjunto2):
    for elemento in conjunto1:
        if elemento not in conjunto2:
            return False
    return True

#funcion para Disjuntos de n cantidad
def disjuntos_conjuntos(*conjuntos):
    for conjunto in conjuntos:
        for elemento in conjunto:
            for conjunto2 in conjuntos:
                if conjunto != conjunto2 and elemento in conjunto2:
                    return False
    return True

#funcion para pasar un array a un string
def array_to_string(array):
    string = ""
    for element in array:
        string += str(element) + " "
    return string

# venn

# funcion para mostrar un diagrama de venn con dos conjuntos (union)
def diagrama_venn(conjunto1, conjunto2):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("Diagrama de Venn")
    """
    en el scatter, en la x, mediante las comas ubicamos en donde y cuantos circulos queremos
    """
    plt.scatter(x=[0, 0.25], y=[0, 0], s=150000, color=['red', 'blue'], alpha=0.3, vmax=3, vmin=2)

    union = union_conjuntos(conjunto1, conjunto2)

    # restar el conjunto 1 de la union
    conjunto_1 = array_to_string(diferencia_conjuntos(union, conjunto2))
    # restar el conjunto 2 de la union
    conjunto_2 = array_to_string(diferencia_conjuntos(union, conjunto1))

    plt.text(x=-0.17, y=-0.03, s=conjunto_1, rotation=50, fontsize=33, fontweight='bold', color='red')
    plt.text(x=0.25, y=-0.08, s=conjunto_2, rotation=-55, fontsize=33, fontweight='bold', color='blue')
    # union entre los dos conjuntos
    plt.text(x=0.0, y=-0.15, s=union, fontsize=33, fontweight='bold', color='purple')

    plt.xlim(-0.25, 0.5)
    plt.ylim(-0.4, 0.2)
    plt.show()

# funcion para mostrar un diagrama de venn con dos conjuntos (interseccion)
def diagrama_venn_interseccion(conjunto1, conjunto2):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("Diagrama de Venn")
    """
    en el scatter, en la x, mediante las comas ubicamos en donde y cuantos circulos queremos
    """
    plt.scatter(x=[0, 0.25], y=[0, 0], s=100000, color=['red', 'blue'], alpha=0.3, vmax=3, vmin=2)

    interseccion = interseccion_conjuntos(conjunto1, conjunto2)

    # restar el conjunto 1 de la union
    conjunto_1 = array_to_string(diferencia_conjuntos(conjunto1, interseccion))
    # restar el conjunto 2 de la union
    conjunto_2 = array_to_string(diferencia_conjuntos(conjunto2, interseccion))

    plt.text(x=-0.17, y=-0.03, s=conjunto_1, rotation=50, fontsize=33, fontweight='bold', color='red')
    plt.text(x=0.25, y=-0.08, s=conjunto_2, rotation=-55, fontsize=33, fontweight='bold', color='blue')
    # interseccion entre los dos conjuntos
    plt.text(x=0.05, y=0.0, s=array_to_string(interseccion), fontsize=33, fontweight='bold', color='purple')

    plt.xlim(-0.3, 0.5)
    plt.ylim(-0.4, 0.4)
    plt.show()

# funcion para mostar un diagrama de venn con tres conjuntos (interseccion)
def diagrama_venn_interseccion_3(conjunto1, conjunto2, conjunto3):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("Diagrama de Venn")
    """
    en el scatter, en la x, mediante las comas ubicamos en donde y cuantos circulos queremos
    """
    x = [0, 0.25, 0.12]
    y = [0, 0, -0.3]

    # Mapeo de colores
    valores_de_color = [2, 3, 4]

    # Gráfico de dispersión con mapeo de colores
    plt.scatter(x=x, y=y, s=100000, c=valores_de_color, cmap='viridis', alpha=0.3, vmax=3, vmin=2)

    interseccionaux = interseccion_conjuntos(conjunto1, conjunto2)
    interseccion2aux = interseccion_conjuntos(conjunto1, conjunto3)
    interseccion3aux = interseccion_conjuntos(conjunto2, conjunto3)
    interseccion_todos = interseccion_conjuntos(conjunto1, conjunto2, conjunto3)

    interseccion = diferencia_conjuntos(interseccionaux, interseccion_todos)
    interseccion2 = diferencia_conjuntos(interseccion2aux, interseccion_todos)
    interseccion3 = diferencia_conjuntos(interseccion3aux, interseccion_todos)

    # restar el conjunto 1 de la interseccion de todos
    conjunto_1 = array_to_string(diferencia_conjuntos(conjunto1, conjunto2, conjunto3, interseccion_todos))
    # restar el conjunto 2 de la interseccion de todos
    conjunto_2 = array_to_string(diferencia_conjuntos(conjunto2, conjunto1, conjunto3, interseccion_todos))
    # restar el conjunto 3 de la interseccion de todos
    conjunto_3 = array_to_string(diferencia_conjuntos(conjunto3, conjunto2, conjunto1, interseccion_todos))

    plt.text(x=-0.17, y=-0.03, s=conjunto_1, rotation=50, fontsize=33, fontweight='bold', color='red')
    plt.text(x=0.25, y=-0.03, s=conjunto_2, rotation=-55, fontsize=33, fontweight='bold', color='blue')
    plt.text(x=0.01, y=-0.3, s=conjunto_3, fontsize=33, fontweight='bold', color='green')

    # interseccion entre los 3 conjuntos
    plt.text(x=0.08, y=-0.15, s=array_to_string(interseccion_todos), fontsize=33, fontweight='bold', color='purple')
    # nterseccion entre conjunto 1 y 2
    plt.text(x=0.08, y=0.0, s=array_to_string(interseccion), fontsize=33, fontweight='bold', color='purple')
    # nterseccion entre conjunto 1 y 3
    plt.text(x=0.0, y=-0.2, s=array_to_string(interseccion2), fontsize=33, fontweight='bold', color='purple')
    # nterseccion entre conjunto 2 y 3
    plt.text(x=0.2, y=-0.2, s=array_to_string(interseccion3), fontsize=33, fontweight='bold', color='purple')

    plt.xlim(-0.3, 0.5)
    plt.ylim(-0.6, 0.3)
    plt.show()

def diagrama_venn_diferencia(conjunto1, conjunto2):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("Diagrama de Venn")

    # restar el conjunto 1 del conjunto 2
    conjunto_1 = array_to_string(diferencia_conjuntos(conjunto1, conjunto2))

    plt.text(x=-0.17, y=-0.03, s=conjunto_1, rotation=50, fontsize=33, fontweight='bold', color='black')

    plt.scatter(x=[0, 0.25], y=[0, 0], s=100000, color=['red', 'white'])

    plt.xlim(-0.3, 0.5)
    plt.ylim(-0.4, 0.4)
    plt.show()

def diagrama_venn_complemento(conjunto1, conjunto2):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("Diagrama de Venn")

    cuadrado = plt.Rectangle((-0.3, -0.4), 1, 1, color='blue')
    # Añadir el cuadrado a los ejes
    ax.add_patch(cuadrado)
    # Dibujar otros elementos (pueden estar encima del cuadrado)
    ax.plot(zorder=1)

    # Establecer límites de los ejes
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)

    # Circunferencias
    plt.scatter(x=[0, 0.25], y=[0, 0], s=100000, color=['blue', 'red'], edgecolor='red')

    complemento = complemento_conjuntos(conjunto1, conjunto2)

    # restar el conjunto 1 de la union
    conjunto_1 = array_to_string(complemento)
#     restar el conjunto 2 de la union
    conjunto_2 = array_to_string(diferencia_conjuntos(conjunto1, complemento))

    plt.text(x=-0.17, y=-0.03, s=conjunto_1, rotation=50, fontsize=33, fontweight='bold', color='red')
    plt.text(x=0.25, y=-0.08, s=conjunto_2, rotation=-55, fontsize=33, fontweight='bold', color='white')
    # interseccion entre los dos conjuntos
    plt.text(x=0.5, y=0.4, s="U", fontsize=33, fontweight='bold', color='purple')

    plt.xlim(-0.3, 0.5)
    plt.ylim(-0.4, 0.4)
    plt.show()

def diagrama_venn_combinacion(conjunto1, conjunto2):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("Diagrama de Venn")

    plt.scatter(x=[0, 0.3], y=[-.1, -.1], s=150000, color=['red', 'red'], alpha=0.3)

    union = union_conjuntos(conjunto1, conjunto2)

    # restar el conjunto 1 de la union
    conjunto_1 = array_to_string(diferencia_conjuntos(union, conjunto2))
    # restar el conjunto 2 de la union
    conjunto_2 = array_to_string(diferencia_conjuntos(union, conjunto1))

    plt.text(x=-0.17, y=-0.1, s=conjunto_1, rotation=50, fontsize=33, fontweight='bold', color='red')
    plt.text(x=0.3, y=-0.1, s=conjunto_2, rotation=-55, fontsize=33, fontweight='bold', color='blue')
    # union entre los dos conjuntos
    plt.text(x=0.0, y=-0.15, s=array_to_string(union), fontsize=33, fontweight='bold', color='purple')

    plt.xlim(-0.25, 0.5)
    plt.ylim(-0.4, 0.2)
    plt.show()

def diagrama_venn_cardinalidad(conjunto1, conjunto2):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("Diagrama de Venn")

    plt.scatter(x=[0, 0.3], y=[-.1, -.1], s=10000, color=['red', 'blue'], alpha=0.3)

    cardinalidad = cardinalidad_conjuntos(conjunto1, conjunto2)

    conjunto_1 = cardinalidad[0]
    conjunto_2 = cardinalidad[1]

    plt.text(x=0, y=-0.1, s=conjunto_1, fontsize=33, fontweight='bold', color='red')
    plt.text(x=0.3, y=-0.1, s=conjunto_2, fontsize=33, fontweight='bold', color='blue')

    plt.xlim(-0.25, 0.5)
    plt.ylim(-0.4, 0.2)
    plt.show()

def diagrama_venn_subconjunto(conjunto1, conjunto2):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("Diagrama de Venn")

    if es_subconjunto(conjunto1, conjunto2):

        plt.scatter(x=[0.1, 0.1], y=[-.1, -.1], s=[100000, 10000], color=['red', 'blue'], alpha=0.3)

        plt.text(x=0.05, y=-0.2, s=array_to_string(diferencia_conjuntos(conjunto2, conjunto1)), fontsize=33, fontweight='bold', color='red')
        plt.text(x=0.05, y=-0.1, s=array_to_string(interseccion_conjuntos(conjunto1, conjunto2)), fontsize=33, fontweight='bold', color='blue')

        plt.xlim(-0.25, 0.5)
        plt.ylim(-0.4, 0.2)
        plt.show()

    else:
        plt.text(x=0, y=-0.1, s="No es subconjunto", fontsize=33, fontweight='bold', color='red')

        plt.xlim(-0.25, 0.5)
        plt.ylim(-0.4, 0.2)
        plt.show()

def diagrama_venn_disjuntos(conjunto1, conjunto2):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("Diagrama de Venn")

    if disjuntos_conjuntos(conjunto1, conjunto2):

        plt.scatter(x=[0, 0.3], y=[-.1, -.1], s=19000, color=['red', 'blue'], alpha=0.3)

        plt.text(x=-0.06, y=-0.1, s=array_to_string(conjunto1), fontsize=33, fontweight='bold', color='red')
        plt.text(x=0.22, y=-0.1, s=array_to_string(conjunto2), fontsize=33, fontweight='bold', color='blue')

        plt.xlim(-0.25, 0.5)
        plt.ylim(-0.4, 0.2)
        plt.show()

    else:
        plt.text(x=0, y=-0.1, s="No es disjunto", fontsize=33, fontweight='bold', color='red')

        plt.xlim(-0.25, 0.5)
        plt.ylim(-0.4, 0.2)
        plt.show()

main()
