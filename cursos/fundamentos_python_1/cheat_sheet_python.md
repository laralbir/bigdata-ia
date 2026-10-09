# 🐍 Cheat Sheet: De TypeScript / Node / PHP a Python

Esta guía está diseñada para desarrolladores que ya dominan TypeScript, Node.js o PHP y necesitan adaptarse rápidamente a la sintaxis y el ecosistema de Python para trabajar en Big Data e IA.

---

## 1. Ecosistema y Entorno

| Concepto (Node/PHP) | Equivalencia en Python | Ejemplo / Comentario |
| :--- | :--- | :--- |
| `npm init` / `composer init` | **Entornos Virtuales** | `python -m venv .venv` (Crea un entorno aislado) |
| Activar entorno | `source .venv/bin/activate` | **Obligatorio** antes de instalar nada. (En Windows: `.venv\Scripts\activate`) |
| `npm install <pkg>` | `pip install <pkg>` | Instala una librería en tu entorno virtual activo. |
| `package.json` | `requirements.txt` | Para generar: `pip freeze > requirements.txt`<br>Para instalar: `pip install -r requirements.txt` |
| `node_modules/` | Carpeta `.venv/` | Contiene los binarios y dependencias locales. |
| `npm run dev` | `python main.py` | Ejecución directa del script principal. |

---

## 2. Sintaxis Básica y Operadores

### Variables y Tipos
Python es de tipado dinámico, no existen `let`, `const` ni `var`. 
*Nota: Para constantes se usa convención de MAYÚSCULAS.*

```python
# TypeScript
const nombre = "Carlos";
let edad = 30;
let activo = true;
let nulo = null;

# Python
nombre = "Carlos"
EDAD_MAXIMA = 30  # Convención para constantes
activo = True     # Mayúscula inicial
nulo = None       # El equivalente a null/undefined
```

### Interpolación de Strings (Template literals)
```python
# TypeScript: console.log(`Hola ${nombre}`);
# Python usa las f-strings (format strings):
print(f"Hola {nombre}")
```

### Operadores Lógicos, Ternarios y Cortocircuitos
```python
# JS/TS: &&, ||, !
# Python: and, or, not
if activo and not nulo:
    print("Funciona")

# 1. Ternario oficial
# JS: const x = edad > 18 ? "Mayor" : "Menor"
# Python (primero va el valor verdadero):
x = "Mayor" if edad > 18 else "Menor"

# 2. Cortocircuito lógico (Hack estilo JS/PHP)
# JS: const x = (edad > 18) && "Mayor" || "Menor"
# Python:
x = (edad > 18) and "Mayor" or "Menor"
# ⚠️ Peligro: Falla si el valor verdadero se evalúa como False (ej. 0, "", None)
```

---

## 3. Estructuras de Datos

### Arrays (Listas en Python)
```python
# TS: const arr = [1, 2, 3]; arr.push(4); console.log(arr.length);
arr = [1, 2, 3]
arr.append(4)     # push -> append
print(len(arr))   # .length -> len()
```

### Objects (Diccionarios en Python)
```python
# TS: const usuario = { nombre: "Carlos", edad: 30 };
# TS: console.log(usuario.nombre);

usuario = {
    "nombre": "Carlos",
    "edad": 30
}
# En Python NO puedes usar la notación de punto para diccionarios
print(usuario["nombre"])  
print(usuario.get("apellido", "No encontrado")) # Evita errores si no existe
```

---

## 4. Control de Flujo (Bucles y Condicionales)

La principal diferencia es que **Python no usa llaves `{}` sino indentación (espacios)** y **dos puntos `:`**.

### Condicionales
```python
# if / else if / else
if edad < 18:
    print("Menor")
elif edad == 18:      # else if -> elif
    print("Exactamente 18")
else:
    print("Mayor")
```

### Bucles (For / Foreach)
```python
# TS: for (const item of arr) { ... }
# Python:
for item in arr:
    print(item)

# TS: for (let i = 0; i < 5; i++) { ... }
# Python (usando range):
for i in range(5):    # 0, 1, 2, 3, 4
    print(i)
```

---

## 5. Funciones y Arrow Functions

```python
# TS: function sumar(a: number, b: number): number { return a + b; }
# Python (con Type Hints):
def sumar(a: int, b: int) -> int:
    return a + b

# Arrow Functions (Lambdas)
# TS: const doblar = x => x * 2;
# Python (muy limitadas, ideal para pasar a otras funciones):
doblar = lambda x: x * 2
```

---

## 6. Programación Orientada a Objetos (Clases)

```python
# TypeScript
class Persona {
    constructor(public nombre: string) {}
    saludar() {
        console.log(`Hola, soy ${this.nombre}`);
    }
}

# Python
class Persona:
    # El constructor siempre se llama __init__
    # 'self' es obligatorio como primer parámetro (equivale a 'this')
    def __init__(self, nombre: str):
        self.nombre = nombre
        
    def saludar(self):
        print(f"Hola, soy {self.nombre}")

p = Persona("Carlos")
p.saludar()
```

---

## 7. Asincronía (Async / Await)
Funciona de manera muy similar a Node.js, pero usando la librería estándar `asyncio`.

```python
import asyncio

# TS: async function fetchData() { await delay(); }
async def fetch_data():
    print("Empezando...")
    await asyncio.sleep(2) # Simula un delay (Promise.resolve)
    print("Terminado")

# Para ejecutar la promesa principal (Event Loop):
asyncio.run(fetch_data())
```

---

## 8. Librerías de Big Data e IA (Tu arsenal principal)
Cuando entres al máster, esto será tu día a día:

*   **Pandas:** Es como manipular bases de datos SQL o Excel directamente en código.
*   **NumPy:** Trabajo con matrices a bajo nivel y muy rápido (escrito en C).
*   **Scikit-Learn:** Algoritmos clásicos de Machine Learning listos para usar (modelos, regresiones).
*   **Matplotlib / Seaborn:** Para dibujar gráficas con tus datos.
*   **Jupyter Notebooks (`.ipynb`):** Archivos especiales donde ejecutas código por "bloques" y ves los resultados o gráficas al instante. (Imprescindible instalarlos).
