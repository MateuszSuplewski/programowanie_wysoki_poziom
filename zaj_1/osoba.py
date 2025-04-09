class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek


    def przedstaw_sie(self):
        return f"Jestem {self.imie} {self.nazwisko}"


class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, wiek, stanowisko, pensja):
        Osoba.__init__(self, imie, nazwisko, wiek)
        self.stanowisko = stanowisko
        self.pensja = pensja
        # self.stanowisko.przedstaw_sie()

    def info_o_pracy(self):
        return f"Pracuje jako {self.stanowisko}, zarabiam {self.pensja} zł"

class Manager(Pracownik):
    def __init__(self, imie, nazwisko, wiek, stanowisko, pensja, zespol):
        super().__init__(imie, nazwisko, wiek, stanowisko, pensja)
        self.zespol = zespol

    def przedstaw_sie(self):
        return f"Jestem {self.imie} {self.nazwisko}, posiadam {len(self.zespol)} pracownikow"

    def dodaj_do_zespolu(self, pracownik):
        self.zespol.append(pracownik)

osoba_1 = Osoba("Kacper","K", 18)
print(osoba_1.przedstaw_sie())

pracownik_1 = Pracownik("Mateusz", "M", 25, "Inżynier", 30000)

print(pracownik_1.przedstaw_sie())
print(pracownik_1.info_o_pracy())

pracownik_2 = Pracownik("Leonard", "L", 25, "Inżynier", 20000)
pracownik_3 = Pracownik("Marta", "M", 22, "Grafik", 15000)
pracownik_4 = Pracownik("Karolina", "K", 33, "Tester", 19000)


zespol_1 = [pracownik_2, pracownik_3]
manager_1 = Manager("Jan", "J", "43", "Manager", 26000, zespol_1)
print(manager_1.przedstaw_sie())
manager_1.dodaj_do_zespolu(pracownik_4)
print(manager_1.przedstaw_sie())
