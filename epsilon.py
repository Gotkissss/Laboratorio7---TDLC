"""Eliminacion de producciones-epsilon mostrando cada paso del algoritmo."""

from itertools import product

from colores import AMARILLO, AZUL, EPSILON, NEGRITA, RESET, VERDE
from impresion import cuerpo_a_texto


def encontrar_anulables(producciones):
    """Calcula el conjunto de simbolos anulables mostrando cada iteracion."""
    print(f"\n{AZUL}{NEGRITA}PASO 1: Encontrar simbolos anulables{RESET}")

    anulables = {nt for nt, cuerpos in producciones.items() if () in cuerpos}
    print(f"  Base: no-terminales con produccion {EPSILON} directa -> "
          f"{{{', '.join(sorted(anulables))}}}")

    iteracion = 1
    while True:
        nuevos = set()
        for nt, cuerpos in producciones.items():
            if nt in anulables:
                continue
            for cuerpo in cuerpos:
                if cuerpo and all(s in anulables for s in cuerpo):
                    nuevos.add(nt)
                    print(f"  Iteracion {iteracion}: {nt} es anulable porque "
                          f"{nt} → {cuerpo_a_texto(cuerpo)} y todos sus simbolos son anulables")
                    break
        if not nuevos:
            print(f"  Iteracion {iteracion}: no hay nuevos anulables, se detiene.")
            break
        anulables |= nuevos
        iteracion += 1

    print(f"  {VERDE}Conjunto de anulables = {{{', '.join(sorted(anulables))}}}{RESET}")
    return anulables


def eliminar_epsilon(inicial, producciones):
    anulables = encontrar_anulables(producciones)

    print(f"\n{AZUL}{NEGRITA}PASO 2: Generar nuevas producciones (2^m combinaciones){RESET}")
    nuevas = {}

    for nt, cuerpos in producciones.items():
        nuevas[nt] = []
        for cuerpo in cuerpos:
            if not cuerpo:
                print(f"\n  {nt} → {EPSILON}   (se elimina la produccion-{EPSILON})")
                continue

            posiciones = [i for i, s in enumerate(cuerpo) if s in anulables]
            m = len(posiciones)
            print(f"\n  {nt} → {cuerpo_a_texto(cuerpo)}   "
                  f"anulables: {[cuerpo[i] for i in posiciones] or 'ninguno'}  "
                  f"(m = {m}, 2^{m} = {2 ** m} caso{'s' if m else ''})")

            # Cada combinacion decide si se conserva (True) u omite (False)
            # cada simbolo anulable
            for mascara in product([True, False], repeat=m):
                omitidos = {pos for pos, conservar in zip(posiciones, mascara) if not conservar}
                resultado = tuple(s for i, s in enumerate(cuerpo) if i not in omitidos)
                descripcion = ", ".join(
                    f"{'con' if c else 'sin'} {cuerpo[p]}" for p, c in zip(posiciones, mascara)
                ) or "sin cambios"

                if not resultado:
                    nota = f"{AMARILLO}descartada (cuerpo vacio = {EPSILON}){RESET}"
                elif resultado == (nt,):
                    nota = f"{AMARILLO}descartada ({nt} → {nt} es trivial){RESET}"
                elif resultado in nuevas[nt]:
                    nota = "repetida"
                else:
                    nuevas[nt].append(resultado)
                    nota = f"{VERDE}agregada{RESET}"
                print(f"      [{descripcion}]  ->  {nt} → {cuerpo_a_texto(resultado)}   {nota}")

    # Quitar no-terminales que quedaron sin producciones
    vacios = [nt for nt, c in nuevas.items() if not c]
    for nt in vacios:
        print(f"\n  {AMARILLO}{nt} se queda sin producciones y se elimina.{RESET}")
        del nuevas[nt]

    if inicial in anulables:
        print(f"\n  {AMARILLO}Nota: el simbolo inicial {inicial} es anulable, por lo que "
              f"{EPSILON} ∈ L(G). La nueva gramatica genera L(G) - {{{EPSILON}}}.{RESET}")

    return nuevas
