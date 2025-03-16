import json
class ModelAI:
    liczba_modeli=0
    def __init__(self, nazwa_modelu, wersja):
        self.nazwa_modelu = nazwa_modelu
        self.wersja = wersja
        self.nowy_model()

    @classmethod
    def ile_modeli(cls):
        return (f"Liczba modeli: {cls.liczba_modeli}")

    @classmethod
    def z_pliku(cls, nazwa_pliku):
        with open(nazwa_pliku, "r") as f:
            text = json.load(f)
            nazwa_modelu=text["nazwa_modelu"]
            wersja=text["wersja"]
            return cls(nazwa_modelu, wersja)
    @classmethod
    def nowy_model(cls):
        ModelAI.liczba_modeli += 1