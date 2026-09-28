"""
Laboratorio 7 - Teoria de la Computacion

"""

import os
import sys

from colores import EPSILON, NEGRITA, RESET, ROJO, VERDE
from epsilon import eliminar_epsilon
from impresion import imprimir_gramatica
from validador import cargar_gramatica


def procesar(ruta):
    print("=" * 70)
    print(f"{NEGRITA}Archivo: {ruta}{RESET}")
    print("=" * 70)

    inicial, producciones = cargar_gramatica(ruta)

    print(f"\n{NEGRITA}Gramatica original (simbolo inicial: {inicial}):{RESET}")
    imprimir_gramatica(producciones, inicial)

    resultado = eliminar_epsilon(inicial, producciones)

    print(f"\n{VERDE}{NEGRITA}RESULTADO: gramatica sin producciones-{EPSILON}:{RESET}")
    imprimir_gramatica(resultado, inicial)
    print()


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    rutas = sys.argv[1:]
    if not rutas:
        carpeta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gramaticas")
        rutas = sorted(os.path.join(carpeta, f) for f in os.listdir(carpeta) if f.endswith(".txt"))

    for ruta in rutas:
        if not os.path.isfile(ruta):
            print(f"{ROJO}ERROR: no existe el archivo '{ruta}'.{RESET}")
            sys.exit(1)
        procesar(ruta)


if __name__ == "__main__":
    main()
