# Python Fundamentals Exercises

Colección de ejercicios de fundamentos de Python desarrollados como parte de un proceso de mentoría técnica. Cada función está implementada con manejo de casos edge y validación de tipos, y verificada mediante tests unitarios con pytest.

---

## Ejercicios implementados

### Algoritmos y lógica
- **Palíndromo** — detecta si una cadena es palíndromo, ignorando espacios, puntuación y mayúsculas
- **FizzBuzz** — implementación clásica con soporte para entrada numérica y string
- **Número primo** — verifica si un número es primo con validación de tipos
- **Año bisiesto** — aplica correctamente las reglas del calendario gregoriano (400/100/4)
- **Calculadora** — parsea y evalúa expresiones aritméticas básicas desde un string

### Fechas
- **Diferencia entre fechas** — calcula la diferencia entre dos fechas en años, meses o días con ajuste fino de calendario

### Álgebra lineal
- **Suma de vectores** — suma elemento a elemento con validación de dimensiones
- **Multiplicación de vector por escalar** — con validación de tipos numéricos
- **Suma de matrices** — con validación de dimensiones y tipos
- **Multiplicación de matrices** — implementación completa con validación de compatibilidad dimensional

### Programación Orientada a Objetos (POO)
- **Clase `Person`** — atributos de nombre y fecha de nacimiento, cálculo de edad por fecha de referencia, método de saludo entre instancias
- **Clase `Employee`** — hereda estructura de persona, agrega rol laboral y método de información

---

## Tests

Todos los ejercicios cuentan con tests unitarios escritos con `pytest`, incluyendo casos felices y casos edge (entradas inválidas, tipos incorrectos, valores límite).

Para ejecutar los tests:
```bash
pip install pytest
pytest test_utils.py -v
```

---

## Stack

- Python 3.9+
- pytest

---

## Contexto

Estos ejercicios fueron desarrollados como parte de un proceso de mentoría técnica, siguiendo un flujo de trabajo colaborativo con Git: fork del repositorio, implementación de cada ejercicio en ramas independientes, pull requests y revisión de código por parte del instructor.
