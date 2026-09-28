"""Utilidades para mostrar gramaticas en pantalla."""

from colores import EPSILON


def cuerpo_a_texto(cuerpo):
    return "".join(cuerpo) if cuerpo else EPSILON


def imprimir_gramatica(producciones, inicial):
    orden = [inicial] + [nt for nt in producciones if nt != inicial]
    for nt in orden:
        if nt in producciones and producciones[nt]:
            cuerpos = " | ".join(cuerpo_a_texto(c) for c in producciones[nt])
            print(f"    {nt} → {cuerpos}")
