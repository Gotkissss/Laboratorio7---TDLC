"""Carga de gramaticas desde archivos y validacion con expresiones regulares."""

import re
import sys

from colores import AMARILLO, NEGRITA, RESET, ROJO, VERDE

# Cuerpo de produccion: una o mas letras/digitos, o epsilon (ε / ϵ)
CUERPO = r"(?:[A-Za-z0-9]+|[εϵ])"
# Produccion completa:  NoTerminal  flecha  cuerpo ( | cuerpo )*
REGEX_PRODUCCION = re.compile(
    r"^\s*([A-Z])\s*(?:->|→)\s*(" + CUERPO + r"(?:\s*\|\s*" + CUERPO + r")*)\s*$"
)


def cargar_gramatica(ruta):
    """Lee el archivo, valida cada linea con la regex y construye la gramatica.

    Devuelve (inicial, producciones) donde producciones es un dict
    {NoTerminal: [cuerpo, ...]} y cada cuerpo es una tupla de simbolos
    (la tupla vacia representa epsilon).
    """
    producciones = {}
    inicial = None

    with open(ruta, encoding="utf-8") as f:
        lineas = f.readlines()

    print(f"{NEGRITA}Validando lineas con la expresion regular:{RESET}")
    print(f"  {REGEX_PRODUCCION.pattern}\n")

    for num, linea in enumerate(lineas, start=1):
        texto = linea.strip()
        if not texto or texto.startswith("#"):
            continue  # lineas vacias o comentarios

        coincidencia = REGEX_PRODUCCION.match(texto)
        if not coincidencia:
            print(f"  {ROJO}✗ Linea {num}: '{texto}'  -> NO es una produccion valida{RESET}")
            print(f"\n{ROJO}{NEGRITA}ERROR: la gramatica en '{ruta}' esta mal escrita. "
                  f"Se detiene la ejecucion.{RESET}")
            sys.exit(1)

        print(f"  {VERDE}✓ Linea {num}: {texto}{RESET}")
        cabeza = coincidencia.group(1)
        if inicial is None:
            inicial = cabeza  # el primer no-terminal es el simbolo inicial

        for alternativa in coincidencia.group(2).split("|"):
            alternativa = alternativa.strip()
            cuerpo = () if alternativa in ("ε", "ϵ") else tuple(alternativa)
            lista = producciones.setdefault(cabeza, [])
            if cuerpo not in lista:
                lista.append(cuerpo)

    if inicial is None:
        print(f"{ROJO}ERROR: el archivo '{ruta}' no contiene producciones.{RESET}")
        sys.exit(1)

    # Aviso si se usan no-terminales que no tienen producciones
    usados = {s for cuerpos in producciones.values() for c in cuerpos for s in c if s.isupper()}
    sin_definir = sorted(usados - producciones.keys())
    if sin_definir:
        print(f"\n  {AMARILLO}Aviso: no-terminales sin producciones: {', '.join(sin_definir)}{RESET}")

    return inicial, producciones
