"""Moduł prostego systemu zarządzania biblioteką."""


class Ksiazka:
    """Reprezentuje książkę w bibliotece."""

    def __init__(self, tytul, autor, dostepna=True):
        """
        Inicjalizuje obiekt książki.

        Args:
            title (str): Tytuł książki.
            author (str): Autor książki.
            available (bool, optional): Czy książka jest dostępna. Domyślnie True.
        """
        self.tytul = tytul
        self.autor = autor
        self.dostepna = dostepna

    def __str__(self):
        """Zwraca reprezentację string książki."""
        status = "dostępna" if self.dostepna else "niedostępna"
        return f"'{self.tytul}' by {self.autor} - {status}"

    def zmien_status(self, nowy_status):
        """
        Zmienia status dostępności książki.

        Args:
            nowy_status (bool): Nowy status dostępności
        """
        self.dostepna = nowy_status


class Biblioteka:
    """Prosty system zarządzania książkami."""

    def __init__(self):
        """Tworzy pustą bibliotekę."""
        self.lista_ksiazek = []

    def dodaj_ksiazke(self, ksiazka):
        """Dodaje książkę do biblioteki."""
        self.lista_ksiazek.append(ksiazka)

    def wypozycz_ksiazke(self, tytul):
        """
        Wypożycza książkę, jeśli jest dostępna.

        Args:
            title (str): Tytuł książki do wypożyczenia.
        """
        for ksiazka in self.lista_ksiazek:
            if ksiazka.Tytul == tytul:
                if ksiazka.dostepna:
                    ksiazka.dostepna = False
                    return f"Wypozyczono: {tytul}"
                return f"Ksiazka {tytul} niedostepna"
        return f"Brak ksiazki: {tytul}"

    def zwroc_ksiazke(self, tytul):
        """
        Zwraca książkę do biblioteki.

        Args:
            title (str): Tytuł zwracanej książki.
        """
        for ksiazka in self.lista_ksiazek:
            if ksiazka.Tytul == tytul:
                ksiazka.dostepna = True
                return f"Zwrocono: {tytul}"
        return f"Nie nalezy do biblioteki: {tytul}"

    def dostepne_ksiazki(self):
        """Zwraca listę dostępnych książek."""
        dostepne = []
        for ksiazka in self.lista_ksiazek:
            if ksiazka.dostepna:
                dostepne.append(ksiazka.Tytul)
        return dostepne


def main():
    """Funkcja demonstracyjna działania biblioteki."""
    biblioteka = Biblioteka()
    biblioteka.dodaj_ksiazke(Ksiazka("Wiedzmin", "Sapkowski"))
    biblioteka.dodaj_ksiazke(Ksiazka("Solaris", "Lem"))
    biblioteka.dodaj_ksiazke(Ksiazka("Lalka", "Prus", False))

    print(biblioteka.wypozycz_ksiazke("Solaris"))
    print(biblioteka.wypozycz_ksiazke("Lalka"))
    print(biblioteka.zwroc_ksiazke("Lalka"))
    print("Dostepne ksiazki: ", biblioteka.dostepne_ksiazki())


if __name__ == "__main__":
    main()
