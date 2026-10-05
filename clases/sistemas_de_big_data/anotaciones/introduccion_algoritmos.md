# Introducción a los Algoritmos

## Complejidad Computacional (Big O Notation)

El análisis de la complejidad computacional nos permite entender cómo se comporta un algoritmo en términos de tiempo de ejecución y uso de memoria a medida que crece el tamaño de los datos de entrada ($n$).

A continuación se presenta un gráfico comparativo con las diferentes clases de complejidad, desde las más óptimas hasta las más costosas computacionalmente:

![Gráfico de Complejidad Computacional](img/complejidad_computacional.png)

> 💡 **Nota:** 
> - **$O(1)$ y $O(\log n)$:** Son altamente eficientes, escalando perfectamente con grandes volúmenes de datos.
> - **$O(n)$ y $O(n \log n)$:** Tienen un crecimiento manejable y son comunes en muchos algoritmos eficientes de búsqueda y ordenación.
> - **$O(n^2)$ y $O(2^n)$:** Su coste crece rápidamente de forma cuadrática o exponencial, volviéndose impracticables para entradas de datos grandes (como es habitual en entornos de Big Data).

### Ejemplo Práctico en Python

A continuación, un pequeño ejemplo en Python para ilustrar la diferencia entre una operación de complejidad constante $O(1)$ y una lineal $O(n)$:

```python
import time

def obtener_primer_elemento(datos):
    """Ejemplo de O(1) - Tiempo constante"""
    return datos[0] if datos else None

def buscar_elemento(datos, objetivo):
    """Ejemplo de O(n) - Tiempo lineal"""
    for elemento in datos:
        if elemento == objetivo:
            return True
    return False

# Generamos un dataset de prueba
datos_prueba = list(range(1000000))

# Prueba O(1)
inicio = time.time()
obtener_primer_elemento(datos_prueba)
fin = time.time()
print(f"Tiempo O(1): {fin - inicio:.6f} segundos")

# Prueba O(n) (en el peor de los casos, buscando el último elemento)
inicio = time.time()
buscar_elemento(datos_prueba, 999999)
fin = time.time()
print(f"Tiempo O(n): {fin - inicio:.6f} segundos")
```
