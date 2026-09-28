"""Colores ANSI y constantes compartidas para la salida en consola."""

import os

EPSILON = "ε"

# Habilita colores ANSI en la terminal de Windows
os.system("")
AZUL, VERDE, ROJO, AMARILLO, NEGRITA, RESET = (
    "\033[94m", "\033[92m", "\033[91m", "\033[93m", "\033[1m", "\033[0m"
)
