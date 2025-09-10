#!/usr/bin/env python3
"""
Przykładowy skrypt demonstrujący użycie pakietu geompy.
"""

import geompy.figury2d as fig2d
import geompy.figury3d as fig3d


def main():
    """Demonstracja działania pakietu geompy."""
    print("=== PRZYKŁADY DZIAŁANIA PAKIETU GEOMPY ===\n")


    print("Figury 2D:")
    print("----------")


    kwadrat = fig2d.Kwadrat(5)
    print(f"Kwadrat (bok=5): pole={kwadrat.pole()}, obwód={kwadrat.obwod()}")


    prostokat = fig2d.Prostokat(4, 6)
    print(f"Prostokąt (4x6): pole={prostokat.pole()}, obwód={prostokat.obwod()}")


    kolo = fig2d.Kolo(3)
    print(f"Koło (promień=3): pole={kolo.pole():.2f}, obwód={kolo.obwod():.2f}")

    print("\nFigury 3D:")
    print("----------")


    szescian = fig3d.Szescian(4)
    print(f"Sześcian (bok=4): objętość={szescian.objetosc()}, pole powierzchni={szescian.pole_powierzchni()}")


    prostopadloscian = fig3d.Prostopadloscian(3, 4, 5)
    print(
        f"Prostopadłościan (3x4x5): objętość={prostopadloscian.objetosc()}, pole powierzchni={prostopadloscian.pole_powierzchni()}")


    kula = fig3d.Kula(2)
    print(f"Kula (promień=2): objętość={kula.objetosc():.2f}, pole powierzchni={kula.pole_powierzchni():.2f}")


if __name__ == "__main__":
    main()