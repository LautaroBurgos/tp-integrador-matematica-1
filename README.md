# Trabajo Integrador 2: Matemática y Programación


## Integrantes:
- Matías Facundo Herrera
- Leandro Bareiro
- Alexis Borda
- Lautaro Burgos

## Objetivo del Proyecto
Este trabajo busca integrar conocimientos de Matemática (conjuntos y lógica) y Programación (estructuras condicionales, funciones y bucles), desarrollando habilidades de razonamiento lógico, codificación, junto con trabajo en equipo.

---

## Parte 1 – Desarrollo Matemático

A partir de los DNIs de los integrantes, se generaron conjuntos de dígitos únicos. Luego se realizaron operaciones entre conjuntos: unión, intersección, diferencia y diferencia simétrica. También se redactaron expresiones lógicas que posteriormente se implementaron en el programa.

### Operaciones con conjuntos:
- Unión: A ∪ B = {…}
- Intersección: A ∩ B = {…}
- Diferencia (A - B): {…}
- Diferencia simétrica: A Δ B = {…}

### Expresiones lógicas:
1. **"Si todos los conjuntos tienen al menos 6 elementos, entonces hay alta diversidad numérica."**
   - Se cumple en un caso.

2. **"Si un dígito aparece en todos los conjuntos, se marca como dígito común."**
   - No se cumple

3. **"Si la suma de los dígitos de dos dnis es igual, entonces hay al menos un Par de dni con mismo valor"**
   - No se cumple

---

## Parte 2 – Desarrollo del Programa en Python

El archivo Python implementa las funcionalidades requeridas, organizadas en funciones con un menú de opciones para que el usuario elija cuál visualizar.
### Requisitos previos

- Python 3.x
### Funcionalidades del programa:
- Ingreso de DNIs y años de nacimiento.
- Generación automática de conjuntos de dígitos únicos.
- Cálculo y visualización de:
  - Unión
  - Intersección
  - Diferencias
  - Diferencia simétrica
- Conteo de frecuencia de cada dígito por DNI.
- Suma total de los dígitos de cada DNI.
- Evaluación de condiciones lógicas, por ejemplo:
  - “Dígito compartido”
  - “Diversidad numérica alta”
- Operaciones con años:
  - Cantidad de años pares e impares.
  - Detección de año bisiesto.
  - Determinación de "Grupo Z".
  - Producto cartesiano entre años y edades actuales.

### Lógica implementada en código (condiciones evaluadas):
- Si un dígito aparece en todos los conjuntos → imprime “Dígito compartido”.
- Si un conjunto tiene más de 6 elementos → imprime “Diversidad numérica alta”.
- Si todos nacieron después del 2000 → imprime “Grupo Z”.
- Si alguno nació en año bisiesto → imprime “Tenemos un año especial”.

---

## Parte 3 – Video de Presentación

🔗 [Link al video](https://youtube.com/...)
---


