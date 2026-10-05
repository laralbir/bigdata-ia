# Introducción a los Algoritmos

## Complejidad Computacional

El análisis de la complejidad computacional nos permite entender y predecir el rendimiento de nuestros algoritmos cuando trabajan con volúmenes de datos que tienden a infinito, algo especialmente crítico en entornos de Big Data.

### Introducción a la notación Big O
La notación Big O describe el **comportamiento asintótico** de un algoritmo. Se utiliza para clasificar algoritmos en función de cómo responden a cambios en el tamaño de la entrada de datos (representado como $n$).

Las clases principales de complejidad asintótica (de más eficientes a menos eficientes) son:
$O(1), O(\log n), O(n), O(n \log n), O(n^2), O(2^n)$

![Gráfico de Complejidad Computacional](img/complejidad_computacional.png)

### Análisis de Tiempo y Espacio
El análisis computacional se evalúa principalmente en dos ejes fundamentales:
- **Tiempo:** Determinado por el número de operaciones básicas que realiza el algoritmo.
- **Espacio:** Determinado por la memoria adicional requerida durante la ejecución.

---

### Clasificación de algoritmos y Casos Prácticos

A continuación se detalla la clasificación según su complejidad, usando ejemplos clásicos implementados en Python:

#### 1. Complejidad Constante $O(1)$
El tiempo de ejecución y el espacio en memoria no dependen del tamaño de entrada. 
**Ejemplo:** Acceso directo a un elemento en un array lineal.

```python
def acceso_directo(datos, indice):
    """
    Complejidad O(1). 
    No importa el tamaño de 'datos', acceder a un índice 
    concreto siempre toma el mismo número de operaciones básicas.
    """
    return datos[indice]
```

#### 2. Complejidad Logarítmica $O(\log n)$
El tiempo de ejecución crece de forma logarítmica respecto a $n$, típicamente cuando el conjunto de datos se divide en cada paso.
**Ejemplo:** Búsqueda binaria (requiere que los datos estén previamente ordenados).

```python
def busqueda_binaria(datos_ordenados, objetivo):
    """
    Complejidad O(log n). 
    Descarta sistemáticamente la mitad de los datos en cada iteración,
    haciéndolo extremadamente eficiente para listas muy grandes.
    """
    izquierda, derecha = 0, len(datos_ordenados) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if datos_ordenados[medio] == objetivo:
            return medio
        elif datos_ordenados[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1
```

#### 3. Complejidad Lineal $O(n)$
El tiempo de ejecución crece proporcionalmente al tamaño de entrada $n$.
**Ejemplo:** Búsqueda secuencial.

```python
def busqueda_secuencial(datos, objetivo):
    """
    Complejidad O(n). 
    En el peor de los casos, se debe recorrer y comparar 
    cada uno de los elementos de toda la colección de datos.
    """
    for elemento in datos:
        if elemento == objetivo:
            return True
    return False
```

#### 4. Complejidad Cuadrática $O(n^2)$
El tiempo crece de forma cuadrática respecto a la entrada. Es típico de algoritmos con bucles anidados sobre toda la colección.
**Ejemplo:** Ordenamiento por burbuja (Bubble sort).

```python
def ordenamiento_burbuja(datos):
    """
    Complejidad O(n^2). 
    Compara todos los elementos con todos, utilizando bucles anidados.
    Muy poco eficiente y a evitar para conjuntos de datos grandes.
    """
    n = len(datos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if datos[j] > datos[j + 1]:
                # Intercambiar elementos
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
    return datos
```

> 💡 **Nota sobre escalabilidad:** En arquitecturas y sistemas de Big Data, se debe priorizar buscar soluciones y algoritmos que operen en $O(1)$, $O(\log n)$, o a lo sumo $O(n)$ u $O(n \log n)$. Cualquier operación cuadrática $O(n^2)$ (como producto cartesiano o ordenamientos poco optimizados) sobre miles de millones de registros resulta inviable en tiempo.
