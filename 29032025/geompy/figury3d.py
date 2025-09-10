"""
Moduł do obliczeń na figurach 3D.
"""

import math


class Szescian:
    """Klasa reprezentująca sześcian."""

    def __init__(self, bok):
        """
        Inicjalizuje sześcian.

        Args:
            bok (float): Długość boku sześcianu.
        """
        self.bok = bok

    def objetosc(self):
        """Oblicza objętość sześcianu."""
        return self.bok ** 3

    def pole_powierzchni(self):
        """Oblicza pole powierzchni całkowitej sześcianu."""
        return 6 * self.bok ** 2


class Prostopadloscian:
    """Klasa reprezentująca prostopadłościan."""

    def __init__(self, dlugosc, szerokosc, wysokosc):
        """
        Inicjalizuje prostopadłościan.

        Args:
            dlugosc (float): Długość prostopadłościanu.
            szerokosc (float): Szerokość prostopadłościanu.
            wysokosc (float): Wysokość prostopadłościanu.
        """
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc

    def objetosc(self):
        """Oblicza objętość prostopadłościanu."""
        return self.dlugosc * self.szerokosc * self.wysokosc

    def pole_powierzchni(self):
        """Oblicza pole powierzchni całkowitej prostopadłościanu."""
        return 2 * (self.dlugosc * self.szerokosc +
                    self.dlugosc * self.wysokosc +
                    self.szerokosc * self.wysokosc)


class Kula:
    """Klasa reprezentująca kulę."""

    def __init__(self, promien):
        """
        Inicjalizuje kulę.

        Args:
            promien (float): Promień kuli.
        """
        self.promien = promien

    def objetosc(self):
        """Oblicza objętość kuli."""
        return (4 / 3) * math.pi * self.promien ** 3

    def pole_powierzchni(self):
        """Oblicza pole powierzchni całkowitej kuli."""
        return 4 * math.pi * self.promien ** 2