import json


class AplikacjaMobilna:
    liczba_pobran = 0

    def __init__(self, nazwa, wersja):
        self.nazwa = nazwa
        self.wersja = wersja

    def nowe_pobranie(self):
        AplikacjaMobilna.liczba_pobran += 1

    @classmethod
    def ile_pobran(cls):
        return (f"Liczba pobran wynosi: {cls.liczba_pobran}")

    def z_json(cls, nazwa_pliku):
        with open(nazwa_pliku, 'r') as plik:
            dane = json.load(plik)
            return AplikacjaMobilna(dane['nazwa'], dane['wersja'])


aplikacjamobilna = AplikacjaMobilna("Facebook", "1.19.2")
aplikacjamobilna.nowe_pobranie()
print(aplikacjamobilna.ile_pobran())

aplikacjamobilna_2 = aplikacjamobilna.z_json("app.json")
aplikacjamobilna_2.nowe_pobranie()
print(aplikacjamobilna_2.ile_pobran())
