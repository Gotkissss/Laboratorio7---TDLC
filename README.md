# Laboratorio 7 - Teoría de la Computación

## Video de demostración (Problema 1)



## Problema 1

Programa en Python que:

1. Carga gramáticas desde archivos de texto (`gramaticas/`).
2. Valida cada línea con una expresión regular; si una línea está mal escrita, la ejecución se detiene.
3. Elimina las producciones-ε mostrando los pasos:
   - Cálculo de los símbolos anulables (por iteraciones).
   - Generación de las 2^m combinaciones por cada producción con m símbolos anulables.
4. Muestra la gramática resultante sin producciones-ε.

### Estructura

| Archivo | Contenido |
|---|---|
| `main.py` | Punto de entrada: carga cada gramática y ejecuta el algoritmo |
| `validador.py` | Expresión regular y carga/validación de los archivos |
| `epsilon.py` | Cálculo de anulables y eliminación de producciones-ε (2^m casos) |
| `impresion.py` | Funciones para mostrar gramáticas en pantalla |
| `colores.py` | Colores ANSI y constantes compartidas |
| `gramaticas/` | Archivos de texto con las gramáticas 1 y 2 |

### Formato de los archivos

- Una producción por línea, con alternativas separadas por `|`.
- Mayúscula = no-terminal, minúscula o dígito = terminal, `ε` = cadena vacía.
- Flecha `->` o `→`.

```
S -> 0A0 | 1B1 | BB
C -> S | ε
```

### Ejecución

Requiere Python 3.8+ (sin librerías externas).

```bash
python main.py                            # procesa todas las gramáticas
python main.py gramaticas/gramatica1.txt  # procesa un archivo
```

## Problema 2

Las respuestas están en la carpeta [`problema2/`](problema2/) en formato PDF.
