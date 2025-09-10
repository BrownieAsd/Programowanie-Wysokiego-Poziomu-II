"""
Moduł do obliczeń na figurach 2D.
"""

import math


class Kwadrat:
    """Klasa reprezentująca kwadrat."""

    def __init__(self, bok):
        """
        Inicjalizuje kwadrat.

        Args:
            bok (float): Długość boku kwadratu.
        """
        self.bok = bok

    def pole(self):
        """Oblicza pole kwadratu."""
        return self.bok ** 2

    def obwod(self):
        """Oblicza obwód kwadratu."""
        return 4 * self.bok


class Prostokat:
    """Klasa reprezentująca prostokąt."""

    def __init__(self, dlugosc, szerokosc):
        """
        Inicjalizuje prostokąt.

        Args:
            dlugosc (float): Długość prostokąta.
            szerokosc (float): Szerokość prostokąta.
        """
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def pole(self):
        """Oblicza pole prostokąta."""
        return self.dlugosc * self.szerokosc

    def obwod(self):
        """Oblicza obwód prostokąta."""
        return 2 * (self.dlugosc + self.szerokosc)


class Kolo:
    """Klasa reprezentująca koło."""

    def __init__(self, promien):
        """
        Inicjalizuje koło.

        Args:
            promien (float): Promień koła.
        """
        self.promien = promien

    def pole(self):
        """Oblicza pole koła."""
        return math.pi * self.promien ** 2

    def obwod(self):
        """Oblicza obwód koła."""
        return 2 * math.pi * self.promien